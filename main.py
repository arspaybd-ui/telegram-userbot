import os
from telethon import TelegramClient, events

# Railway Variables
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session = os.environ["SESSION"]

# Client
client = TelegramClient("session", api_id, api_hash)


# START COMMAND
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("""
🤖 USERBOT ACTIVE

Commands:
/pay - Payment methods
/calc 10+5 - Calculator
""")


# PAYMENT COMMAND
@client.on(events.NewMessage(pattern='/Apay'))
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


# CALCULATOR COMMAND
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
