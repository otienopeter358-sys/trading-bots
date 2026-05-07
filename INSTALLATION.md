# 🔧 Installation & Setup Guide

## Files Overview

```
trading-bots/
├── martingale_bot.xml          ← XML for Deriv Bot Builder (READY TO USE)
├── trading_bot.py              ← Python executable bot
├── run_bot.py                  ← Interactive launcher
├── config.json                 ← Configuration file
├── requirements.txt            ← Python dependencies (none!)
├── README.md                   ← Full documentation
├── DERIV_BOT_SETUP.md         ← Deriv-specific setup
├── INSTALLATION.md            ← This file
└── martingale_strategy/
    └── strategy.md            ← Strategy explanation
```

## Quick Links

| Platform | File | Download |
|----------|------|----------|
| **Deriv** | `martingale_bot.xml` | [Download XML](https://raw.githubusercontent.com/otienopeter358-sys/trading-bots/main/bot_converted.xml) |
| **Python** | `trading_bot.py` | [Download Python](https://raw.githubusercontent.com/otienopeter358-sys/trading-bots/main/trading_bot.py) |
| **Config** | `config.json` | [Download Config](https://raw.githubusercontent.com/otienopeter358-sys/trading-bots/main/config.json) |
| **All Files** | ZIP Archive | [Download ZIP](https://github.com/otienopeter358-sys/trading-bots/archive/refs/heads/main.zip) |

## Installation Steps

### Option A: Deriv Bot (Easiest)

```bash
# 1. Download XML file
wget https://raw.githubusercontent.com/otienopeter358-sys/trading-bots/main/bot_converted.xml

# 2. Import into Deriv:
#    - Go to https://app.deriv.com/bot
#    - Click Import
#    - Select martingale_bot.xml
#    - Configure and Run
```

### Option B: Python Bot (Local)

```bash
# 1. Check Python version
python3 --version  # Should be 3.7+

# 2. Download bot
wget https://raw.githubusercontent.com/otienopeter358-sys/trading-bots/main/trading_bot.py

# 3. Run bot
python3 trading_bot.py
```

### Option C: Clone Repository

```bash
# 1. Clone
git clone https://github.com/otienopeter358-sys/trading-bots.git
cd trading-bots

# 2. Run
python3 trading_bot.py

# OR use launcher
python3 run_bot.py
```

## Verification

After installation, verify everything works:

```bash
# Test Python bot
python3 trading_bot.py

# Expected output:
# ========================================
# 🤖 STARTING TRADING BOT - MARTINGALE STRATEGY
# ========================================
# ...
# Trade #1 completed
# ...
```

## Files Explained

### Core Files

**`martingale_bot.xml`** (Deriv Bot)
- XML format for Deriv Bot Builder
- Ready to import and run
- No installation needed
- Size: ~58 KB

**`trading_bot.py`** (Python Bot)
- Full Python implementation
- Runs locally on your computer
- Requires Python 3.7+
- No external dependencies
- Size: ~20 KB

**`run_bot.py`** (Launcher)
- Interactive configuration selector
- Easy preset selection
- Size: ~3 KB

**`config.json`** (Settings)
- Bot configuration parameters
- Edit to customize strategy
- Size: ~0.5 KB

### Documentation

**`README.md`** - Main documentation (7 KB)
**`DERIV_BOT_SETUP.md`** - Deriv-specific guide (8 KB)
**`INSTALLATION.md`** - This file (3 KB)
**`martingale_strategy/strategy.md`** - Strategy deep-dive (6 KB)

## System Requirements

### For Deriv Bot
- Web browser (Chrome, Firefox, Safari, Edge)
- Internet connection
- Deriv account
- No installation needed

### For Python Bot
- Python 3.7 or higher
- Terminal/Command Prompt
- Internet connection (optional)
- ~50 MB disk space

## Troubleshooting

### Python Not Found
```bash
# Install Python from python.org
# Or use:
brew install python3        # macOS
sudo apt-get install python3  # Linux
choco install python       # Windows
```

### Permission Denied
```bash
chmod +x trading_bot.py
python3 trading_bot.py
```

### Module Not Found
```bash
# All dependencies are built-in, but if you get errors:
python3 -m pip install --upgrade pip
```

## Configuration

Edit `config.json` to customize:

```json
{
  "initial_stake": 30.0,
  "martingale_multiplier": 1.3,
  "take_profit": 10.0,
  "stop_loss": 300.0,
  "max_trades": 20,
  "max_duration": 300
}
```

## Running the Bot

### Using Python
```bash
python3 trading_bot.py
```

### Using Launcher
```bash
python3 run_bot.py
# Select preset (1=Default, 2=Conservative, 3=Aggressive)
```

### Using Deriv
1. Import `martingale_bot.xml` into Bot Builder
2. Configure settings
3. Click "Run"
4. Monitor dashboard

## Next Steps

1. **Read Documentation**: Check README.md
2. **Review Strategy**: See martingale_strategy/strategy.md
3. **Test Locally**: Run trading_bot.py in demo mode
4. **Try Deriv**: Import XML and test with demo account
5. **Go Live**: Start with small stakes on real account

---

For detailed information, see the full documentation in the repository.
