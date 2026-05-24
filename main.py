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
💳 পেমেন্ট নাম্বার সমূহ
━━━━━━━━━━━━━━━━

🟣 বিকাশ (মার্চেন্ট)
➥ `01331202837`

🟠 নগদ (পার্সোনাল)
➥ `01957858795`

🔵 রকেট (পার্সোনাল)
➥ `01957858795`

🟢 উপায় (পার্সোনাল)
➥ `01957858795`

━━━━━━━━━━━━━━━━

✓ পেমেন্ট শেষে স্ক্রিনশট ও
ট্রানজেকশন আইডি পাঠান।
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
