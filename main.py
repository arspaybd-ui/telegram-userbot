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

@client.on(events.NewMessage(pattern='/Apay'))
async def pay(event):
    await event.reply("""
💳 PAYMENT METHODS

🟣 Bkash
`01331202837`

🟠 Nagad
`01957858795`

🔵 Rocket
`01957858795`

🟢 Upay
`01957858795`
""")

print("Userbot Running...")

with client:
    client.run_until_disconnected()
