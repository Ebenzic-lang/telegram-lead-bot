from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.inline import main_menu

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        "Welcome to my Lead Generation Bot! 🚀\n\nChoose an option below:",
        reply_markup=main_menu
    )
