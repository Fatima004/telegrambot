from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from config import bot, dp
import logging


@dp.message_handler(commands=['start', 'help'])
async def start_command(message: types.Message):
    await message.answer(f"Привет! Я Бот обоснованный на фактах! {message.from_user.first_name}")


@dp.message_handler(commands=['facts'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("go!)", callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Сколько весил самый толстый человек в истории?"
    answers = [
        "615",
        "523",
        "727",
        "827",
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Learn more facts!",
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_2)

    question = "Самый высокий человек в истории?"
    answers = [
        "293",
        "254",
        "282",
        "Не знаю",
        'У меня есть брат высокий я думаю это он',
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="На самом деле Фатима",
        open_period=10,
    )


@dp.message_handler(commands=['mem'])
async def mem(call: types.CallbackQuery):
    photo = open("media/memchik.png", 'rb')
    await bot.send_photo(call.from_user.id, photo)


@dp.message_handler(content_types=['text', 'photo'])
async def echo(message: types.Message):
    k = message.text
    if message.text.isdigit():
        k = int(message.text) ** 2
    await bot.send_message(message.from_user.id, k)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
