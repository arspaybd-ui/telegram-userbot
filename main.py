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

@client.on(events.NewMessage(pattern='Apay'))
async def pay(event):
    await event.reply("""
💳 PAYMENT METHODS

🟣 Bkash Parsonal
`01957858795`

🟣 Bkash Merchant
`01331202837`

🟠 Nagad
`01957858795`

🔵 Rocket
`01957858795`

🟢 Upay
`01957858795`
""")

# CALCULATOR COMMAND
@client.on(events.NewMessage(pattern=r'c (.+)'))
async def calc(event):
    try:
        expression = event.pattern_match.group(1)
        result = eval(expression)

        await event.reply(f"""
✓ CALCULATION COMPLETED

➥ INPUT : {expression}
➥ RESULT : {result}

━━━━━━━━━━━━━━
""")

    except:
        await event.reply("""
✗ CALCULATION FAILED

➥ Invalid input
━━━━━━━━━━━━━━
""")
        
print("Userbot Running...")

with client:
    client.run_until_disconnected()
