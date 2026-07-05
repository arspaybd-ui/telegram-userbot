import os
from telethon import TelegramClient,
events from telethon.sessions
import StringSession
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
╔══════════════════════╗
      💳 Pᴀʏᴍᴇɴᴛ Mᴇᴛʜᴏᴅs
╚══════════════════════╝

🟣 ʙKᴀsʜ • Mᴇʀᴄʜᴀɴᴛ
╭────────────────────╮
│ `01331202837`
╰────────────────────╯

🟣 ʙKᴀsʜ • Pᴇʀsᴏɴᴀʟ
╭────────────────────╮
│ `01957858795`
╰────────────────────╯

🟠 Nᴀɢᴀᴅ • Pᴇʀsᴏɴᴀʟ
╭────────────────────╮
│ `01957858795`
╰────────────────────╯

🔵 Rᴏᴄᴋᴇᴛ • Pᴇʀsᴏɴᴀʟ
╭────────────────────╮
│ `01957858795`
╰────────────────────╯

🟢 Uᴘᴀʏ • Pᴇʀsᴏɴᴀʟ
╭────────────────────╮
│ `01957858795`
╰────────────────────╯

━━━━━━━━━━━━━━━━━━━━━━

📌 Pᴀʏᴍᴇɴᴛ Sᴇɴᴅ Kᴏʀᴀʀ Pᴏʀ

✓ Sᴄʀᴇᴇɴsʜᴏᴛ
✓ Tʀᴀɴsᴀᴄᴛɪᴏɴ ID
✓ Sᴇɴᴅᴇʀ Nᴜᴍʙᴇʀ
✓ Pᴀɪᴅ Aᴍᴏᴜɴᴛ

━━━━━━━━━━━━━━━━━━━━━━

⚡ Vᴇʀɪғɪᴄᴀᴛɪᴏɴ Tɪᴍᴇ
1 - 10 Mɪɴᴜᴛᴇs

❤️ Tʜᴀɴᴋ Yᴏᴜ Fᴏʀ Cʜᴏᴏsɪɴɢ
Aʀs Tᴏᴘᴜᴘ Bᴅ
""")
@client.on(events.NewMessage)

async def auto_calc(event):

    if not event.out:
        return

    try:
        text = event.raw_text.strip()

        # Command ignore
        if text.startswith("/"):
            return

        # Operator না থাকলে calculator চলবে না
        if not any(op in text for op in ["+", "-", "*", "/"]):
            return

        result = eval(text)

       await event.reply(f"""
╭━━━〔 🧮 Cᴀʟᴄᴜʟᴀᴛᴏʀ 〕━━━╮
✓ Cᴀʟᴄᴜʟᴀᴛɪᴏɴ Cᴏᴍᴘʟᴇᴛᴇᴅ
➥ Iɴᴘᴜᴛ
`{text}`
➥ Rᴇsᴜʟᴛ
`{result}`
╰━━━━━━━━━━━━━━━━━━╯
""")

    except Exception:
        pass

print("Userbot Running...")

with client:
    client.run_until_disconnected()    
