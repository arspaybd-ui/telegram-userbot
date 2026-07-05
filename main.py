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

@client.on(events.NewMessage(pattern=r'(?i)^apay$'))
async def pay(event):

    # শুধু আপনার নিজের message হলে কাজ করবে
    if not event.out:
        return

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
❤️ Thank You For Choosing ARS TOPUP BD
""")
@client.on(events.NewMessage)
async def auto_calc(event):
    if not event.out:
        return
    try:
        text = event.raw_text.strip()

        if text.startswith("/"):
            return

        if not any(op in text for op in ["+","-","*","/"]):
            return

        allowed = "0123456789+-*/(). "
        if not all(ch in allowed for ch in text):
            return

        result = eval(text)

       await event.reply(f"""
✓ Cᴀʟᴄᴜʟᴀᴛɪᴏɴ Cᴏᴍᴘʟᴇᴛᴇᴅ
➦ Iɴᴘᴜᴛ :
➥ `{text}`
➦ Rᴇsᴜʟᴛ :
➥ `{result}`
━━━━━━━━━━━━━━━━━━
""")
    except Exception:
        pass

print("✅ Userbot Running...")

with client:
    client.run_until_disconnected()
