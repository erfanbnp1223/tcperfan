import asyncio
import random
import time
from datetime import datetime
from xC4 import *

class AdvancedFeatures:
    def __init__(self):
        self.emote_sequences = {
            'wave': [909000001, 909000002, 909000003, 909000004],
            'dance': [909000005, 909000006, 909000007, 909000008],
            'victory': [909000009, 909000010, 909000011, 909000012],
            'funny': [909000013, 909000014, 909000015, 909000016],
            'sad': [909000017, 909000018, 909000019, 909000020],
            'angry': [909000021, 909000022, 909000023, 909000024],
            'love': [909000025, 909000026, 909000027, 909000028],
            'cool': [909000029, 909000030, 909000031, 909000032],
            'party': [909000033, 909000034, 909000035, 909000036],
            'fire': [909000037, 909000038, 909000039, 909000040]
        }
        
        self.auto_responses = {
            'hi': '👋 Hello! Welcome to the squad!',
            'hello': '👋 Hey there! Ready to play?',
            'help': '📋 Type /help to see all commands!',
            'thanks': '😊 You\'re welcome! Happy gaming!',
            'bye': '👋 Goodbye! See you next time!',
            'gg': '🎮 Good game! Well played!',
            'noob': '😅 Everyone starts somewhere!',
            'pro': '🔥 You\'re a legend!',
            'lag': '⚠️ Try restarting your game!',
            'hack': '🛡️ Report hackers in-game!'
        }
        
        self.fun_facts = [
            "🎮 Free Fire has over 1 billion downloads!",
            "🏆 The first Free Fire World Series was in 2019!",
            "💎 There are over 50 unique characters in Free Fire!",
            "🔫 AWM is one of the most powerful sniper rifles!",
            "🎯 Headshots deal 200% damage!",
            "🚁 You can call airdrops for special loot!",
            "⚡ Gloo walls can save your life!",
            "🎪 Pet skills can give you advantages!",
            "🌟 DJ Alok is one of the most popular characters!",
            "🔥 Booyah means victory in Free Fire!"
        ]
    
    async def get_help_message(self):
        return """[B][C][00FF00]╔════════════════════════════╗
║   🎮 ERFAN BOT COMMANDS 🎮   ║
╚════════════════════════════╝

[FFFF00]📌 EMOTE COMMANDS:
[FFFFFF]@a [uid] [emote_id] - Send emote to player
/combo [name] - Use emote combo
/emotes - List all emote combos
/random - Random emote to all

[FFFF00]📌 SQUAD COMMANDS:
[FFFFFF]/5 - Accept squad invitation
/x/ [code] - Join squad by code
/s - Friend system
a - Exit squad

[FFFF00]📌 INFO COMMANDS:
[FFFFFF]/help - Show this menu
/stats - Your statistics
/botstats - Bot statistics
/fact - Random Free Fire fact

[FFFF00]📌 ADMIN COMMANDS:
[FFFFFF]/whitelist [uid] - Add to whitelist
/blacklist [uid] - Add to blacklist
/unban [uid] - Remove from blacklist
/broadcast [msg] - Send to all
/kick [uid] - Kick player

[00FF00]💡 TIP: Use combos for epic effects!
[FF0000]⚡ Dev: ERFAN HACKER | Instagram"""
    
    async def get_emote_list(self):
        combos = '\n'.join([f"[FFFF00]/{name}[FFFFFF] - {len(emotes)} emotes" 
                           for name, emotes in self.emote_sequences.items()])
        return f"""[B][C][00FF00]🎭 AVAILABLE EMOTE COMBOS 🎭

{combos}

[00FFFF]Usage: /combo [name]
[90EE90]Example: /combo dance"""
    
    async def execute_emote_combo(self, combo_name, target_uids, key, iv, region, send_packet_func, writer1, writer2):
        if combo_name not in self.emote_sequences:
            return None
        
        emotes = self.emote_sequences[combo_name]
        
        for emote_id in emotes:
            for uid in target_uids:
                if uid:
                    packet = await Emote_k(uid, emote_id, key, iv, region)
                    await send_packet_func(writer1, writer2, "OnLine", packet)
            await asyncio.sleep(0.5)
        
        return f"[B][C][00FF00]✨ Combo '{combo_name}' executed! {len(emotes)} emotes sent!"
    
    async def random_emote_all(self, target_uids, key, iv, region, send_packet_func, writer1, writer2):
        all_emotes = [909000001 + i for i in range(50)]
        selected_emote = random.choice(all_emotes)
        
        for uid in target_uids:
            if uid:
                packet = await Emote_k(uid, selected_emote, key, iv, region)
                await send_packet_func(writer1, writer2, "OnLine", packet)
                await asyncio.sleep(0.2)
        
        return f"[B][C][00FF00]🎲 Random emote {selected_emote} sent to all!"
    
    def get_auto_response(self, message):
        msg_lower = message.lower().strip()
        for key, response in self.auto_responses.items():
            if key in msg_lower:
                return f"[B][C][00FFFF]{response}"
        return None
    
    def get_random_fact(self):
        return f"[B][C][FFFF00]💡 DID YOU KNOW?\n[FFFFFF]{random.choice(self.fun_facts)}"
    
    async def broadcast_message(self, message, chat_type, uid, chat_id, key, iv, send_msg_func):
        formatted_msg = f"[B][C][FF0000]📢 BROADCAST:\n[FFFFFF]{message}"
        return await send_msg_func(chat_type, formatted_msg, uid, chat_id, key, iv)
    
    async def get_player_stats_message(self, stats):
        return f"""[B][C][00FF00]📊 YOUR STATISTICS 📊

[FFFF00]Commands Used: [FFFFFF]{stats['commands_used']}
[FFFF00]Emotes Received: [FFFFFF]{stats['emotes_received']}
[FFFF00]Warnings: [FFFFFF]{stats['warnings']}
[FFFF00]Member Since: [FFFFFF]{stats['member_since']}

[00FF00]Keep playing and have fun! 🎮"""
    
    async def get_bot_stats_message(self, stats):
        return f"""[B][C][00FF00]🤖 BOT STATISTICS 🤖

[FFFF00]Total Commands: [FFFFFF]{stats['total_commands']}
[FFFF00]Total Users: [FFFFFF]{stats['total_users']}
[FFFF00]Active Users: [FFFFFF]{stats['active_users']}
[FFFF00]Admins: [FFFFFF]{stats['admins']}
[FFFF00]Whitelisted: [FFFFFF]{stats['whitelisted']}
[FFFF00]Blacklisted: [FFFFFF]{stats['blacklisted']}

[00FF00]Bot running smoothly! ⚡"""
    
    async def spam_emotes(self, target_uid, emote_id, count, key, iv, region, send_packet_func, writer1, writer2):
        for i in range(count):
            packet = await Emote_k(target_uid, emote_id, key, iv, region)
            await send_packet_func(writer1, writer2, "OnLine", packet)
            await asyncio.sleep(0.3)
        return f"[B][C][00FF00]🔥 Sent {count} emotes!"
    
    async def emote_wave(self, target_uids, key, iv, region, send_packet_func, writer1, writer2):
        """Send emotes in a wave pattern"""
        emote_ids = [909000001, 909000002, 909000003, 909000004, 909000005]
        
        for emote_id in emote_ids:
            for uid in target_uids:
                if uid:
                    packet = await Emote_k(uid, emote_id, key, iv, region)
                    await send_packet_func(writer1, writer2, "OnLine", packet)
            await asyncio.sleep(0.4)
        
        return "[B][C][00FF00]🌊 Emote wave completed!"
    
    async def emote_sync(self, target_uids, emote_id, key, iv, region, send_packet_func, writer1, writer2):
        """Send same emote to all players simultaneously"""
        tasks = []
        for uid in target_uids:
            if uid:
                packet = await Emote_k(uid, emote_id, key, iv, region)
                tasks.append(send_packet_func(writer1, writer2, "OnLine", packet))
        
        await asyncio.gather(*tasks)
        return f"[B][C][00FF00]⚡ Synced emote {emote_id} to all players!"
    
    def get_welcome_message(self, player_name=None):
        greetings = [
            f"🎮 Welcome {player_name or 'Player'}! Ready to dominate?",
            f"🔥 {player_name or 'Player'} joined! Let's get that Booyah!",
            f"⚡ {player_name or 'Player'} is here! Time to win!",
            f"🏆 Welcome {player_name or 'Player'}! Let's make it epic!",
            f"💎 {player_name or 'Player'} entered! Squad up!"
        ]
        return f"[B][C][00FF00]{random.choice(greetings)}"
    
    def get_cooldown_message(self, seconds_left):
        return f"[B][C][FFA500]⏰ Cooldown active! Wait {seconds_left:.1f}s"
    
    def get_unauthorized_message(self):
        return "[B][C][FF0000]❌ Unauthorized! Admin only command!"
    
    def get_blacklisted_message(self):
        return "[B][C][FF0000]🚫 You are blacklisted! Contact admin."
    
    def get_rate_limit_message(self):
        return "[B][C][FF4500]⚠️ Too many requests! Slow down!"

# Global instance
advanced_features = AdvancedFeatures()
