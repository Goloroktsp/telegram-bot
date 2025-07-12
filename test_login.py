from telethon.sync import TelegramClient

api_id = 28387160
api_hash = '9ad26275dc54ca6281b2957a9a34fe02'

with TelegramClient('session_name', api_id, api_hash) as client:
    print("Успешный вход как", client.get_me().username)
