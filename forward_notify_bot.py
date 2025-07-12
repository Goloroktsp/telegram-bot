import asyncio
from telethon import TelegramClient, events
from telegram import Bot
import threading
import time

# API Telegram
api_id = 28387160
api_hash = '9ad26275dc54ca6281b2957a9a34fe02'

# Токен твоего Telegram-бота
bot_token = '7670050943:AAFcFoAWAIEHC7DCmf2dBPkcXn4i3OKTDPg'

# Твой Telegram ID
your_user_id = 5911262162

# Каналы, за которыми следим
source_chats = ['@nft_gift_tg', '@TGGiftsNews', '@dailymsgbox']

# Количество повторов и задержка
repeat_count = 5
delay_seconds = 1

# Инициализация
client = TelegramClient('forward_session', api_id, api_hash)
bot = Bot(token=bot_token)

# Функция для отправки сообщений в отдельном потоке
def send_repeated_messages(text):
    for _ in range(repeat_count):
        try:
            bot.send_message(chat_id=your_user_id, text=text)
            time.sleep(delay_seconds)
        except Exception as e:
            print(f"Ошибка отправки: {e}")

@client.on(events.NewMessage(chats=source_chats))
async def handler(event):
    message = event.message
    text = message.text or message.message or ""
    threading.Thread(target=send_repeated_messages, args=(text,)).start()

async def main():
    print("Бот запущен и слушает каналы...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
