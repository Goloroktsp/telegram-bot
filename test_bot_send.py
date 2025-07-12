import asyncio
from telegram import Bot

# 🔑 Новый токен
bot_token = '7670050943:AAFcFoAWAIEHC7DCmf2dBPkcXn4i3OKTDPg'

# 👤 Твой Telegram user ID
your_user_id = 5911262162

async def main():
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=your_user_id, text="Бот работает! ✅ Ты получил это сообщение.")

asyncio.run(main())
