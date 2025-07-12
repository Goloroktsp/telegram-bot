import asyncio
from telethon import TelegramClient, events
from telegram import Bot

# Telethon данные
api_id = 28387160
api_hash = '9ad26275dc54ca6281b2957a9a34fe02'

# Источники
source_chats = ['@nft_gift_tg', '@TGGiftsNews', '@dailymsgbox']

# Данные Telegram-бота
bot_token = '7670050943:AAFcFoAWAIEHC7DCmf2dBPkcXn4i3OKTDPg'
your_user_id = 5911262162  # твой Telegram ID

repeat_count = 5
delay_seconds = 1

client = TelegramClient('session_name', api_id, api_hash)
bot = Bot(token=bot_token)

@client.on(events.NewMessage(chats=source_chats))
async def handler(event):
    text = event.message.message
    for _ in range(repeat_count):
        try:
            await bot.send_message(chat_id=your_user_id, text=text)
            await asyncio.sleep(delay_seconds)
        except Exception as e:
            print(f'Ошибка отправки: {e}')

async def main():
    print("Бот запущен, слушает каналы...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
