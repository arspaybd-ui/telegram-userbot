import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# =========================
# Railway Variables
# =========================

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session = os.environ["SESSION"]

client = TelegramClient(
    StringSession(session),
    api_id,
    api_hash
)

# =========================
# Payment Command
# =========================

@client.on(events.NewMessage(pattern=r'(?i)^apay$'))
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

# =========================
# Private Auto Calculator
# =========================

@client.on(events.NewMessage)
async def auto_calc(event):

    # শুধু আপনার নিজের message
    if not event.out:
        return

    try:
        text = event.raw_text.strip()

        # Command ignore
        if text.startswith("/"):
            return

        # শুধুমাত্র operator থাকলে
        if not any(op in text for op in ["+", "-", "*", "/"]):
            return

        # শুধু valid character
        allowed = "0123456789+-*/(). "

        if not all(ch in allowed for ch in text):
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


print("✅ Userbot Running...")

with client:
    client.run_until_disconnected()
