import os
import asyncio
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def send_test_message():
    if not TOKEN or not CHAT_ID:
        print("Error: Telegram Token or Chat ID is missing in your .env file")
        return

    bot = Bot(token=TOKEN)
    message=(
        "🤖 **Job Apply Agent - System Update**\n\n"
        "✅ Task 1 Verified: Indeed session cookies loaded successfully.\n"
        "🚀 Telegram notification pipeline is now fully operational!"
    )

    try: 
        await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")
        print("Test Message sent to your telegram chat")

    except Exception as e:
        print(f"Failed to send Telegram message: {e}")

if __name__ == "__main__":
    asyncio.run(send_test_message())
