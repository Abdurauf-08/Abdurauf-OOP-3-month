from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from src.keyboards import keybord_main, help_keyboard

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Выберите язык програмирования:",
        reply_markup=keybord_main
    )
    
@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Полезные ссылки:",
        reply_markup=help_keyboard
    )

@router.message(F.text == "Python")
async def python_info(message: Message):
    await message.answer(
        "Python - простой и популярный язык програмирования."
    )

@router.message(F.text == "JS")
async def js_info(message: Message):
    await message.answer(
        "JavaScript - язык для создания интерактивных веб-сайтов."
    )

@router.message(F.text == "C#")
async def  csharp_info(message: Message):
    await message.answer(
        "C# - язык програмирования от Microsoft."
    )

@router.callback_query(F.data == "start_learning")
async def start_learning(callback: CallbackQuery):
    await callback.answer(
        "Начинаем обучение!",
        show_alert=True
    )

@router.message()
async def echo(message: Message):
    await message.answer(f"Ты написал {message.text}")





