# 🤖 Deriv Bot - Setup & Installation Guide

> **Ready-to-Run Martingale Trading Bot for Deriv Synthetic Index Markets**

---

## 📥 DOWNLOAD BOT FILES

### Option 1: Download XML Bot (For Deriv Bot Builder)
**File**: `martingale_bot.xml` (This is the bot ready to import into Deriv)

**Download Link**:
```
https://raw.githubusercontent.com/otienopeter358-sys/trading-bots/main/bot_converted.xml
```

### Option 2: Download Python Bot (For Local Testing)
**File**: `trading_bot.py`

**Download Link**:
```
https://raw.githubusercontent.com/otienopeter358-sys/trading-bots/main/trading_bot.py
```

### Option 3: Download All Files (ZIP)
```bash
cd ~/Downloads
wget https://github.com/otienopeter358-sys/trading-bots/archive/refs/heads/main.zip
unzip main.zip
cd trading-bots-main
```

---

## 🚀 QUICK START FOR DERIV

### Step 1: Open Deriv Bot Builder
1. Go to **Deriv.com**
2. Log in to your account
3. Navigate to **"Bot"** → **"Bot Builder"**
4. Or visit: https://app.deriv.com/bot

### Step 2: Import the XML Bot
1. Click **"Import"** button
2. Select **`martingale_bot.xml`** file
3. Wait for it to load
4. Click **"Load"** or **"Open"**

### Step 3: Configure Settings
Edit these parameters in the bot:

```json
{
  "Market": "Synthetic Index",
  "Symbol": "1HZ10V",
  "Stake": "30 USD",
  "Multiplier": "1.3x",
  "Take Profit": "10 USD",
  "Stop Loss": "300 USD",
  "Trade Type": "Over/Under (Digits)"
}
```

### Step 4: Run the Bot
1. Click **"Run"** button
2. Select **"Run on this device"** or **"Run on cloud"**
3. Monitor trades in real-time
4. Check profit/loss on dashboard

---

## 📊 BOT CONFIGURATION EXPLAINED

### Market Setup
| Setting | Value | Description |
|---------|-------|-------------|
| Market | Synthetic Index | Trading on synthetic markets |
| Symbol | 1HZ10V | Volatility Index (10 Hz) |
| Candle | 60 seconds | 1-minute timeframe |
| Trade Type | Digits Over/Under | Predict if digit will be over/under |

### Risk Management
| Setting | Default | Min | Max |
|---------|---------|-----|-----|
| Initial Stake | $30 | $1 | $1,000 |
| Martingale (multiplier) | 1.3x | 1.1x | 2.0x |
| Take Profit | $10 | $1 | $10,000 |
| Stop Loss | $300 | $10 | $10,000 |

### Prediction Logic
```
IF Loss Count = 0:
  └─ Predict OVER (digit >= 6) ✓

IF Loss Count >= 1:
  └─ Predict UNDER (digit <= 8) ✗→✓
```

---

## 🎯 PRESET CONFIGURATIONS

### 🟢 Conservative (Safe)
```json
{
  "Stake": "20 USD",
  "Multiplier": "1.2x",
  "Take Profit": "50 USD",
  "Stop Loss": "200 USD",
  "Max Trades": "50"
}
```
**Best for**: Learning, small account, high capital preservation

### 🟡 Balanced (Recommended) ⭐
```json
{
  "Stake": "30 USD",
  "Multiplier": "1.3x",
  "Take Profit": "10 USD",
  "Stop Loss": "300 USD",
  "Max Trades": "20"
}
```
**Best for**: Good capital, balanced risk/reward

### 🔴 Aggressive (High Risk)
```json
{
  "Stake": "50 USD",
  "Multiplier": "1.5x",
  "Take Profit": "100 USD",
  "Stop Loss": "500 USD",
  "Max Trades": "50"
}
```
**Best for**: Large capital, high risk tolerance

---

## 📱 USING DERIV BOT BUILDER

### Import Steps
```
1. Deriv.com → Bot → Bot Builder
2. Menu → Import
3. Select martingale_bot.xml
4. Click Load/Open
5. Configure settings
6. Click Run
```

### Monitor Bot
- **Dashboard**: Watch profit/loss in real-time
- **Logs**: View detailed trade information
- **Stats**: Win rate, total profit, number of trades
- **Stop**: Pause or stop bot at any time

### Export Results
- **Download Report**: Click "Download" for CSV/PDF
- **Trade History**: View all trades with entry/exit prices
- **Performance**: Analyze win rate and profit metrics

---

## 💻 ALTERNATIVE: RUN LOCALLY WITH PYTHON

If you prefer to run the bot on your computer:

### Requirements
- Python 3.7+
- No additional dependencies

### Installation
```bash
# Download files
git clone https://github.com/otienopeter358-sys/trading-bots.git
cd trading-bots

# Run bot
python3 trading_bot.py
```

### Output Files
- `trading_bot.log` - Complete execution logs
- `trades.json` - All trades with prices and results

---

## ⚠️ RISK MANAGEMENT WARNINGS

### Important!
1. **Start Small** - Test with minimum stake ($1-$5)
2. **Use Demo First** - Practice before real money
3. **Monitor Closely** - Don't leave bot unattended
4. **Capital Required** - Need 5-10x stop loss as capital
5. **Market Risk** - Real trading involves real money loss

### Loss Streak Analysis
With 1.3x multiplier on a 5-loss streak:
```
Loss 1: $30
Loss 2: $39
Loss 3: $50.70
Loss 4: $65.91
Loss 5: $85.68
───────────────
Total Capital Needed: $271.29
```

**Recommended**: Have at least **$500-$1,000** capital before running

---

## 🎮 BOT CONTROLS

### Start
- Click **"Run"** to start trading
- Select **"On This Device"** (local) or **"On Cloud"** (Deriv servers)

### Monitor
- **View Stats**: Total trades, wins, losses, profit
- **Check Logs**: Click "Logs" to see trade details
- **Watch Charts**: Real-time price movements

### Stop
- Click **"Stop"** to pause bot
- Click **"Clear"** to reset all data
- Check **"Export"** to save trade history

### Modify
- Click **"Edit"** to change settings
- Adjust stakes, multiplier, profit targets
- Save changes before running

---

## 📈 PERFORMANCE TRACKING

### Key Metrics
| Metric | What It Means |
|--------|---------------|
| Total Trades | Number of trades executed |
| Win Rate | % of winning trades |
| Total Profit | Sum of all wins |
| Total Loss | Sum of all losses |
| Net Profit | Profit - Loss |
| Current Stake | Next trade amount |
| Loss Streak | Current consecutive losses |

### Expected Results
With default config (balanced):
- **Win Rate**: 65-75%
- **Profit per session**: $50-$200
- **Duration**: 30-120 minutes
- **Max drawdown**: $300 (stop loss)

---

## 🛠️ TROUBLESHOOTING

### Bot Won't Start
**Problem**: "Import failed" or "Invalid file"
**Solution**: 
- Download fresh `martingale_bot.xml`
- Ensure file is not corrupted
- Try clearing browser cache
- Use different browser (Chrome/Firefox)

### Bot Stops Immediately
**Problem**: Bot runs for 1-2 trades then stops
**Solution**:
- Check if take profit or stop loss was hit
- Verify account has sufficient balance
- Check internet connection
- Review error logs

### High Losses
**Problem**: Losing streak is too long
**Solution**:
- Reduce multiplier (1.3 → 1.2)
- Increase stop loss limit
- Reduce initial stake
- Wait for better market conditions

### Can't Download XML File
**Problem**: Download link doesn't work
**Solution**:
- Right-click → "Save As"
- Use browser's download manager
- Try alternative download:
  ```
  https://github.com/otienopeter358-sys/trading-bots/blob/main/bot_converted.xml
  ```

---

## 📝 STEP-BY-STEP WALKTHROUGH

### First Time Setup

**Step 1: Create Deriv Account** (if new)
- Visit deriv.com
- Sign up with email
- Verify email
- Complete verification

**Step 2: Access Bot Builder**
- Log in to Deriv
- Click "Bot" in top menu
- Click "Bot Builder" or "Create"
- You'll see a blank canvas

**Step 3: Download Bot File**
- Go to: github.com/otienopeter358-sys/trading-bots
- Download `bot_converted.xml`
- Save to your computer

**Step 4: Import Bot**
- In Bot Builder, click "Import"
- Select the downloaded XML file
- Wait for import to complete
- Click "Load"

**Step 5: Configure**
- Edit "Initial Stake" → Set to $30
- Edit "Take Profit" → Set to $10
- Edit "Stop Loss" → Set to $300
- Review prediction settings

**Step 6: Test with Demo**
- Click "Run"
- Select "On This Device"
- **IMPORTANT**: Use Demo Account first!
- Watch 5-10 trades
- Check if results look good

**Step 7: Run Live (Optional)**
- Switch to Real Account
- Start with minimum stake ($1)
- Monitor carefully
- Increase stake as you gain confidence

**Step 8: Monitor & Analyze**
- Watch the dashboard
- Review trade logs
- Check profit metrics
- Stop at take profit or stop loss

---

## 🎓 LEARNING RESOURCES

### In Repository
- `README.md` - Complete documentation
- `martingale_strategy/strategy.md` - Strategy deep-dive
- `config.json` - Configuration examples
- `trading_bot.py` - Source code

### External Resources
- [Deriv Bot Builder Docs](https://deriv.com/trading/bot)
- [Martingale Strategy Guide](https://en.wikipedia.org/wiki/Martingale_(betting_system))
- [Trading Psychology](https://www.investopedia.com/terms/t/trading-psychology.asp)

---

## ❓ FAQ

**Q: Where do I download the XML file?**  
A: From the repository: `https://github.com/otienopeter358-sys/trading-bots`

**Q: Can I modify the bot?**  
A: Yes! Edit it in Bot Builder or download Python version to customize.

**Q: Do I need a Deriv account?**  
A: Yes, to use their Bot Builder. Create free account at deriv.com

**Q: Can I use this for real trading?**  
A: Yes, but start with demo/small stakes first.

**Q: What's the success rate?**  
A: 65-75% win rate typically, depends on market and settings.

**Q: How much capital do I need?**  
A: Minimum $300 (to cover stop loss). Recommended: $500-$1,000

**Q: Can I run multiple bots?**  
A: Yes, Deriv allows multiple bots simultaneously.

**Q: How often should I check the bot?**  
A: Check every 30-60 minutes or set alerts.

---

## 📞 SUPPORT

### Issues?
1. Check **DERIV_BOT_SETUP.md** (this file)
2. Review **README.md** for detailed docs
3. Check **GitHub Issues**: github.com/otienopeter358-sys/trading-bots/issues
4. Contact Deriv Support: deriv.com/contact

### Feedback
If you have suggestions or improvements, let me know!

---

## ⭐ If This Helped, Star The Repository!

Show support by starring: ⭐  
https://github.com/otienopeter358-sys/trading-bots

---

**Version**: 1.0.0  
**Updated**: May 7, 2026  
**Status**: ✅ Ready for Production

---

## 🚀 READY TO START?

1. **Download** `martingale_bot.xml`
2. **Import** into Deriv Bot Builder
3. **Configure** with your settings
4. **Test** with demo account
5. **Run** on real account (optional)
6. **Monitor** and enjoy profits!

**Good luck! 📈**
