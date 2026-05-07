#!/usr/bin/env python3
"""
Simple launcher script for the trading bot
"""

from trading_bot import create_default_bot, create_custom_bot
import json
import sys

def main():
    print("\n" + "=" * 70)
    print("🤖 AI TRADING BOT LAUNCHER")
    print("=" * 70)
    
    choice = input("\nSelect bot configuration:\n1. Default (30 stake, 1.3x multiplier)\n2. Conservative (20 stake, 1.2x multiplier)\n3. Aggressive (50 stake, 1.5x multiplier)\n\nEnter choice (1-3): ").strip()
    
    if choice == "1":
        print("Creating bot with DEFAULT configuration...")
        bot = create_default_bot()
    elif choice == "2":
        print("Creating bot with CONSERVATIVE configuration...")
        bot = create_custom_bot(
            initial_stake=20.0,
            martingale_multiplier=1.2,
            take_profit=50.0,
            stop_loss=200.0
        )
    elif choice == "3":
        print("Creating bot with AGGRESSIVE configuration...")
        bot = create_custom_bot(
            initial_stake=50.0,
            martingale_multiplier=1.5,
            take_profit=100.0,
            stop_loss=500.0
        )
    else:
        print("Invalid choice! Using default configuration.")
        bot = create_default_bot()
    
    max_trades = input("\nMax number of trades (default 20): ").strip()
    max_trades = int(max_trades) if max_trades.isdigit() else 20
    
    max_duration = input("Max duration in seconds (default 300): ").strip()
    max_duration = int(max_duration) if max_duration.isdigit() else 300
    
    print(f"\nStarting bot with max_trades={max_trades}, max_duration={max_duration}s")
    
    stats = bot.run(max_trades=max_trades, max_duration=max_duration)
    
    print("\n" + "=" * 70)
    print("📊 FINAL RESULTS")
    print("=" * 70)
    print(json.dumps(stats, indent=2))
    print("=" * 70)
    print("\n✅ Bot execution complete! Check 'trading_bot.log' for full details.")
    print("📈 Trade history saved to 'trades.json'")

if __name__ == "__main__":
    main()
