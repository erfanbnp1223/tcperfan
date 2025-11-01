# 🔥 ERFAN Advanced Free Fire TCP Bot 🔥

## 🎮 Overview
Powerful Free Fire TCP Bot with advanced features including Admin System, Emote Combos, Stats Tracking, Rate Limiting, and more!

## ✨ New Features Added

### 1. 🛡️ Admin & Security System
- **Admin Management**: Whitelist system for authorized users
- **Blacklist System**: Ban unwanted users automatically
- **Rate Limiting**: Prevent spam and abuse
- **Cooldown System**: 3-second cooldown between commands
- **Auto-ban**: 3 warnings = automatic blacklist

### 2. 🎭 Advanced Emote System
- **Emote Combos**: Pre-configured emote sequences
  - `/combo wave` - Wave emote sequence
  - `/combo dance` - Dance emote sequence
  - `/combo victory` - Victory celebration
  - `/combo funny` - Funny emotes
  - `/combo fire` - Fire emotes
  - And many more!
- **Random Emotes**: `/random` - Send random emote to all
- **Emote Sync**: Send same emote to all players simultaneously
- **Emote Wave**: Send emotes in wave pattern

### 3. 📊 Statistics & Analytics
- **Player Stats**: Track commands used, emotes received, warnings
- **Bot Stats**: Total commands, active users, admin count
- **Command History**: Last 1000 commands logged
- **Usage Tracking**: Monitor bot performance

### 4. 💬 Enhanced Commands

#### Public Commands:
```
/help - Show all commands
/emotes - List all emote combos
/stats - Your personal statistics
/botstats - Bot statistics
/fact - Random Free Fire fact
/combo [name] - Execute emote combo
/random - Random emote to all
@a [uid] [emote_id] - Send emote to player
```

#### Admin Commands:
```
/whitelist [uid] - Add user to whitelist
/blacklist [uid] - Ban user
/unban [uid] - Remove from blacklist
/broadcast [msg] - Send message to all
/kick [uid] - Kick player from squad
```

#### Original Commands (Still Working):
```
/5 - Accept squad invitation
/x/ [code] - Join squad by code
/s - Friend system
a - Exit squad
```

### 5. 🤖 Auto-Response System
Bot automatically responds to common messages:
- "hi", "hello" → Greeting
- "help" → Command suggestion
- "thanks" → You're welcome
- "gg" → Good game response
- "bye" → Goodbye message
- And more!

### 6. 🎨 Enhanced UI
- Beautiful welcome messages
- Color-coded responses
- Emoji support
- Professional formatting
- Clear error messages

## 📁 File Structure

```
Erfan TCP/
├── erfan.py                 # Original bot (backup)
├── erfan_advanced.py        # New advanced bot
├── bot_manager.py           # Admin & stats management
├── advanced_features.py     # Advanced features & commands
├── config.json              # Bot configuration
├── xC4.py                   # Packet encryption/decryption
├── xHeaders.py              # API headers & functions
├── Pb2/                     # Protobuf definitions
└── README.md                # This file
```

## ⚙️ Configuration

Edit `config.json` to customize:

```json
{
  "admins": [4259604271],           // Admin UIDs
  "whitelist": [],                   // Whitelisted users
  "blacklist": [],                   // Banned users
  "bot_settings": {
    "max_requests_per_minute": 10,   // Rate limit
    "cooldown_seconds": 3,            // Command cooldown
    "auto_accept_invites": true,      // Auto-accept squad invites
    "auto_response": true,            // Enable auto-responses
    "log_commands": true              // Log all commands
  },
  "emote_combos": {
    "combo1": [909000001, 909000002, 909000003],
    // Add more combos...
  }
}
```

## 🚀 How to Use

### Installation:
```bash
pip install -r requirements.txt
```

### Run the Bot:
```bash
# Run original bot
python erfan.py

# Run advanced bot (recommended)
python erfan_advanced.py
```

### In-Game Usage:
1. Bot joins your squad automatically
2. Type `/help` to see all commands
3. Use `/combo dance` for emote combo
4. Use `@a [uid] [emote_id]` for single emote
5. Admins can use `/whitelist`, `/blacklist`, etc.

## 🎯 Emote IDs Reference

Common emote IDs:
- 909000001-909000050: Various emotes
- Use `/emotes` command in-game to see available combos

## 🔒 Security Features

1. **Blacklist Protection**: Banned users can't use commands
2. **Rate Limiting**: Max 10 requests per minute per user
3. **Cooldown System**: 3 seconds between commands
4. **Admin-Only Commands**: Sensitive commands restricted
5. **Auto-Ban System**: 3 warnings = automatic ban

## 📈 Statistics Tracking

Bot tracks:
- Total commands executed
- Commands per user
- Emotes sent/received
- Active users count
- Warning system
- Join dates

## 🎨 Customization

### Add New Emote Combo:
Edit `config.json`:
```json
"emote_combos": {
  "mycombo": [909000001, 909000002, 909000003]
}
```

### Add New Admin:
Edit `config.json`:
```json
"admins": [4259604271, YOUR_UID_HERE]
```

### Change Messages:
Edit `config.json` → `custom_messages`

## 🐛 Troubleshooting

**Bot not responding?**
- Check internet connection
- Verify account credentials
- Check if account is banned

**Commands not working?**
- Make sure you're in a squad
- Check if you're blacklisted
- Verify cooldown period passed

**Emotes not sending?**
- Verify emote IDs are correct
- Check if target UID is valid
- Ensure bot has proper permissions

## 📝 Notes

- Bot account must be in squad for emotes to work
- Some commands only work in squad chat
- Admin commands require admin UID in config
- Rate limits prevent spam and abuse
- All commands are logged for security

## 👨‍💻 Developer

**Created by**: ERFAN HACKER
**Instagram**: @ERFAN
**Version**: 2.0 Advanced

## 🔥 Features Summary

✅ Admin/Whitelist System
✅ 10+ Emote Combos
✅ Rate Limiting & Spam Protection
✅ Statistics Tracking
✅ Auto-Response System
✅ Broadcast Messages
✅ Player Management
✅ Command Logging
✅ Cooldown System
✅ Enhanced UI/UX
✅ Security Features
✅ Customizable Config

## 📞 Support

For issues or questions:
- Check this README
- Review config.json settings
- Test with `/help` command in-game

---

**Enjoy the most powerful Free Fire TCP Bot! 🎮🔥**
