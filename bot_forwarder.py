import asyncio
from telethon import TelegramClient, events
from telegram import Bot
from telegram.error import TelegramError

# Данные твоего аккаунта
api_id = 28387160
api_hash = '9ad26275dc54ca6281b2957a9a34fe02'
session_name = 'session_name'

# Данные твоего бота
bot_token = '7670050943:AAFcFoAWAIEHC7DCmf2dBPkcXn4i3OKTDPg'
your_user_id = 5911262162

# Каналы, которые бот читает
source_chats = ['@nft_gift_tg', '@TGGiftsNews', '@dailymsgbox']

# Повторная отправка сообщений
repeat_count = 5
delay_seconds = 1

client = TelegramClient(session_name, api_id, api_hash)
bot = Bot(token=bot_token)

@client.on(events.NewMessage(chats=source_chats))
async def handler(event):
    message_text = event.message.message

    for i in range(repeat_count):
        try:
            await bot.send_message(chat_id=your_user_id, text=f"🔁 #{i+1}: {message_text}")
            await asyncio.sleep(delay_seconds)
        except TelegramError as e:
            print(f"Ошибка отправки: {e}")

async def main():
    print("Бот запущен и следит за каналами...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
