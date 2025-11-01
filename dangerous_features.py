import asyncio
import random
import time
from xC4 import *

class DangerousFeatures:
    """
    ⚠️ DANGEROUS FEATURES - USE WITH CAUTION ⚠️
    Advanced bot capabilities for power users
    """
    
    def __init__(self):
        self.spam_active = False
        self.auto_kick_enabled = False
        self.emote_rain_active = False
        self.tracked_players = {}
        
    async def emote_rain(self, target_uids, duration, key, iv, region, send_packet_func, writer1, writer2):
        """
        🌧️ EMOTE RAIN - Spam emotes continuously
        Sends random emotes rapidly to all targets
        """
        self.emote_rain_active = True
        start_time = time.time()
        emote_count = 0
        
        while self.emote_rain_active and (time.time() - start_time) < duration:
            emote_id = random.randint(909000001, 909000050)
            for uid in target_uids:
                if uid:
                    packet = await Emote_k(uid, emote_id, key, iv, region)
                    await send_packet_func(writer1, writer2, "OnLine", packet)
                    emote_count += 1
            await asyncio.sleep(0.2)
        
        self.emote_rain_active = False
        return f"[B][C][FF0000]🌧️ EMOTE RAIN COMPLETE!\n[FFFFFF]Sent {emote_count} emotes in {duration}s!"
    
    async def stop_emote_rain(self):
        """Stop emote rain"""
        self.emote_rain_active = False
        return "[B][C][00FF00]✅ Emote rain stopped!"
    
    async def emote_nuke(self, target_uids, key, iv, region, send_packet_func, writer1, writer2):
        """
        💣 EMOTE NUKE - Send all emotes at once
        Massive emote spam attack
        """
        emote_ids = list(range(909000001, 909000051))
        tasks = []
        
        for emote_id in emote_ids:
            for uid in target_uids:
                if uid:
                    packet = await Emote_k(uid, emote_id, key, iv, region)
                    tasks.append(send_packet_func(writer1, writer2, "OnLine", packet))
        
        await asyncio.gather(*tasks)
        return f"[B][C][FF0000]💣 NUKE LAUNCHED!\n[FFFFFF]Sent {len(emote_ids) * len(target_uids)} emotes!"
    
    async def emote_wave_attack(self, target_uids, waves, key, iv, region, send_packet_func, writer1, writer2):
        """
        🌊 WAVE ATTACK - Multiple waves of emotes
        """
        total_sent = 0
        for wave_num in range(waves):
            emote_id = random.randint(909000001, 909000050)
            for uid in target_uids:
                if uid:
                    packet = await Emote_k(uid, emote_id, key, iv, region)
                    await send_packet_func(writer1, writer2, "OnLine", packet)
                    total_sent += 1
            await asyncio.sleep(0.5)
        
        return f"[B][C][00FF00]🌊 Wave Attack Complete!\n[FFFFFF]{waves} waves, {total_sent} emotes sent!"
    
    async def emote_spiral(self, target_uids, key, iv, region, send_packet_func, writer1, writer2):
        """
        🌀 SPIRAL PATTERN - Emotes in spiral pattern
        """
        emote_sequence = [909000001, 909000005, 909000010, 909000015, 909000020, 
                         909000025, 909000030, 909000035, 909000040, 909000045]
        
        for i, emote_id in enumerate(emote_sequence):
            for uid in target_uids:
                if uid:
                    packet = await Emote_k(uid, emote_id, key, iv, region)
                    await send_packet_func(writer1, writer2, "OnLine", packet)
            await asyncio.sleep(0.3)
        
        return "[B][C][9400D3]🌀 Spiral pattern executed!"
    
    async def emote_sync_all(self, target_uids, emote_id, count, key, iv, region, send_packet_func, writer1, writer2):
        """
        ⚡ SYNC ALL - Everyone gets same emote simultaneously
        """
        for _ in range(count):
            tasks = []
            for uid in target_uids:
                if uid:
                    packet = await Emote_k(uid, emote_id, key, iv, region)
                    tasks.append(send_packet_func(writer1, writer2, "OnLine", packet))
            await asyncio.gather(*tasks)
            await asyncio.sleep(0.5)
        
        return f"[B][C][FFFF00]⚡ SYNC COMPLETE!\n[FFFFFF]{count} synchronized emotes to {len(target_uids)} players!"
    
    async def emote_chain_reaction(self, target_uids, key, iv, region, send_packet_func, writer1, writer2):
        """
        🔗 CHAIN REACTION - Sequential emote cascade
        """
        emote_ids = [909000001, 909000010, 909000020, 909000030, 909000040]
        
        for uid in target_uids:
            if uid:
                for emote_id in emote_ids:
                    packet = await Emote_k(uid, emote_id, key, iv, region)
                    await send_packet_func(writer1, writer2, "OnLine", packet)
                    await asyncio.sleep(0.2)
        
        return "[B][C][FFA500]🔗 Chain reaction completed!"
    
    async def random_chaos(self, target_uids, duration, key, iv, region, send_packet_func, writer1, writer2):
        """
        🎲 RANDOM CHAOS - Completely random emote spam
        """
        start_time = time.time()
        emote_count = 0
        
        while (time.time() - start_time) < duration:
            emote_id = random.randint(909000001, 909000050)
            target = random.choice(target_uids) if target_uids else None
            if target:
                packet = await Emote_k(target, emote_id, key, iv, region)
                await send_packet_func(writer1, writer2, "OnLine", packet)
                emote_count += 1
            await asyncio.sleep(random.uniform(0.1, 0.5))
        
        return f"[B][C][FF00FF]🎲 CHAOS MODE!\n[FFFFFF]{emote_count} random emotes in {duration}s!"
    
    async def emote_matrix(self, target_uids, key, iv, region, send_packet_func, writer1, writer2):
        """
        🟢 MATRIX EFFECT - Green emote cascade
        """
        matrix_emotes = [909000001, 909000002, 909000003, 909000004, 909000005]
        
        for _ in range(10):
            emote_id = random.choice(matrix_emotes)
            for uid in target_uids:
                if uid:
                    packet = await Emote_k(uid, emote_id, key, iv, region)
                    await send_packet_func(writer1, writer2, "OnLine", packet)
            await asyncio.sleep(0.15)
        
        return "[B][C][00FF00]🟢 Matrix effect complete!"
    
    async def emote_tsunami(self, target_uids, key, iv, region, send_packet_func, writer1, writer2):
        """
        🌊 TSUNAMI - Massive wave of emotes
        """
        emote_ids = list(range(909000001, 909000031))
        
        for emote_id in emote_ids:
            tasks = []
            for uid in target_uids:
                if uid:
                    packet = await Emote_k(uid, emote_id, key, iv, region)
                    tasks.append(send_packet_func(writer1, writer2, "OnLine", packet))
            await asyncio.gather(*tasks)
            await asyncio.sleep(0.1)
        
        return f"[B][C][00BFFF]🌊 TSUNAMI!\n[FFFFFF]{len(emote_ids)} emotes per player!"
    
    async def player_tracker(self, uid):
        """
        👁️ PLAYER TRACKER - Track player activity
        """
        if uid not in self.tracked_players:
            self.tracked_players[uid] = {
                'first_seen': time.time(),
                'last_seen': time.time(),
                'message_count': 0,
                'emote_count': 0,
                'commands_used': []
            }
        
        self.tracked_players[uid]['last_seen'] = time.time()
        return self.tracked_players[uid]
    
    async def get_tracked_info(self, uid):
        """Get tracking info for player"""
        if uid in self.tracked_players:
            info = self.tracked_players[uid]
            duration = time.time() - info['first_seen']
            return f"""[B][C][00FF00]👁️ PLAYER TRACKING

[FFFF00]UID: [FFFFFF]{uid}
[FFFF00]First Seen: [FFFFFF]{int(duration)}s ago
[FFFF00]Messages: [FFFFFF]{info['message_count']}
[FFFF00]Emotes: [FFFFFF]{info['emote_count']}
[FFFF00]Commands: [FFFFFF]{len(info['commands_used'])}"""
        return "[B][C][FF0000]❌ Player not tracked!"
    
    async def auto_response_attack(self, message, chat_type, uid, chat_id, key, iv, send_msg_func):
        """
        🤖 AUTO RESPONSE ATTACK - Rapid auto-responses
        """
        responses = [
            "[B][C][FF0000]🔥 DETECTED!",
            "[B][C][FFFF00]⚡ PROCESSING...",
            "[B][C][00FF00]✅ CONFIRMED!",
            "[B][C][FF00FF]💎 LEGENDARY!",
            "[B][C][00FFFF]🌟 AMAZING!"
        ]
        
        for response in responses:
            packet = await send_msg_func(chat_type, response, uid, chat_id, key, iv)
            await asyncio.sleep(0.3)
        
        return True
    
    async def emote_fortress(self, target_uid, key, iv, region, send_packet_func, writer1, writer2):
        """
        🏰 FORTRESS - Surround player with emotes
        """
        fortress_emotes = [909000001, 909000005, 909000010, 909000015, 
                          909000020, 909000025, 909000030, 909000035]
        
        for emote_id in fortress_emotes:
            packet = await Emote_k(target_uid, emote_id, key, iv, region)
            await send_packet_func(writer1, writer2, "OnLine", packet)
            await asyncio.sleep(0.2)
        
        return "[B][C][FFD700]🏰 Fortress deployed!"
    
    async def emote_heartbeat(self, target_uids, beats, key, iv, region, send_packet_func, writer1, writer2):
        """
        💓 HEARTBEAT - Rhythmic emote pattern
        """
        heart_emotes = [909000025, 909000026]
        
        for _ in range(beats):
            for emote_id in heart_emotes:
                for uid in target_uids:
                    if uid:
                        packet = await Emote_k(uid, emote_id, key, iv, region)
                        await send_packet_func(writer1, writer2, "OnLine", packet)
                await asyncio.sleep(0.3)
            await asyncio.sleep(0.5)
        
        return f"[B][C][FF1493]💓 Heartbeat: {beats} beats!"
    
    async def emote_explosion(self, center_uid, target_uids, key, iv, region, send_packet_func, writer1, writer2):
        """
        💥 EXPLOSION - Emotes explode from center
        """
        # Center explosion
        for i in range(5):
            emote_id = 909000001 + (i * 5)
            packet = await Emote_k(center_uid, emote_id, key, iv, region)
            await send_packet_func(writer1, writer2, "OnLine", packet)
            await asyncio.sleep(0.1)
        
        # Spread to others
        for uid in target_uids:
            if uid != center_uid and uid:
                emote_id = random.randint(909000001, 909000050)
                packet = await Emote_k(uid, emote_id, key, iv, region)
                await send_packet_func(writer1, writer2, "OnLine", packet)
        
        return "[B][C][FF4500]💥 EXPLOSION!"
    
    def get_dangerous_commands_help(self):
        """Get help for dangerous commands"""
        return """[B][C][FF0000]⚠️ DANGEROUS COMMANDS ⚠️

[FFFF00]🌧️ EMOTE ATTACKS:
[FFFFFF]/rain [duration] - Emote rain
/nuke - Massive emote spam
/tsunami - Wave of all emotes
/chaos [duration] - Random chaos

[FFFF00]🎯 PATTERNS:
[FFFFFF]/spiral - Spiral pattern
/wave [count] - Wave attacks
/matrix - Matrix effect
/explosion - Emote explosion

[FFFF00]⚡ SYNC ATTACKS:
[FFFFFF]/sync [emote] [count] - Sync all
/chain - Chain reaction
/fortress [uid] - Fortress around player
/heartbeat [beats] - Heartbeat pattern

[FFFF00]👁️ TRACKING:
[FFFFFF]/track [uid] - Track player
/trackinfo [uid] - Get tracking info

[FF0000]⚠️ USE RESPONSIBLY!"""

# Global instance
dangerous_features = DangerousFeatures()
