import asyncio
from telethon import TelegramClient, events
from telegram import Bot

# Твои данные API Telegram (Telethon)
api_id = 28387160
api_hash = '9ad26275dc54ca6281b2957a9a34fe02'

# Токен твоего бота Telegram Bot API
bot_token = '7670050943:AAFcFoAWAIEHC7DCmf2dBPkcXn4i3OKTDPg'

# Твой Telegram user ID — куда бот будет отправлять сообщения
your_user_id = 5911262162

# Список каналов для отслеживания
source_chats = ['@nft_gift_tg', '@TGGiftsNews', '@dailymsgbox']

# Кол-во повторов и задержка между ними (сек)
repeat_count = 5
delay_seconds = 1

# Инициализация клиентов
client = TelegramClient('forward_session', api_id, api_hash)
bot = Bot(token=bot_token)

@client.on(events.NewMessage(chats=source_chats))
async def handler(event):
    message = event.message
    text = message.text or message.message or ""

    for _ in range(repeat_count):
        try:
            await bot.send_message(chat_id=your_user_id, text=text)
        except Exception as e:
            print(f"Ошибка отправки: {e}")
        await asyncio.sleep(delay_seconds)

async def main():
    print("Бот запущен и слушает каналы...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
