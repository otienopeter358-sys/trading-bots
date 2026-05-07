"""
AI Trading Bot - Martingale Strategy Implementation
Converts Blockly XML strategy to a fully functional trading bot
Market: Synthetic Index 1HZ10V (Digits/OverUnder)
Strategy: Martingale with Dynamic Prediction Switching
"""

import logging
import time
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
import json
import random

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('trading_bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class TradeStatus(Enum):
    """Trade status enumeration"""
    PENDING = "pending"
    RUNNING = "running"
    WIN = "win"
    LOSS = "loss"
    COMPLETED = "completed"


class PredictionType(Enum):
    """Prediction type for digits"""
    OVER = "over"
    UNDER = "under"


@dataclass
class TradingConfig:
    """Trading configuration from XML"""
    market: str = "synthetic_index"
    submarket: str = "random_index"
    symbol: str = "1HZ10V"
    trade_type: str = "overunder"
    contract_type: str = "both"
    candle_interval: int = 60
    time_machine_enabled: bool = False
    restart_on_error: bool = True
    
    initial_stake: float = 30.0
    stake: float = 30.0
    take_profit: float = 10.0
    stop_loss: float = 300.0
    martingale_multiplier: float = 1.3
    
    under_prediction: int = 8
    over_prediction: int = 6
    
    loss_count: int = 0
    
    def to_dict(self) -> Dict:
        return {
            'market': self.market,
            'submarket': self.submarket,
            'symbol': self.symbol,
            'trade_type': self.trade_type,
            'contract_type': self.contract_type,
            'candle_interval': self.candle_interval,
            'initial_stake': self.initial_stake,
            'stake': self.stake,
            'take_profit': self.take_profit,
            'stop_loss': self.stop_loss,
            'martingale_multiplier': self.martingale_multiplier,
            'under_prediction': self.under_prediction,
            'over_prediction': self.over_prediction,
            'loss_count': self.loss_count
        }


@dataclass
class TradeRecord:
    """Individual trade record"""
    trade_id: str
    timestamp: datetime
    stake: float
    prediction: str
    entry_price: float
    entry_digit: int
    status: TradeStatus
    profit_loss: float = 0.0
    exit_price: Optional[float] = None
    exit_digit: Optional[int] = None
    
    def to_dict(self) -> Dict:
        return {
            'trade_id': self.trade_id,
            'timestamp': self.timestamp.isoformat(),
            'stake': self.stake,
            'prediction': self.prediction,
            'entry_price': self.entry_price,
            'entry_digit': self.entry_digit,
            'status': self.status.value,
            'profit_loss': self.profit_loss,
            'exit_price': self.exit_price,
            'exit_digit': self.exit_digit
        }


class MartingaleStrategy:
    """Martingale trading strategy implementation"""
    
    def __init__(self, config: TradingConfig):
        self.config = config
        self.trades: List[TradeRecord] = []
        self.total_profit = 0.0
        self.total_loss = 0.0
        self.win_count = 0
        self.loss_count = 0
        
        logger.info(f"Martingale Strategy initialized")
    
    def get_prediction(self) -> str:
        """
        Loss count = 0: OVER (digit >= 6)
        Loss count >= 1: UNDER (digit <= 8)
        """
        if self.config.loss_count == 0:
            return PredictionType.OVER.value
        else:
            return PredictionType.UNDER.value
    
    def calculate_next_stake(self, is_win: bool) -> float:
        """Apply Martingale: 1.3x on loss, reset on win"""
        if is_win:
            next_stake = self.config.initial_stake
        else:
            next_stake = self.config.stake * self.config.martingale_multiplier
        
        self.config.stake = next_stake
        return next_stake
    
    def should_take_profit(self) -> bool:
        return self.total_profit >= self.config.take_profit
    
    def should_stop_loss(self) -> bool:
        return self.total_loss <= -self.config.stop_loss
    
    def execute_trade(self, current_price: float, prediction: str) -> TradeRecord:
        """Execute a single trade"""
        trade_id = f"TRADE_{len(self.trades) + 1:05d}_{int(time.time())}"
        entry_digit = int(current_price) % 10
        
        trade = TradeRecord(
            trade_id=trade_id,
            timestamp=datetime.now(),
            stake=self.config.stake,
            prediction=prediction,
            entry_price=current_price,
            entry_digit=entry_digit,
            status=TradeStatus.PENDING
        )
        
        logger.info(f"TRADE: {trade_id} | Stake: ${self.config.stake:.2f} | Prediction: {prediction.upper()} | Price: {current_price:.2f}")
        self.trades.append(trade)
        return trade
    
    def settle_trade(self, trade: TradeRecord, exit_price: float, is_win: bool) -> None:
        """Settle a completed trade"""
        trade.exit_price = exit_price
        trade.exit_digit = int(exit_price) % 10
        trade.status = TradeStatus.WIN if is_win else TradeStatus.LOSS
        
        if is_win:
            trade.profit_loss = trade.stake
            self.total_profit += trade.stake
            self.win_count += 1
            self.config.loss_count = 0
            logger.info(f"✓ WIN | Profit: ${trade.stake:.2f} | Total: ${self.total_profit:.2f}")
        else:
            trade.profit_loss = -trade.stake
            self.total_loss -= trade.stake
            self.loss_count += 1
            self.config.loss_count += 1
            logger.info(f"✗ LOSS | Loss: ${trade.stake:.2f} | Streak: {self.config.loss_count} | Total: ${self.total_loss:.2f}")
        
        self.calculate_next_stake(is_win)
    
    def get_statistics(self) -> Dict:
        """Get trading statistics"""
        total_trades = len(self.trades)
        win_rate = (self.win_count / total_trades * 100) if total_trades > 0 else 0
        net_profit = self.total_profit + self.total_loss
        
        return {
            'total_trades': total_trades,
            'wins': self.win_count,
            'losses': self.loss_count,
            'win_rate': round(win_rate, 2),
            'total_profit': round(self.total_profit, 2),
            'total_loss': round(self.total_loss, 2),
            'net_profit': round(net_profit, 2),
            'current_stake': round(self.config.stake, 2),
            'loss_streak': self.config.loss_count
        }
    
    def export_trades(self, filename: str = "trades.json") -> None:
        """Export trade history to JSON"""
        trades_data = [trade.to_dict() for trade in self.trades]
        with open(filename, 'w') as f:
            json.dump({
                'trades': trades_data,
                'statistics': self.get_statistics(),
                'config': self.config.to_dict()
            }, f, indent=2)
        logger.info(f"Trades exported to {filename}")


class TradingBot:
    """Main trading bot orchestrator"""
    
    def __init__(self, config: TradingConfig, api_provider=None):
        self.config = config
        self.strategy = MartingaleStrategy(config)
        self.api = api_provider
        self.is_running = False
        self.consecutive_errors = 0
        
        logger.info("Trading Bot initialized")
    
    def get_market_data(self) -> Optional[Dict]:
        """Get current market data"""
        try:
            if self.api:
                return self.api.get_ticks(self.config.symbol)
            else:
                price = random.uniform(10000, 15000)
                return {
                    'symbol': self.config.symbol,
                    'price': price,
                    'timestamp': datetime.now().isoformat(),
                    'bid': price * 0.999,
                    'ask': price * 1.001
                }
        except Exception as e:
            logger.error(f"Error fetching market data: {e}")
            self.consecutive_errors += 1
            return None
    
    def analyze_market(self, market_data: Dict) -> tuple:
        """Analyze market and generate prediction"""
        try:
            price = market_data.get('price', 0)
            digit = int(price) % 10
            prediction = self.strategy.get_prediction()
            confidence = (self.config.over_prediction / 10) * 100 if prediction == "over" else (self.config.under_prediction / 10) * 100
            
            logger.info(f"Market: Price={price:.2f} | Digit={digit} | Prediction={prediction.upper()} | Confidence={confidence:.1f}%")
            return prediction, confidence
        except Exception as e:
            logger.error(f"Error analyzing market: {e}")
            return None, 0
    
    def execute_trade_cycle(self) -> bool:
        """Execute one complete trade cycle"""
        try:
            if self.strategy.should_take_profit():
                logger.info("💰 TAKE PROFIT TARGET REACHED!")
                return False
            
            if self.strategy.should_stop_loss():
                logger.info("⚠️  STOP LOSS TRIGGERED!")
                return False
            
            market_data = self.get_market_data()
            if not market_data:
                return False
            
            prediction, confidence = self.analyze_market(market_data)
            if not prediction:
                return False
            
            entry_price = market_data['price']
            trade = self.strategy.execute_trade(entry_price, prediction)
            
            logger.info(f"Waiting {self.config.candle_interval}s for trade to settle...")
            time.sleep(min(self.config.candle_interval, 2))
            
            exit_data = self.get_market_data()
            if not exit_data:
                return False
            
            exit_price = exit_data['price']
            exit_digit = int(exit_price) % 10
            is_win = self._check_prediction(prediction, exit_digit)
            
            self.strategy.settle_trade(trade, exit_price, is_win)
            self.consecutive_errors = 0
            return True
            
        except Exception as e:
            logger.error(f"Error in trade cycle: {e}")
            self.consecutive_errors += 1
            return False
    
    def _check_prediction(self, prediction: str, digit: int) -> bool:
        """Check if prediction was correct"""
        if prediction == "over":
            return digit >= self.config.over_prediction
        else:
            return digit <= self.config.under_prediction
    
    def run(self, max_trades: int = None, max_duration: int = None) -> Dict:
        """Run the trading bot"""
        self.is_running = True
        start_time = time.time()
        trades_executed = 0
        
        logger.info("=" * 70)
        logger.info("🤖 STARTING TRADING BOT - MARTINGALE STRATEGY")
        logger.info("=" * 70)
        logger.info(f"Config: {self.config.to_dict()}")
        logger.info("=" * 70)
        
        try:
            while self.is_running:
                if max_trades and trades_executed >= max_trades:
                    logger.info(f"Max trades ({max_trades}) reached")
                    break
                
                if max_duration and (time.time() - start_time) > max_duration:
                    logger.info(f"Max duration ({max_duration}s) reached")
                    break
                
                if self.consecutive_errors > 3:
                    logger.error(f"Too many errors. Stopping.")
                    break
                
                if self.execute_trade_cycle():
                    trades_executed += 1
                    logger.info(f"Trade #{trades_executed} completed\n")
                else:
                    if not self.config.restart_on_error:
                        break
                
                time.sleep(1)
        
        except KeyboardInterrupt:
            logger.info("Bot interrupted by user")
        except Exception as e:
            logger.error(f"Fatal error: {e}", exc_info=True)
        finally:
            self.is_running = False
            duration = time.time() - start_time
            
            logger.info("=" * 70)
            logger.info("🛑 TRADING BOT STOPPED")
            logger.info("=" * 70)
            
            stats = self.strategy.get_statistics()
            stats['duration_seconds'] = round(duration, 2)
            
            logger.info(f"Final Statistics: {stats}")
            self.strategy.export_trades()
            
            return stats


def create_default_bot() -> TradingBot:
    """Create bot with default configuration"""
    config = TradingConfig()
    return TradingBot(config)


def create_custom_bot(
    initial_stake: float = 30.0,
    martingale_multiplier: float = 1.3,
    take_profit: float = 10.0,
    stop_loss: float = 300.0
) -> TradingBot:
    """Create bot with custom configuration"""
    config = TradingConfig(
        initial_stake=initial_stake,
        stake=initial_stake,
        martingale_multiplier=martingale_multiplier,
        take_profit=take_profit,
        stop_loss=stop_loss
    )
    return TradingBot(config)


if __name__ == "__main__":
    bot = create_default_bot()
    stats = bot.run(max_trades=20, max_duration=300)
    
    print("\n" + "=" * 70)
    print("📊 FINAL RESULTS")
    print("=" * 70)
    print(json.dumps(stats, indent=2))
    print("=" * 70)
