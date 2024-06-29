from pprint import pprint

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states import SignUp


async def info(message: Message, bot: Bot, state: FSMContext):
    profile = await bot.get_chat(chat_id=message.from_user.id)
    user = message.from_user
    data = f""" Sizning ismingiz : {user.first_name} \nId raqamingiz: {user.id} \n"""
    if user.username:
        data += f"Siznig usernameiz @{user.username}\n"
    if user.last_name:
        data += f"Sizning familyangiz {user.last_name}\n"
    if profile.bio:
        data += f"Sizning bioingiz {profile.bio}\n"
    pprint(data)
    await message.answer(text=data)


async def helps(message: Message, bot: Bot, state: FSMContext):
    await message.answer("""
/start -> Botni ishga tushirish
/help -> Commandlarni ko'rish
/vacancy -> E'lon berish

    """)


async def vacancy(message: Message, bot: Bot, state: FSMContext):
    await message.answer(
        "Idora nomini kiriting: "
    )
    await state.set_state(SignUp.Idora)


async def register_idora(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(Idora=message.text)
    await message.answer("Texnalogiyalarni kiriting: ")
    await state.set_state(SignUp.Texnologiya)


async def register_tex(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(Texnologiya=message.text)
    await message.answer("Telegram nikingizni kiriting: ")
    await state.set_state(SignUp.Telegram)


async def register_telegram(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(Telegram=message.text)
    await message.answer("Telefon nomeringizni kiriting: ")
    await state.set_state(SignUp.Aloqa)


async def register_aloqa(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(Aloqa=message.text)
    await message.answer("Hududni  kiriting: ")
    await state.set_state(SignUp.Hudud)


async def register_hudud(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(Hudud=message.text)
    await message.answer("Mas'ulni kiriting: ")
    await state.set_state(SignUp.Masul)


async def register_masul(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(Masul=message.text)
    await message.answer("Murojaat vaqtini kiriting:")
    await state.set_state(SignUp.Murojaat_vaqti)


async def register_murojat(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(Murojaat_vaqti=message.text)
    await message.answer("Ish vaqtini kiriting: ")
    await state.set_state(SignUp.Ish_vaqti)


async def register_ish(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(Ish_vaqti=message.text)
    await message.answer("Maoshni kiriting: ")
    await state.set_state(SignUp.Maosh)


async def register_maosh(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(Maosh=message.text)
    await message.answer("Qo'shimcha kiriting: ")
    await state.set_state(SignUp.Qoshimcha)


async def register_finish(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(Qoshimcha=message.text)
    data = await state.get_data()
    txt = f'''Siznign e'loningiz:\n \n
🏢Idora: {data.get("Idora ")}
📚Texnologiya: {data.get("Texnologiya")}
🇺🇿 Telegram: {data.get("Telegram")}
📞 Aloqa: {data.get("Aloqa")}
🌐 Hudud: {data.get("Hudud")}
✍️ Mas'ul: {data.get("Masul")}
🕰 Murojaat vaqt: {data.get("Murojaat_vaqti")}
🕰 Ish vaqti: {data.get("Ish_vaqti")}
💰 Maosh: {data.get("Maosh")}
‼️ Qo`shimcha: {data.get("Qoshimcha")}
'''
    await state.clear()
    await message.answer(text=txt, parse_mode="html")
    await message.answer("Siznig E'loningiz Admin Tomonidan Tekshirilib Tez Orada Kanalda Chop etiladi")
    await bot.send_message(chat_id="1932693641", text=txt)
    await state.clear()



async def start_menu(message: Message, bot: Bot, state: FSMContext):
    await message.answer(f"Assalomu Alaykun {message.from_user.first_name} /help orqali menularni ko'ring")


async def start(bot: Bot):
    await bot.send_message(chat_id="1932693641", text="Bot Ishga tushdi ✅")


async def stop(bot: Bot):
    await bot.send_message(chat_id="1932693641", text="Bot To'xtadi ⚠️")

