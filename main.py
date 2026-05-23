from telethon import TelegramClient, events
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("session", api_id, api_hash)


@client.on(events.NewMessage(pattern='/pay'))
async def pay(event):
    await event.reply("""
💳 PAYMENT METHODS
━━━━━━━━━━━━━━

🟣 Bkash (Merchant)
➤ `01331202837`

🟠 Nagad (Personal)
➤ `01957858795`

🔵 Rocket (Personal)
➤ `01957858795`

🟢 Upay (Personal)
➤ `01957858795`

━━━━━━━━━━━━━━
📌 Hold number to copy
""")

@client.on(events.NewMessage(pattern=r'/calc (.+)'))
async def calc(event):
    try:
        expression = event.pattern_match.group(1)
        result = eval(expression)

        await event.reply(
            f"🧮 Calculator\n\n`{expression}` = `{result}`"
        )
    except:
        await event.reply("❌ Invalid calculation")


print("Userbot Running...")
client.start()
client.run_until_disconnected()