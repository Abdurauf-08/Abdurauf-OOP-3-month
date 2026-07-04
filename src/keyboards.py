from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)


keybord_main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Python")],
    [KeyboardButton(text="JS")],
    [KeyboardButton(text="C#")]

],
resize_keyboard=True,
input_field_placeholder="Выберите один пункт"
)

help_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Python Docs", url="https://docs.python.org/3/")],
    [InlineKeyboardButton(text="JavaScript Docs", url="https://developer.mozzila.org/docs/Web/JavaScript")],
    [InlineKeyboardButton(text="C# Docs", url="https://learn.microsoft.com/dotnet/csharp/")],
    [InlineKeyboardButton(text="Начинаем обучения", callback_data="start_learning")]
])