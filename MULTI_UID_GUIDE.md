# 🔥 MULTIPLE UID SYSTEM - Complete Guide

## ⚡ NEW FEATURES

### 1. Save Multiple UIDs at Once 💾
Save unlimited friends in one command!

```
/save 4259604271 111111111 222222222 333333333
```

**Output**:
```
✅ 4 UIDs Saved!
default: 4259604271
uid2: 111111111
uid3: 222222222
uid4: 333333333
Use: @a [number] or /all [number]
```

---

### 2. Send to Multiple UIDs 🎯
Send emote to multiple friends at once!

```
@a 4259604271 111111111 222222222 1
```

**What happens**:
- Emote 909000001 sent to 4259604271 ✅
- Emote 909000001 sent to 111111111 ✅
- Emote 909000001 sent to 222222222 ✅

---

### 3. Send to ALL Saved UIDs 🔥
Send to everyone you saved!

```
/all 1
```

**What happens**:
- Sends emote to ALL saved UIDs
- Shows count: "Sent to 5 UIDs"

---

### 4. View All Saved UIDs 📋
Check who you saved!

```
/saves
```

**Output**:
```
💾 Your Saved UIDs (5):
default: 4259604271
uid2: 111111111
uid3: 222222222
uid4: 333333333
uid5: 444444444
Use: @a [number] or /all [number]
```

---

## 🎮 Complete Usage Examples

### Example 1: Save Squad Members
```
/save 4259604271 111111111 222222222 333333333 444444444
✅ 5 UIDs Saved!

/saves
💾 Your Saved UIDs (5):
default: 4259604271
uid2: 111111111
uid3: 222222222
uid4: 333333333
uid5: 444444444
```

---

### Example 2: Send to Multiple Friends
```
@a 4259604271 111111111 222222222 1

🔥 Sending Emote!
To: 3 UIDs
Emote: 909000001

✅ Emote 909000001 sent to UID 4259604271
✅ Emote 909000001 sent to UID 111111111
✅ Emote 909000001 sent to UID 222222222
✅ Emote 909000001 sent to 3/3 UIDs
```

---

### Example 3: Send to ALL Saved
```
/save 4259604271 111111111 222222222
/all 5

🔥 Sent to ALL!
Emote: 909000005
Sent to 3 UIDs

✅ Emote 909000005 sent to default (4259604271)
✅ Emote 909000005 sent to uid2 (111111111)
✅ Emote 909000005 sent to uid3 (222222222)
```

---

### Example 4: Quick Number with Multiple UIDs
```
@a 4259604271 111111111 222222222 266

🔥 Sending Emote!
To: 3 UIDs
Emote: 909000266
```

---

## 📊 All Commands

### 💾 Save Multiple UIDs
```
/save [uid1] [uid2] [uid3] [uid4] [uid5]...
```

**Examples**:
```
/save 123456789
/save 123456789 987654321
/save 111111111 222222222 333333333 444444444 555555555
```

---

### 📌 Send to Multiple UIDs
```
@a [uid1] [uid2] [uid3] [emote]
```

**Examples**:
```
@a 123456789 1                          # 1 UID
@a 123456789 987654321 1                # 2 UIDs
@a 111111111 222222222 333333333 266    # 3 UIDs
```

---

### 🔥 Send to ALL Saved
```
/all [number]
```

**Examples**:
```
/all 1          # Wave to all
/all 5          # Angry to all
/all 266        # Special emote to all
```

---

### 📋 View Saved UIDs
```
/saves
```

Shows all saved UIDs with count.

---

## 🚀 Workflows

### Workflow 1: Squad Setup
```
# Save entire squad
/save 4259604271 111111111 222222222 333333333

# Check saved
/saves

# Send to all
/all 1
```

---

### Workflow 2: Send to Specific Friends
```
# Send to 2 friends
@a 111111111 222222222 5

# Send to 3 friends
@a 111111111 222222222 333333333 266
```

---

### Workflow 3: Mass Emote
```
# Save 10 friends
/save 111111111 222222222 333333333 444444444 555555555 666666666 777777777 888888888 999999999 101010101

# Send to all at once
/all 1
```

---

## 💡 Pro Tips

### Tip 1: Save Squad Quickly
```
/save 4259604271 111111111 222222222 333333333 444444444
```
One command = 5 UIDs saved! ⚡

### Tip 2: Send to All
```
/all 1
```
Fastest way to send to everyone!

### Tip 3: Selective Sending
```
@a 111111111 222222222 1        # Only 2 friends
@a 333333333 444444444 5        # Different 2 friends
```

### Tip 4: Check Saved
```
/saves
```
Always check who you saved!

---

## 🎯 Use Cases

### Case 1: Squad Leader
```
/save [member1] [member2] [member3] [member4]
/all 1                  # Wave to squad
/all 5                  # Angry at enemies
```

### Case 2: Friend Group
```
/save [friend1] [friend2] [friend3] [friend4] [friend5]
/all 266                # Special emote to all
```

### Case 3: Selective Emotes
```
@a [friend1] [friend2] 1        # Wave to 2
@a [friend3] [friend4] 5        # Angry to other 2
```

---

## 📈 Comparison

### Old Way (Slow):
```
@a 4259604271 1         ❌ One by one
@a 111111111 1          ❌ Repeat command
@a 222222222 1          ❌ Boring
@a 333333333 1          ❌ Time consuming
```

### New Way (Fast):
```
/save 4259604271 111111111 222222222 333333333
/all 1                  ✅ ONE COMMAND!
```

Or:
```
@a 4259604271 111111111 222222222 333333333 1
✅ ONE COMMAND!
```

---

## 🔥 Terminal Output

```
💾 UID 4259604271 saved as 'default' for user 123456789
💾 UID 111111111 saved as 'uid2' for user 123456789
💾 UID 222222222 saved as 'uid3' for user 123456789
🎯 Using 3 UIDs, Emote: 909000001
✅ Emote 909000001 sent to UID 4259604271
✅ Emote 909000001 sent to UID 111111111
✅ Emote 909000001 sent to UID 222222222
✅ Emote 909000001 sent to 3/3 UIDs
```

---

## ⚡ Quick Reference

| Command | Description | Example |
|---------|-------------|---------|
| `/save [uid1] [uid2]...` | Save multiple | `/save 111 222 333` |
| `/saves` | Show all saved | `/saves` |
| `@a [uid1] [uid2] [emote]` | Send to multiple | `@a 111 222 1` |
| `/all [number]` | Send to ALL saved | `/all 1` |

---

## 🎮 Complete Example

```bash
# Step 1: Save squad
/save 4259604271 111111111 222222222 333333333 444444444
✅ 5 UIDs Saved!

# Step 2: Check saved
/saves
💾 Your Saved UIDs (5):
default: 4259604271
uid2: 111111111
uid3: 222222222
uid4: 333333333
uid5: 444444444

# Step 3: Send to all
/all 1
🔥 Sent to ALL!
Emote: 909000001
Sent to 5 UIDs

# Step 4: Send to specific 2
@a 111111111 222222222 5
🔥 Sending Emote!
To: 2 UIDs
Emote: 909000005

# Step 5: Quick emote to 3
@a 222222222 333333333 444444444 266
🔥 Sending Emote!
To: 3 UIDs
Emote: 909000266
```

---

## 🔥 Power Features

✅ **Save Unlimited UIDs** - No limit!
✅ **One Command Save** - Multiple UIDs at once
✅ **Multiple UID Emote** - @a with multiple UIDs
✅ **Send to ALL** - /all command
✅ **Auto-naming** - default, uid2, uid3...
✅ **Error Handling** - Skips invalid UIDs
✅ **Count Display** - Shows how many sent
✅ **Terminal Logs** - Track everything

---

**ERFAN MULTI-UID BOT - Send to Everyone at Once!** 🔥

**Bot by: ERFAN** ⚡
