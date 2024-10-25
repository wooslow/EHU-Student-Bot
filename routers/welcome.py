from aiogram import Router, types, filters


welcome_router = Router()


@welcome_router.message(filters.Command("start"))
async def command_start(message: types.Message) -> None:
    ...
