import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session = os.environ["SESSION"]

client = TelegramClient(
    StringSession(session),
    api_id,
    api_hash
)

@client.on(events.NewMessage(pattern=r'(?i)Apay'))
async def pay(event):
    await event.reply("""
╭━━━〔 💳 Pᴀʏᴍᴇɴᴛ Sʏsᴛᴇᴍ 〕━━━╮

🟣 Bᴋᴀsʜ (Mᴇʀᴄʜᴀɴᴛ)
┏━━━━━━━━━━━━┓
➥ `01331202837`
┗━━━━━━━━━━━━┛

🟠 Nᴀɢᴀᴅ (Pᴇʀsᴏɴᴀʟ)
┏━━━━━━━━━━━━┓
➥ `01957858795`
┗━━━━━━━━━━━━┛

🔵 Rᴏᴄᴋᴇᴛ (Pᴇʀsᴏɴᴀʟ)
┏━━━━━━━━━━━━┓
➥ `01957858795`
┗━━━━━━━━━━━━┛

🟢 Uᴘᴀʏ (Pᴇʀsᴏɴᴀʟ)
┏━━━━━━━━━━━━┓
➥ `01957858795`
┗━━━━━━━━━━━━┛

╰━━━━━━━━━━━━━━━━━━━━╯

📌 Pᴀʏᴍᴇɴᴛ Sᴇɴᴅ Kᴏʀᴀʀ Pᴏʀ
Sᴄʀᴇᴇɴsʜᴏᴛ & Tʀx ID Pᴀᴛʜᴀɴ

""")

# AUTO CALCULATOR

@client.on(events.NewMessage)
async def auto_calc(event):
    try:
        text = event.raw_text.strip()

        allowed = "0123456789+-*/().% "

        if all(ch in allowed for ch in text):

            result = eval(text)

            await event.reply(f"""
✓ Cᴀʟᴄᴜʟᴀᴛɪᴏɴ Cᴏᴍᴘʟᴇᴛᴇᴅ

➦ Iɴᴘᴜᴛ :
➥ `{text}`

➦ Rᴇsᴜʟᴛ :
➥ `{result}`

━━━━━━━━━━━━━━━━━━
""")

        
print("Userbot Running...")

with client:
    client.run_until_disconnected()
