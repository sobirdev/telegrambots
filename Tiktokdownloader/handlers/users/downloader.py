from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp
from tiktok import tk
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CallbackQuery


@dp.message_handler(Text(startswith="https://www.tiktok.com"))
async def test(message:types.Message):
    natija = tk(message.text)
    qoshiq = natija['Music']

    btn = InlineKeyboardMarkup(
        inline_keyboard = [
            [InlineKeyboardButton(text = "Musiqani yuklab olish 📥",url = "{}".format(qoshiq))]
        ]
    )
    await message.answer_audio(natija['Video'], reply_markup=btn)

