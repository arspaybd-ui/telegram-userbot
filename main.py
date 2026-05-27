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
╔════════════════════╗
      💳 পেমেন্ট সিস্টেম
╚════════════════════╝

🟣 বিকাশ (মার্চেন্ট)
➤ `01331202837`

🟠 নগদ (পার্সোনাল)
➤ `01957858795`

🔵 রকেট (পার্সোনাল)
➤ `01957858795`

🟢 উপায় (পার্সোনাল)
➤ `01957858795`

━━━━━━━━━━━━━━━━━━━

📌 পেমেন্ট করার পর পাঠান:

✓ স্ক্রিনশট  
✓ ট্রানজেকশন আইডি   

━━━━━━━━━━━━━━━━━━━

❤️ ধন্যবাদ
""")
# AUTO CALCULATOR

@client.on(events.NewMessage)
async def auto_calc(event):
    try:
        text = event.raw_text.strip()

        # শুধু math expression হলে কাজ করবে
        allowed = "0123456789+-*/().% "

        if all(ch in allowed for ch in text):

            result = eval(text)

            await event.reply(f"""
╔════════════════╗
      🧮 ক্যালকুলেটর
╚════════════════╝

➥ INPUT:
`{text}`

➥ RESULT:
`{result}`

━━━━━━━━━━━━━━━━
""")

    except:
        pass
        # PAYMENT VERIFY COMMAND
@client.on(events.NewMessage(pattern='verify'))
async def verify(event):
    await event.reply("""
✓ পেমেন্ট ভেরিফিকেশন

━━━━━━━━━━━━━━

➥ নিচের তথ্যগুলো পাঠান:

• পেমেন্ট স্ক্রিনশট
• ট্রানজেকশন আইডি
• যে নাম্বার থেকে পেমেন্ট করেছেন
• পেমেন্টের পরিমাণ

━━━━━━━━━━━━━━

⚡ ভেরিফিকেশন সম্পন্ন হতে
১ - ১০ মিনিট সময় লাগতে পারে।

✓ ভেরিফিকেশন সম্পন্ন হলে
আপনার সার্ভিস চালু করে দেওয়া হবে।

━━━━━━━━━━━━━━

ধন্যবাদ ❤️
""")
        
print("Userbot Running...")

with client:
    client.run_until_disconnected()
