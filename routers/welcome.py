import aiogram.types
from aiogram import Router, types, filters

from core import Client, TelegramUser, Language, welcome_keyboard

welcome_router = Router(name=__name__)
client = Client()


@welcome_router.message(filters.Command("start"))
async def command_start(message: types.Message) -> None:
    user: TelegramUser = await client.database.get_object_by_id(
        message.from_user.id,
        TelegramUser
    )  # TODO: Edit to BaseMiddleware system

    if not user:
        user = TelegramUser(_id=message.from_user.id)
        await user.save()

    if user.language is Language.NULL:
        await message.answer(
            client.i18n["en-US"]['WELCOME_MESSAGE'],
            reply_markup=welcome_keyboard()
        )


@welcome_router.callback_query()
async def callback_data(callback: aiogram.types.CallbackQuery) -> None:
    custom_ids = callback.data.split(":")

    match custom_ids[0]:
        case "language-select":
            user: TelegramUser = await client.database.get_object_by_id(
                callback.from_user.id,
                TelegramUser
            )
            user.language = Language(custom_ids[1])

            await callback.answer("")
            await user.save()
