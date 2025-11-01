"""
VIP FEATURES - ERFAN BOT
Powerful features for advanced users
"""

import asyncio
import random
from datetime import datetime
from xC4 import Emote_k

class VIPFeatures:
    def __init__(self):
        # Generate all emotes from 909000001 to 909060001
        self.all_emotes = {}
        for i in range(1, 60002):
            emote_id = 909000000 + i
            self.all_emotes[str(i)] = emote_id
        
        # Quick access for first 10
        self.quick_emotes = {
            '1': 909000001,
            '2': 909000002,
            '3': 909000003,
            '4': 909000004,
            '5': 909000005,
            '6': 909000006,
            '7': 909000007,
            '8': 909000008,
            '9': 909000009,
            '10': 909000010,
        }
        
        self.auto_reply_enabled = {}  # {uid: True/False}
        self.auto_reply_messages = {
            'hi': '👋 Hello! I am using ERFAN BOT!',
            'hello': '👋 Hey there! Bot by ERFAN!',
            'hey': '👋 Hi! Type /help for commands',
            'how are you': '😊 I am good! Thanks for asking!',
            'thanks': '😊 You are welcome!',
            'thank you': '😊 My pleasure!',
            'bye': '👋 Goodbye! See you later!',
            'gn': '🌙 Good night! Sweet dreams!',
            'gm': '☀️ Good morning! Have a great day!',
        }
        
        self.emote_history = {}  # {uid: [emote_ids]}
        self.favorite_emotes = {}  # {uid: [emote_ids]}
    
    def get_quick_emote_menu(self, page=1):
        """Get quick emote selection menu with pagination"""
        items_per_page = 10
        start = (page - 1) * items_per_page + 1
        end = min(start + items_per_page - 1, 60001)
        
        menu = f"""[B][C][00FF00]⚡ QUICK EMOTES (Page {page}) ⚡

[FFFF00]Type number to send:
[FFFFFF]"""
        
        for i in range(start, end + 1):
            emote_id = 909000000 + i
            menu += f"{i} - Emote {emote_id}\n"
        
        if end < 60001:
            menu += f"\n[FFFF00]Type: /quick {page + 1} for more..."
        
        menu += "\n[FFFF00]Or: @a [number]\n[00FF00]✅ Bot by ERFAN"
        return menu
    
    def get_quick_emote_id(self, number):
        """Get emote ID from any number (1-60001)"""
        return self.all_emotes.get(str(number), None)
    
    def toggle_auto_reply(self, uid):
        """Toggle auto-reply on/off"""
        current = self.auto_reply_enabled.get(uid, False)
        self.auto_reply_enabled[uid] = not current
        return not current
    
    def get_auto_reply(self, message):
        """Get auto-reply message"""
        msg = message.lower().strip()
        return self.auto_reply_messages.get(msg, None)
    
    def add_to_history(self, uid, emote_id):
        """Add emote to history"""
        if uid not in self.emote_history:
            self.emote_history[uid] = []
        self.emote_history[uid].append(emote_id)
        # Keep only last 10
        if len(self.emote_history[uid]) > 10:
            self.emote_history[uid] = self.emote_history[uid][-10:]
    
    def get_history(self, uid):
        """Get emote history"""
        return self.emote_history.get(uid, [])
    
    def add_favorite(self, uid, emote_id):
        """Add emote to favorites"""
        if uid not in self.favorite_emotes:
            self.favorite_emotes[uid] = []
        if emote_id not in self.favorite_emotes[uid]:
            self.favorite_emotes[uid].append(emote_id)
            return True
        return False
    
    def remove_favorite(self, uid, emote_id):
        """Remove emote from favorites"""
        if uid in self.favorite_emotes and emote_id in self.favorite_emotes[uid]:
            self.favorite_emotes[uid].remove(emote_id)
            return True
        return False
    
    def get_favorites(self, uid):
        """Get favorite emotes"""
        return self.favorite_emotes.get(uid, [])
    
    async def send_quick_emote(self, number, target_uid, key, iv, region, send_packet, whisper_writer, online_writer):
        """Send emote using quick number"""
        emote_id = self.get_quick_emote_id(number)
        if emote_id:
            H = await Emote_k(target_uid, emote_id, key, iv, region)
            await send_packet(whisper_writer, online_writer, "OnLine", H)
            return emote_id
        return None
    
    async def repeat_last_emote(self, uid, target_uid, key, iv, region, send_packet, whisper_writer, online_writer):
        """Repeat last sent emote"""
        history = self.get_history(uid)
        if history:
            last_emote = history[-1]
            H = await Emote_k(target_uid, last_emote, key, iv, region)
            await send_packet(whisper_writer, online_writer, "OnLine", H)
            return last_emote
        return None
    
    def get_emote_stats(self, uid):
        """Get emote usage statistics"""
        history = self.get_history(uid)
        if not history:
            return None
        
        from collections import Counter
        counter = Counter(history)
        most_used = counter.most_common(3)
        
        return {
            'total': len(history),
            'unique': len(set(history)),
            'most_used': most_used
        }

# Global instance
vip_features = VIPFeatures()
