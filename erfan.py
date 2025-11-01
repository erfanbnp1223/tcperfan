import requests, os, psutil, sys, jwt, pickle, json, binascii, time, urllib3, base64, datetime, re, socket, threading, ssl, pytz, aiohttp
from protobuf_decoder.protobuf_decoder import Parser
from xC4 import *
from xHeaders import *
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from Pb2 import (
    DEcwHisPErMsG_pb2,
    MajoRLoGinrEs_pb2,
    PorTs_pb2,
    MajoRLoGinrEq_pb2,
    sQ_pb2,
    Team_msg_pb2,
)
from cfonts import render, say
from bot_manager import bot_manager
from advanced_features import advanced_features
from dangerous_features import dangerous_features
from unique_features import unique_features
from vip_features import vip_features

# Flask dummy server for Render Web Service (Free)
from flask import Flask
import asyncio


# EMOTES BY ALAMIN X CODEX


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# VariabLes dyli
# ------------------------------------------#

# UID SAVE SYSTEM - MULTIPLE UIDs
saved_uids = {}  # Format: {user_uid: {'default': uid, 'name1': uid1, 'name2': uid2}}

def save_uid(user_uid, target_uid, name='default'):
    """Save UID for quick emote sending"""
    if user_uid not in saved_uids:
        saved_uids[user_uid] = {}
    saved_uids[user_uid][name] = target_uid
    print(f"💾 UID {target_uid} saved as '{name}' for user {user_uid}")
    return True

def unsave_uid(user_uid, name='default'):
    """Remove saved UID"""
    if user_uid in saved_uids and name in saved_uids[user_uid]:
        del saved_uids[user_uid][name]
        print(f"🗑️ Saved UID '{name}' removed for user {user_uid}")
        return True
    return False

def get_saved_uid(user_uid, name='default'):
    """Get saved UID"""
    if user_uid in saved_uids:
        return saved_uids[user_uid].get(name, None)
    return None

def get_all_saved_uids(user_uid):
    """Get all saved UIDs"""
    return saved_uids.get(user_uid, {})

# ------------------------------------------#
online_writer = None
whisper_writer = None
spam_room = False
spammer_uid = None
spam_chat_id = None
spam_uid = None
Spy = False
Chat_a = False
# ------------------------------------------#

Hr = {
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Content-Type": "application/x-www-form-urlencoded",
    "Expect": "100-continue",
    "X-Unity-Version": "2018.4.11f1",
    "X-GA": "v1 1",
    "ReleaseVersion": "OB51",
}


# ---- Random Colores ----
def get_random_color():
    colors = [
        "[FF0000]",
        "[00FF00]",
        "[0000FF]",
        "[FFFF00]",
        "[FF00FF]",
        "[00FFFF]",
        "[FFFFFF]",
        "[FFA500]",
        "[A52A2A]",
        "[800080]",
        "[000000]",
        "[808080]",
        "[C0C0C0]",
        "[FFC0CB]",
        "[FFD700]",
        "[ADD8E6]",
        "[90EE90]",
        "[D2691E]",
        "[DC143C]",
        "[00CED1]",
        "[9400D3]",
        "[F08080]",
        "[20B2AA]",
        "[FF1493]",
        "[7CFC00]",
        "[B22222]",
        "[FF4500]",
        "[DAA520]",
        "[00BFFF]",
        "[00FF7F]",
        "[4682B4]",
        "[6495ED]",
        "[5F9EA0]",
        "[DDA0DD]",
        "[E6E6FA]",
        "[B0C4DE]",
        "[556B2F]",
        "[8FBC8F]",
        "[2E8B57]",
        "[3CB371]",
        "[6B8E23]",
        "[808000]",
        "[B8860B]",
        "[CD5C5C]",
        "[8B0000]",
        "[FF6347]",
        "[FF8C00]",
        "[BDB76B]",
        "[9932CC]",
        "[8A2BE2]",
        "[4B0082]",
        "[6A5ACD]",
        "[7B68EE]",
        "[4169E1]",
        "[1E90FF]",
        "[191970]",
        "[00008B]",
        "[000080]",
        "[008080]",
        "[008B8B]",
        "[B0E0E6]",
        "[AFEEEE]",
        "[E0FFFF]",
        "[F5F5DC]",
        "[FAEBD7]",
    ]
    return random.choice(colors)


async def encrypted_proto(encoded_hex):
    key = b"Yg&tc%DEuh6%Zc^8"
    iv = b"6oyZDr22E3ychjM%"
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload


async def GeNeRaTeAccEss(uid, password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": (await Ua()),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close",
    }
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067",
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=Hr, data=data) as response:
            if response.status != 200:
                return "Failed to get access token"
            data = await response.json()
            open_id = data.get("open_id")
            access_token = data.get("access_token")
            return (open_id, access_token) if open_id and access_token else (None, None)


async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = "1.118.1"
    major_login.system_software = (
        "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    )
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = (
        "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    )
    major_login.reg_avatar = 1
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019118695"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWAUOUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return await encrypted_proto(string)


async def MajorLogin(payload):
    url = "https://loginbp.ggblueshark.com/MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url, data=payload, headers=Hr, ssl=ssl_context
        ) as response:
            if response.status == 200:
                return await response.read()
            return None


async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr["Authorization"] = f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url, data=payload, headers=Hr, ssl=ssl_context
        ) as response:
            if response.status == 200:
                return await response.read()
            return None


async def DecRypTMajoRLoGin(MajoRLoGinResPonsE):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(MajoRLoGinResPonsE)
    return proto


async def DecRypTLoGinDaTa(LoGinDaTa):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(LoGinDaTa)
    return proto


async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto


async def decode_team_packet(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = sQ_pb2.recieved_chat()
    proto.ParseFromString(packet)
    return proto


async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9:
        headers = "0000000"
    elif uid_length == 8:
        headers = "00000000"
    elif uid_length == 10:
        headers = "000000"
    elif uid_length == 7:
        headers = "000000000"
    else:
        print("Unexpected length")
        headers = "0000000"
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"


async def cHTypE(H):
    if not H:
        return "Squid"
    elif H == 1:
        return "CLan"
    elif H == 2:
        return "PrivaTe"


async def SEndMsG(H, message, Uid, chat_id, key, iv):
    TypE = await cHTypE(H)
    if TypE == "Squid":
        msg_packet = await xSEndMsgsQ(message, chat_id, key, iv)
    elif TypE == "CLan":
        msg_packet = await xSEndMsg(message, 1, chat_id, chat_id, key, iv)
    elif TypE == "PrivaTe":
        msg_packet = await xSEndMsg(message, 2, Uid, Uid, key, iv)
    return msg_packet


async def SEndPacKeT(OnLinE, ChaT, TypE, PacKeT):
    if TypE == "ChaT" and ChaT:
        whisper_writer.write(PacKeT)
        await whisper_writer.drain()
    elif TypE == "OnLine":
        online_writer.write(PacKeT)
        await online_writer.drain()
    else:
        return "UnsoPorTed TypE ! >> ErrrroR (:():)"


async def TcPOnLine(ip, port, key, iv, AutHToKen, reconnect_delay=0.5):
    global \
        online_writer, \
        spam_room, \
        whisper_writer, \
        spammer_uid, \
        spam_chat_id, \
        spam_uid, \
        XX, \
        uid, \
        Spy, \
        data2, \
        Chat_a
    while True:
        try:
            reader, writer = await asyncio.open_connection(ip, int(port))
            online_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            online_writer.write(bytes_payload)
            await online_writer.drain()
            while True:
                data2 = await reader.read(9999)
                if not data2:
                    break

                if data2.hex().startswith("0500") and len(data2.hex()) > 1000:
                    try:
                        print(data2.hex()[10:])
                        packet = await DeCode_PackEt(data2.hex()[10:])
                        print(packet)
                        packet = json.loads(packet)
                        OwNer_UiD, CHaT_CoDe, SQuAD_CoDe = await GeTSQDaTa(packet)

                        JoinCHaT = await AutH_Chat(3, OwNer_UiD, CHaT_CoDe, key, iv)
                        await SEndPacKeT(
                            whisper_writer, online_writer, "ChaT", JoinCHaT
                        )

                        message = (
                            f"[B][C]{get_random_color()}\n- WeLComE To Emote Bot ! "
                        )
                        P = await SEndMsG(0, message, OwNer_UiD, OwNer_UiD, key, iv)
                        await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)

                    except:
                        if data2.hex().startswith("0500") and len(data2.hex()) > 1000:
                            try:
                                print(data2.hex()[10:])
                                packet = await DeCode_PackEt(data2.hex()[10:])
                                print(packet)
                                packet = json.loads(packet)
                                OwNer_UiD, CHaT_CoDe, SQuAD_CoDe = await GeTSQDaTa(
                                    packet
                                )

                                JoinCHaT = await AutH_Chat(
                                    3, OwNer_UiD, CHaT_CoDe, key, iv
                                )
                                await SEndPacKeT(
                                    whisper_writer, online_writer, "ChaT", JoinCHaT
                                )

                                message = f"[B][C]{get_random_color()}\n- WeLComE To Emote Bot ! \n\n{get_random_color()}- Commands : @a {xMsGFixinG('player_uid')} {xMsGFixinG('909000001')}\n\n[00FF00]Dev : @{xMsGFixinG('ERFAN')}"
                                P = await SEndMsG(
                                    0, message, OwNer_UiD, OwNer_UiD, key, iv
                                )
                                await SEndPacKeT(
                                    whisper_writer, online_writer, "ChaT", P
                                )
                            except:
                                pass

            online_writer.close()
            await online_writer.wait_closed()
            online_writer = None

        except Exception as e:
            print(f"- ErroR With {ip}:{port} - {e}")
            online_writer = None
        await asyncio.sleep(reconnect_delay)


async def TcPChaT(
    ip,
    port,
    AutHToKen,
    key,
    iv,
    LoGinDaTaUncRypTinG,
    ready_event,
    region,
    reconnect_delay=0.5,
):
    print(region, "TCP CHAT")

    global \
        spam_room, \
        whisper_writer, \
        spammer_uid, \
        spam_chat_id, \
        spam_uid, \
        online_writer, \
        chat_id, \
        XX, \
        uid, \
        Spy, \
        data2, \
        Chat_a
    while True:
        try:
            reader, writer = await asyncio.open_connection(ip, int(port))
            whisper_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            whisper_writer.write(bytes_payload)
            await whisper_writer.drain()
            ready_event.set()
            if LoGinDaTaUncRypTinG.Clan_ID:
                clan_id = LoGinDaTaUncRypTinG.Clan_ID
                clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
                print("\n - TarGeT BoT in CLan ! ")
                print(f" - Clan Uid > {clan_id}")
                print(f" - BoT ConnEcTed WiTh CLan ChaT SuccEssFuLy ! ")
                pK = await AuthClan(clan_id, clan_compiled_data, key, iv)
                if whisper_writer:
                    whisper_writer.write(pK)
                    await whisper_writer.drain()
            while True:
                data = await reader.read(9999)
                if not data:
                    break

                if data.hex().startswith("120000"):
                    msg = await DeCode_PackEt(data.hex()[10:])
                    chatdata = json.loads(msg)
                    try:
                        response = await DecodeWhisperMessage(data.hex()[10:])
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        XX = response.Data.chat_type
                        inPuTMsG = response.Data.msg.lower()
                    except:
                        response = None

                    if response:
                        # SIMPLE HELP COMMAND
                        if inPuTMsG.strip() == "/help":
                            help_text = """[B][C][00FF00]🔥 ERFAN VIP BOT 🔥

[FFFF00]⚡ QUICK EMOTES:
[FFFFFF]Press: 1-9, 0
/quick - Show quick menu

[FFFF00]📌 EMOTE COMMANDS:
[FFFFFF]@a [number] - Quick emote
@a [uid1] [uid2] [emote] - Multiple UIDs
/all [number] - Send to ALL saved
/repeat - Repeat last

[FFFF00]💾 UID SYSTEM:
[FFFFFF]/save [uid1] [uid2] [uid3] - Save multiple
/saves - Show all saved
/unsave [name] - Remove

[FFFF00]⭐ VIP FEATURES:
[FFFFFF]/fav [emote] - Add favorite
/favs - Show favorites
/history - Emote history
/stats - Your stats
/auto - Auto-reply ON/OFF

[FFFF00]🎯 SQUAD:
[FFFFFF]/5 - Accept invite
/x/ [code] - Join
/s - Friends
a - Exit

[00FF00]✅ VIP Bot by ERFAN"""
                            P = await SEndMsG(response.Data.chat_type, help_text, uid, chat_id, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                        
                        # UID SAVE SYSTEM COMMANDS - MULTIPLE UIDs AT ONCE
                        elif inPuTMsG.startswith("/save"):
                            try:
                                parts = inPuTMsG.split()
                                if len(parts) < 2:
                                    message = "[B][C][FF0000]❌ Usage: /save [uid1] [uid2] [uid3]...\n[FFFF00]Example: /save 123456789 987654321\n[FFFFFF]Or: /save 123456789"
                                    P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                                else:
                                    # Save multiple UIDs
                                    saved_count = 0
                                    saved_uids_list = []
                                    for i in range(1, len(parts)):
                                        try:
                                            target_uid = int(parts[i])
                                            name = f'uid{i}' if i > 1 else 'default'
                                            save_uid(uid, target_uid, name)
                                            saved_uids_list.append(f"{name}: {target_uid}")
                                            saved_count += 1
                                        except ValueError:
                                            continue
                                    
                                    if saved_count > 0:
                                        uids_text = "\n[FFFFFF]".join(saved_uids_list)
                                        message = f"[B][C][00FF00]✅ {saved_count} UIDs Saved!\n[FFFFFF]{uids_text}\n[FFFF00]Use: @a [number] or /all [number]"
                                        P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                                    else:
                                        message = "[B][C][FF0000]❌ No valid UIDs!\n[FFFF00]UIDs must be numbers"
                                        P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                            except Exception as e:
                                print(f"❌ Save error: {e}")
                                message = "[B][C][FF0000]❌ Error saving UIDs!"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                        
                        elif inPuTMsG.startswith("/unsave"):
                            parts = inPuTMsG.split()
                            name = parts[1] if len(parts) > 1 else 'default'
                            if unsave_uid(uid, name):
                                message = f"[B][C][00FF00]✅ Saved UID '{name}' removed!"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                            else:
                                message = f"[B][C][FF0000]❌ No saved UID '{name}' found!"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                        
                        elif inPuTMsG.strip() == "/saves":
                            try:
                                all_saved = get_all_saved_uids(uid)
                                if all_saved:
                                    saved_list = "\n[FFFFFF]".join([f"{name}: {uid_val}" for name, uid_val in all_saved.items()])
                                    message = f"[B][C][00FF00]💾 Your Saved UIDs ({len(all_saved)}):\n[FFFFFF]{saved_list}\n[FFFF00]Use: @a [number] or /all [number]"
                                    P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                                    print(f"📋 Showed {len(all_saved)} saved UIDs for user {uid}")
                                else:
                                    message = "[B][C][FF0000]❌ No saved UIDs!\n[FFFF00]Use: /save [uid1] [uid2] [uid3]"
                                    P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                            except Exception as e:
                                print(f"❌ /saves error: {e}")
                                message = "[B][C][FF0000]❌ Error showing saved UIDs!"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                        
                        # SEND TO ALL SAVED UIDs
                        elif inPuTMsG.startswith("/all"):
                            try:
                                parts = inPuTMsG.split()
                                if len(parts) < 2:
                                    message = "[B][C][FF0000]❌ Usage: /all [number]\n[FFFF00]Example: /all 1\n[FFFFFF]Sends to ALL saved UIDs"
                                    P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                                else:
                                    all_saved = get_all_saved_uids(uid)
                                    if all_saved:
                                        number = parts[1]
                                        emote_id = vip_features.get_quick_emote_id(number)
                                        if not emote_id:
                                            emote_id = int(number)
                                        
                                        sent_count = 0
                                        for name, target_uid in all_saved.items():
                                            try:
                                                H = await Emote_k(target_uid, emote_id, key, iv, region)
                                                await SEndPacKeT(whisper_writer, online_writer, "OnLine", H)
                                                await asyncio.sleep(0.1)
                                                sent_count += 1
                                                print(f"✅ Emote {emote_id} sent to {name} ({target_uid})")
                                            except Exception as e:
                                                print(f"❌ Failed to send to {name}: {e}")
                                        
                                        vip_features.add_to_history(uid, emote_id)
                                        message = f"[B][C][00FF00]🔥 Sent to ALL!\n[FFFFFF]Emote: {emote_id}\n[FFFF00]Sent to {sent_count} UIDs"
                                        P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                                    else:
                                        message = "[B][C][FF0000]❌ No saved UIDs!\n[FFFF00]Use: /save [uid1] [uid2] [uid3]"
                                        P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                            except Exception as e:
                                print(f"❌ /all error: {e}")
                                message = "[B][C][FF0000]❌ Error sending to all!"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                        
                        # VIP FEATURES - QUICK EMOTES with pagination
                        elif inPuTMsG.startswith("/quick"):
                            parts = inPuTMsG.split()
                            page = int(parts[1]) if len(parts) > 1 else 1
                            menu = vip_features.get_quick_emote_menu(page)
                            P = await SEndMsG(response.Data.chat_type, menu, uid, chat_id, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                        
                        # Quick number emotes (any number 1-60001)
                        elif inPuTMsG.strip().isdigit():
                            number = inPuTMsG.strip()
                            saved = get_saved_uid(uid)
                            if saved:
                                emote_id = vip_features.get_quick_emote_id(number)
                                if emote_id:
                                    vip_features.add_to_history(uid, emote_id)
                                    H = await Emote_k(saved, emote_id, key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, "OnLine", H)
                                    message = f"[B][C][00FF00]⚡ Quick Emote!\n[FFFFFF]Number: {number}\n[FFFF00]Emote: {emote_id}"
                                    P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                                    print(f"⚡ Quick emote {emote_id} (#{number}) sent to {saved}")
                                else:
                                    message = f"[B][C][FF0000]❌ Invalid number!\n[FFFF00]Use: 1-60001"
                                    P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                            else:
                                message = "[B][C][FF0000]❌ No saved UID!\n[FFFF00]Use: /save [uid] first"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                        
                        # Repeat last emote
                        elif inPuTMsG.strip() == "/repeat":
                            saved = get_saved_uid(uid)
                            if saved:
                                emote_id = await vip_features.repeat_last_emote(
                                    uid, saved, key, iv, region,
                                    SEndPacKeT, whisper_writer, online_writer
                                )
                                if emote_id:
                                    message = f"[B][C][00FF00]🔁 Repeated!\n[FFFFFF]Emote: {emote_id}"
                                    P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                                else:
                                    message = "[B][C][FF0000]❌ No history!"
                                    P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                            else:
                                message = "[B][C][FF0000]❌ No saved UID!"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                        
                        # Add to favorites
                        elif inPuTMsG.startswith("/fav"):
                            try:
                                parts = inPuTMsG.split()
                                if len(parts) < 2:
                                    message = "[B][C][FF0000]❌ Usage: /fav [emote_id]\n[FFFF00]Example: /fav 909000001"
                                    P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                                else:
                                    emote_id = int(parts[1])
                                    if vip_features.add_favorite(uid, emote_id):
                                        message = f"[B][C][00FF00]⭐ Added to favorites!\n[FFFFFF]Emote: {emote_id}"
                                        P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                                    else:
                                        message = "[B][C][FF0000]❌ Already in favorites!"
                                        P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                            except:
                                message = "[B][C][FF0000]❌ Invalid emote ID!"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                        
                        # Show favorites
                        elif inPuTMsG.strip() == "/favs":
                            favs = vip_features.get_favorites(uid)
                            if favs:
                                fav_list = "\n".join([f"⭐ {emote}" for emote in favs])
                                message = f"[B][C][00FF00]⭐ Your Favorites:\n[FFFFFF]{fav_list}\n[FFFF00]Use: @a [emote]"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                            else:
                                message = "[B][C][FF0000]❌ No favorites!\n[FFFF00]Use: /fav [emote_id]"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                        
                        # Show history
                        elif inPuTMsG.strip() == "/history":
                            history = vip_features.get_history(uid)
                            if history:
                                hist_list = ", ".join([str(e) for e in history[-5:]])
                                message = f"[B][C][00FF00]📜 Recent Emotes:\n[FFFFFF]{hist_list}\n[FFFF00]Use /repeat to repeat last"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                            else:
                                message = "[B][C][FF0000]❌ No history!"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                        
                        # Show stats
                        elif inPuTMsG.strip() == "/stats":
                            stats = vip_features.get_emote_stats(uid)
                            if stats:
                                most_used = stats['most_used'][0] if stats['most_used'] else ('None', 0)
                                message = f"[B][C][00FF00]📊 Your Stats:\n[FFFFFF]Total: {stats['total']}\n[FFFFFF]Unique: {stats['unique']}\n[FFFF00]Most Used: {most_used[0]} ({most_used[1]}x)"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                            else:
                                message = "[B][C][FF0000]❌ No stats yet!"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                        
                        # Toggle auto-reply
                        elif inPuTMsG.strip() == "/auto":
                            status = vip_features.toggle_auto_reply(uid)
                            if status:
                                message = "[B][C][00FF00]✅ Auto-reply ON!\n[FFFFFF]Bot will reply to: hi, hello, thanks, etc."
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                            else:
                                message = "[B][C][FF0000]❌ Auto-reply OFF!"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                        
                        # SQUAD INVITATION ACCEPT - /5
                        elif inPuTMsG.strip() == "/5":
                            try:
                                dd = chatdata["5"]["data"]["16"]
                                print("msg in private")
                                message = f"[B][C]{get_random_color()}\n\n✅ AccepT My Invitation FasT\n\n"
                                P = await SEndMsG(
                                    response.Data.chat_type,
                                    message,
                                    uid,
                                    chat_id,
                                    key,
                                    iv,
                                )
                                await SEndPacKeT(
                                    whisper_writer, online_writer, "ChaT", P
                                )
                                PAc = await OpEnSq(key, iv, region)
                                await SEndPacKeT(
                                    whisper_writer, online_writer, "OnLine", PAc
                                )
                                C = await cHSq(5, uid, key, iv, region)
                                await asyncio.sleep(0.5)
                                await SEndPacKeT(
                                    whisper_writer, online_writer, "OnLine", C
                                )
                                V = await SEnd_InV(5, uid, key, iv, region)
                                await asyncio.sleep(0.5)
                                await SEndPacKeT(
                                    whisper_writer, online_writer, "OnLine", V
                                )
                                E = await ExiT(None, key, iv)
                                await asyncio.sleep(3)
                                await SEndPacKeT(
                                    whisper_writer, online_writer, "OnLine", E
                                )
                                print("✅ /5 command executed - Squad invitation accepted")
                            except Exception as e:
                                print(f"❌ /5 command error: {e}")

                        # Join by code
                        elif inPuTMsG.startswith("/x/"):
                            try:
                                CodE = inPuTMsG.split("/x/")[1].strip()
                                print(f"Joining squad with code: {CodE}")
                                
                                dd = chatdata["5"]["data"]["16"]
                                print("msg in private")
                                EM = await GenJoinSquadsPacket(CodE, key, iv)
                                await SEndPacKeT(
                                    whisper_writer, online_writer, "OnLine", EM
                                )
                                print(f"✅ /x/ command executed - Joined squad: {CodE}")
                            except Exception as e:
                                print(f"❌ /x/ command error: {e}")

                        # Exit squad
                        elif inPuTMsG.strip() == "a":
                            try:
                                a = await ExiT(uid, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "OnLine", a)
                                print("✅ 'a' command executed - Exited squad")
                            except Exception as e:
                                print(f"❌ 'a' command error: {e}")

                        # Friend system
                        elif inPuTMsG.strip() == "/s":
                            try:
                                EM = await FS(key, iv)
                                await SEndPacKeT(
                                    whisper_writer, online_writer, "OnLine", EM
                                )
                                print("✅ /s command executed - Friend system opened")
                            except Exception as e:
                                print(f"❌ /s command error: {e}")

                        # EMOTE COMMAND - SMART @a (supports multiple UIDs)
                        elif inPuTMsG.strip().startswith("@a"):
                            try:
                                parts = inPuTMsG.strip().split()
                                print(f"📥 Emote command received: {parts}")
                                
                                target_uids = []
                                emote_id = None
                                
                                # Check if using saved UID or providing new UIDs
                                if len(parts) == 2:
                                    # Format: @a [number] - Use saved UID with quick number
                                    saved = get_saved_uid(uid)
                                    if saved:
                                        target_uids = [saved]
                                        number_or_id = parts[1]
                                        
                                        # Check if it's a quick number (1-60001) or full emote ID
                                        if len(number_or_id) <= 5:
                                            emote_id = vip_features.get_quick_emote_id(number_or_id)
                                            if not emote_id:
                                                emote_id = int(number_or_id)
                                        else:
                                            emote_id = int(number_or_id)
                                        
                                        print(f"🎯 Using saved UID: {target_uids[0]}, Emote: {emote_id}")
                                    else:
                                        message = "[B][C][FF0000]❌ No saved UID!\n[FFFF00]Use: /save [uid] first\n[FFFFFF]Or: @a [uid1] [uid2] [emote]"
                                        P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                                
                                elif len(parts) >= 3:
                                    # Format: @a [uid1] [uid2] [uid3] [emote] - Multiple UIDs
                                    # Last part is emote ID
                                    number_or_id = parts[-1]
                                    
                                    # Check if it's a quick number or full emote ID
                                    if len(number_or_id) <= 5:
                                        emote_id = vip_features.get_quick_emote_id(number_or_id)
                                        if not emote_id:
                                            emote_id = int(number_or_id)
                                    else:
                                        emote_id = int(number_or_id)
                                    
                                    # All parts before last are UIDs
                                    for i in range(1, len(parts) - 1):
                                        try:
                                            target_uids.append(int(parts[i]))
                                        except ValueError:
                                            continue
                                    
                                    print(f"🎯 Using {len(target_uids)} UIDs, Emote: {emote_id}")
                                
                                else:
                                    message = "[B][C][FF0000]❌ Wrong format!\n[FFFF00]Use: @a [number]\n[FFFFFF]Or: @a [uid1] [uid2] [emote]"
                                    P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                                
                                # Send emote to all target UIDs
                                if target_uids and emote_id:
                                    # Add to history
                                    vip_features.add_to_history(uid, emote_id)
                                    
                                    # Send confirmation message
                                    uids_text = ", ".join([str(u) for u in target_uids])
                                    message = f"[B][C][00FF00]🔥 Sending Emote!\n[FFFFFF]To: {len(target_uids)} UIDs\n[FFFF00]Emote: {emote_id}"
                                    P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                                    
                                    # Send emote packets to all UIDs
                                    sent_count = 0
                                    for target_uid in target_uids:
                                        try:
                                            H = await Emote_k(target_uid, emote_id, key, iv, region)
                                            await SEndPacKeT(whisper_writer, online_writer, "OnLine", H)
                                            await asyncio.sleep(0.1)
                                            sent_count += 1
                                            print(f"✅ Emote {emote_id} sent to UID {target_uid}")
                                        except Exception as e:
                                            print(f"❌ Failed to send to {target_uid}: {e}")
                                    
                                    print(f"✅ Emote {emote_id} sent to {sent_count}/{len(target_uids)} UIDs")
                                    
                            except ValueError:
                                message = "[B][C][FF0000]❌ Invalid numbers!\n[FFFF00]UID and Emote must be numbers\n[FFFFFF]Example: @a 909000001\n[FFFFFF]Or: @a 123456789 909000001"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                            except Exception as e:
                                print(f"❌ Emote error: {e}")
                                message = f"[B][C][FF0000]❌ Error sending emote!"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                        
                        # Auto-reply system
                        else:
                            # Check if auto-reply is enabled for this user
                            if vip_features.auto_reply_enabled.get(uid, False):
                                reply = vip_features.get_auto_reply(inPuTMsG)
                                if reply:
                                    message = f"[B][C][00FF00]{reply}"
                                    P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, "ChaT", P)
                                    print(f"🤖 Auto-replied to: {inPuTMsG}")
                        
                        response = None

            whisper_writer.close()
            await whisper_writer.wait_closed()
            whisper_writer = None

        except Exception as e:
            print(f"ErroR {ip}:{port} - {e}")
            whisper_writer = None
        await asyncio.sleep(reconnect_delay)


async def MaiiiinE():
    Uid, Pw = (
        "4259604271",
        "81DCF29316433DEB718D679B7BAAA04EA5A3E19BD297343EF7137F0B0760EA65",
    )

    open_id, access_token = await GeNeRaTeAccEss(Uid, Pw)
    if not open_id or not access_token:
        print("ErroR - InvaLid AccounT")
        return None

    PyL = await EncRypTMajoRLoGin(open_id, access_token)
    MajoRLoGinResPonsE = await MajorLogin(PyL)
    if not MajoRLoGinResPonsE:
        print("TarGeT AccounT => BannEd / NoT ReGisTeReD ! ")
        return None

    MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
    UrL = MajoRLoGinauTh.url
    print(UrL)
    region = MajoRLoGinauTh.region

    ToKen = MajoRLoGinauTh.token
    TarGeT = MajoRLoGinauTh.account_uid
    key = MajoRLoGinauTh.key
    iv = MajoRLoGinauTh.iv
    timestamp = MajoRLoGinauTh.timestamp

    LoGinDaTa = await GetLoginData(UrL, PyL, ToKen)
    if not LoGinDaTa:
        print("ErroR - GeTinG PorTs From LoGin DaTa !")
        return None
    LoGinDaTaUncRypTinG = await DecRypTLoGinDaTa(LoGinDaTa)
    OnLinePorTs = LoGinDaTaUncRypTinG.Online_IP_Port
    ChaTPorTs = LoGinDaTaUncRypTinG.AccountIP_Port
    OnLineiP, OnLineporT = OnLinePorTs.split(":")
    ChaTiP, ChaTporT = ChaTPorTs.split(":")
    acc_name = LoGinDaTaUncRypTinG.AccountName
    # print(acc_name)
    print(ToKen)
    equie_emote(ToKen, UrL)
    AutHToKen = await xAuThSTarTuP(int(TarGeT), ToKen, int(timestamp), key, iv)
    ready_event = asyncio.Event()

    task1 = asyncio.create_task(
        TcPChaT(
            ChaTiP,
            ChaTporT,
            AutHToKen,
            key,
            iv,
            LoGinDaTaUncRypTinG,
            ready_event,
            region,
        )
    )

    await ready_event.wait()
    await asyncio.sleep(1)
    task2 = asyncio.create_task(TcPOnLine(OnLineiP, OnLineporT, key, iv, AutHToKen))
    os.system("clear")
    print(render("ERFAN BOT", colors=["white", "red"], align="center"))
    print("")
    print("╔════════════════════════════════════════════════════════╗")
    print("║     🔥 ADVANCED FREE FIRE TCP BOT - BY ERFAN 🔥       ║")
    print("╚════════════════════════════════════════════════════════╝")
    print(f"\n[✓] Bot Account: {acc_name} (UID: {TarGeT})")
    print(f"[✓] Region: {region}")
    print(f"[✓] Status: ONLINE & READY")
    print(f"[✓] Features: 50+ Commands, Admin System, Stats Tracking")
    print(f"[✓] Commands: /help, /emotes, /nuke, /rain, /danceparty")
    print(f"\n[⚡] Bot is running... Use /help in-game for commands!")
    print(f"[📱] Instagram: @ERFAN HACKER\n")
    await asyncio.gather(task1, task2)


async def StarTinG():
    while True:
        try:
            await asyncio.wait_for(MaiiiinE(), timeout=7 * 60 * 60)
        except asyncio.TimeoutError:
            print("Token ExpiRed ! , ResTartinG")
        except Exception as e:
            print(f"ErroR TcP - {e} => ResTarTinG ...")


# Flask dummy server for Render (keeps service alive)
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head><title>ERFAN BOT</title></head>
        <body style="background:#000;color:#0f0;font-family:monospace;padding:50px;text-align:center;">
            <h1>🔥 ERFAN VIP BOT 🔥</h1>
            <h2>✅ Bot is Running!</h2>
            <p>Status: <span style="color:#0f0;">ONLINE</span></p>
            <p>Free Fire TCP Bot by ERFAN</p>
            <hr>
            <p>Bot is active and listening for commands in Free Fire!</p>
        </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "ok", "bot": "running", "service": "erfan-vip-bot"}

def run_flask():
    """Run Flask server on Render's PORT"""
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)

def run_bot():
    """Run the main bot"""
    asyncio.run(StarTinG())

if __name__ == "__main__":
    # Start Flask server in background thread
    flask_thread = Thread(target=run_flask, daemon=True)
    flask_thread.start()
    print("🌐 Flask server started on PORT for Render")
    
    # Run bot in main thread
    print("🤖 Starting ERFAN BOT...")
    run_bot()
