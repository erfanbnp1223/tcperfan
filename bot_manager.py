import json
import time
from datetime import datetime, timedelta
from collections import defaultdict
import asyncio

class BotManager:
    def __init__(self):
        self.config = self.load_config()
        self.user_stats = defaultdict(lambda: {
            'commands_used': 0,
            'last_command_time': 0,
            'emotes_received': 0,
            'warnings': 0,
            'first_seen': time.time()
        })
        self.command_history = []
        self.rate_limiter = defaultdict(list)
        
    def load_config(self):
        try:
            with open('config.json', 'r') as f:
                return json.load(f)
        except:
            return {
                'admins': [],
                'whitelist': [],
                'blacklist': [],
                'bot_settings': {
                    'max_requests_per_minute': 10,
                    'cooldown_seconds': 3,
                    'auto_accept_invites': True,
                    'auto_response': True,
                    'log_commands': True
                },
                'emote_combos': {},
                'custom_messages': {}
            }
    
    def save_config(self):
        with open('config.json', 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def is_admin(self, uid):
        return uid in self.config.get('admins', [])
    
    def is_whitelisted(self, uid):
        return uid in self.config.get('whitelist', []) or self.is_admin(uid)
    
    def is_blacklisted(self, uid):
        return uid in self.config.get('blacklist', [])
    
    def add_to_whitelist(self, uid):
        if uid not in self.config['whitelist']:
            self.config['whitelist'].append(uid)
            self.save_config()
            return True
        return False
    
    def add_to_blacklist(self, uid):
        if uid not in self.config['blacklist']:
            self.config['blacklist'].append(uid)
            self.save_config()
            return True
        return False
    
    def remove_from_blacklist(self, uid):
        if uid in self.config['blacklist']:
            self.config['blacklist'].remove(uid)
            self.save_config()
            return True
        return False
    
    def check_rate_limit(self, uid):
        current_time = time.time()
        max_requests = self.config['bot_settings']['max_requests_per_minute']
        
        # Clean old requests
        self.rate_limiter[uid] = [t for t in self.rate_limiter[uid] 
                                   if current_time - t < 60]
        
        if len(self.rate_limiter[uid]) >= max_requests:
            return False
        
        self.rate_limiter[uid].append(current_time)
        return True
    
    def check_cooldown(self, uid):
        current_time = time.time()
        last_time = self.user_stats[uid]['last_command_time']
        cooldown = self.config['bot_settings']['cooldown_seconds']
        
        if current_time - last_time < cooldown:
            return False
        
        self.user_stats[uid]['last_command_time'] = current_time
        return True
    
    def log_command(self, uid, command, success=True):
        self.user_stats[uid]['commands_used'] += 1
        self.command_history.append({
            'uid': uid,
            'command': command,
            'timestamp': time.time(),
            'success': success
        })
        
        # Keep only last 1000 commands
        if len(self.command_history) > 1000:
            self.command_history = self.command_history[-1000:]
    
    def add_warning(self, uid):
        self.user_stats[uid]['warnings'] += 1
        if self.user_stats[uid]['warnings'] >= 3:
            self.add_to_blacklist(uid)
            return True
        return False
    
    def get_user_stats(self, uid):
        stats = self.user_stats[uid]
        return {
            'commands_used': stats['commands_used'],
            'emotes_received': stats['emotes_received'],
            'warnings': stats['warnings'],
            'member_since': datetime.fromtimestamp(stats['first_seen']).strftime('%Y-%m-%d %H:%M')
        }
    
    def get_emote_combo(self, combo_name):
        return self.config.get('emote_combos', {}).get(combo_name, None)
    
    def get_all_combos(self):
        return list(self.config.get('emote_combos', {}).keys())
    
    def get_message(self, msg_type):
        return self.config.get('custom_messages', {}).get(msg_type, '')
    
    def get_total_stats(self):
        total_commands = sum(s['commands_used'] for s in self.user_stats.values())
        total_users = len(self.user_stats)
        active_users = sum(1 for s in self.user_stats.values() 
                          if time.time() - s['last_command_time'] < 3600)
        
        return {
            'total_commands': total_commands,
            'total_users': total_users,
            'active_users': active_users,
            'admins': len(self.config['admins']),
            'whitelisted': len(self.config['whitelist']),
            'blacklisted': len(self.config['blacklist'])
        }

# Global instance
bot_manager = BotManager()
