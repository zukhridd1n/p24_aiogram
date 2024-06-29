import os
from asyncio import run

from aiogram.filters import Command
from aiogram.types import BotCommand, Message
from dotenv import load_dotenv

from founctions import start, info, stop, vacancy, helps, start_menu, register_tex, register_ish, register_aloqa, register_maosh, register_idora, register_telegram, register_murojat, register_finish, register_masul, register_hudud
from states import SignUp

load_dotenv()

from aiogram import Bot, Dispatcher

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


async def main(dp) -> None:
    bot = Bot(token=TOKEN)
    await bot.set_my_commands(
        [
            BotCommand(command="/start", description="Bot ni ishga tushirish"),
            BotCommand(command="/info", description="Shaxsiy ma'lumotlarni olish"),
            BotCommand(command="/vacancy", description="Ishga e'lon berish"),
            BotCommand(command="/help", description="Yordam")
        ]
    )
    dp.startup.register(start)
    dp.message.register(vacancy, Command('vacancy'))
    dp.message.register(register_idora, SignUp.Idora)
    dp.message.register(register_tex, SignUp.Texnologiya)
    dp.message.register(register_telegram, SignUp.Telegram)
    dp.message.register(register_aloqa, SignUp.Aloqa)
    dp.message.register(register_hudud, SignUp.Hudud)
    dp.message.register(register_masul, SignUp.Masul)
    dp.message.register(register_murojat, SignUp.Murojaat_vaqti)
    dp.message.register(register_ish, SignUp.Ish_vaqti)
    dp.message.register(register_maosh, SignUp.Maosh)
    dp.message.register(register_finish, SignUp.Qoshimcha)
    dp.message.register(info, Command('info'))
    dp.message.register(start_menu, Command('start'))
    dp.message.register(helps, Command('help'))
    dp.shutdown.register(stop)
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main(dp))


