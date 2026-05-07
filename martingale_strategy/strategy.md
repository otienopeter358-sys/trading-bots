# Martingale Trading Strategy - Implementation Guide

## Overview
The Martingale Strategy is a betting system where the trader doubles (or multiplies) their stake after each loss, aiming to recover losses and gain profit when a win eventually occurs.

## Strategy Rules

### 1. Prediction Logic
```
IF loss_count == 0:
    → Predict OVER (digit >= 6)
ELSE (loss_count >= 1):
    → Predict UNDER (digit <= 8)
```

### 2. Stake Management
```
ON WIN:
    next_stake = initial_stake (reset to $30)
    loss_count = 0
    
ON LOSS:
    next_stake = current_stake × 1.3
    loss_count += 1
```

### 3. Trade Execution
- **Entry**: Open position at current market price
- **Duration**: 60 seconds (1 candle)
- **Exit**: Close at next candle price
- **Result**: Win if prediction is correct

### 4. Risk Management
```
TAKE PROFIT: Close all positions if total profit >= $10
STOP LOSS: Close all positions if total loss <= -$300
```

## Example Trade Sequence

### Scenario 1: Immediate Win
```
Trade 1:
  Loss Count: 0 → Predict OVER
  Stake: $30
  Result: WIN
  Profit: +$30
  Next Loss Count: 0
  Next Stake: $30 (reset)
```

### Scenario 2: Loss and Recovery
```
Trade 1:
  Loss Count: 0 → Predict OVER
  Stake: $30
  Result: LOSS
  Loss: -$30
  Next Loss Count: 1
  Next Stake: $30 × 1.3 = $39

Trade 2:
  Loss Count: 1 → Predict UNDER
  Stake: $39
  Result: WIN
  Profit: +$39
  Total Profit: +$30 + $39 = $69 net
  Next Loss Count: 0
  Next Stake: $30 (reset)
```

### Scenario 3: Loss Streak
```
Trade 1: LOSS → Stake: $30 → Next: $39
Trade 2: LOSS → Stake: $39 → Next: $50.70
Trade 3: LOSS → Stake: $50.70 → Next: $65.91
Trade 4: WIN → Stake: $65.91 → Profit: +$65.91

Total Loss: -$30 - $39 - $50.70 = -$119.70
Win Amount: +$65.91
Net Result: -$53.79 (loss covered by future wins)
```

## Key Metrics

### Win Rate
```
Win Rate = (Wins / Total Trades) × 100
```

### Profit Factor
```
Profit Factor = Total Profit / Total Loss
Example: $300 profit / $100 loss = 3.0 (very profitable)
```

### Drawdown
```
Max Drawdown = Maximum loss during winning phase
Used to assess risk exposure
```

## Advantages ✅

1. **Simple to Implement** - Easy to understand and execute
2. **Mathematically Sound** - Works if you have enough capital
3. **Recovers Losses** - Each win recovers all previous losses + profit
4. **Consistent Results** - Less dependent on prediction accuracy

## Disadvantages ⚠️

1. **Capital Intensive** - Requires large bankroll for loss streaks
2. **Exponential Growth** - Stakes increase exponentially (1.3^n)
3. **Margin Risk** - Leverage requirements increase
4. **Psychological Pressure** - Can lead to poor decision-making
5. **No Guaranteed Win** - Long losing streaks can exceed capital

## Risk Examples

### Losing Streak Analysis
With 1.3x multiplier:
- Loss #1: $30
- Loss #2: $39
- Loss #3: $50.70
- Loss #4: $65.91
- Loss #5: $85.68
- **Total Capital Needed**: $271.29

With 1.5x multiplier (aggressive):
- Loss #1: $50
- Loss #2: $75
- Loss #3: $112.50
- Loss #4: $168.75
- Loss #5: $253.13
- **Total Capital Needed**: $659.38

## Recommended Configuration

### Conservative (Safe)
```json
{
  "initial_stake": 20,
  "martingale_multiplier": 1.2,
  "take_profit": 50,
  "stop_loss": 200
}
```

### Balanced (Default)
```json
{
  "initial_stake": 30,
  "martingale_multiplier": 1.3,
  "take_profit": 10,
  "stop_loss": 300
}
```

### Aggressive (High Risk)
```json
{
  "initial_stake": 50,
  "martingale_multiplier": 1.5,
  "take_profit": 100,
  "stop_loss": 500
}
```

## Testing Before Live Trading

1. **Backtest** with historical data
2. **Demo Test** with simulated trading
3. **Paper Trade** with real prices but no money
4. **Start Small** with minimum stakes
5. **Scale Up** gradually as confidence increases

## References

- Martingale Strategy: https://en.wikipedia.org/wiki/Martingale_(betting_system)
- Risk Management: https://en.wikipedia.org/wiki/Risk_management
- Trading Psychology: https://www.investopedia.com/terms/t/trading-psychology.asp
