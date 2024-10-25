from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def welcome_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🇷🇺 Русский",
                    callback_data="language-select:ru"
                ),
                InlineKeyboardButton(
                    text="🇺🇸 English",
                    callback_data="language-select:en-US"
                )
            ]
        ]
    )