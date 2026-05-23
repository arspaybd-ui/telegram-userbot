import os
from telethon import TelegramClient, events

api_id = int(os.environ["37016967"])
api_hash = os.environ["a55a0cd4bdaf52d12f29b322547c5eac"]

client = TelegramClient("session", api_id, api_hash)


@client.on(events.NewMessage(pattern='/pay'))
async def pay(event):
    await event.reply("""
💳 PAYMENT METHODS
━━━━━━━━━━━━━━

🟣 Bkash
➤ `01331202837`

🟠 Nagad
➤ `01957858795`

🔵 Rocket
➤ `01957858795`

🟢 Upay
➤ `01957858795`
""")


@client.on(events.NewMessage(pattern=r'/calc (.+)'))
async def calc(event):
    try:
        expression = event.pattern_match.group(1)
        result = eval(expression)
        await event.reply(f"🧮 Result: `{result}`")
    except:
        await event.reply("❌ Invalid")

print("Userbot Running...")
client.start()
client.run_until_disconnected()
