from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "Get Started")
async def get_started(message: Message):
    await message.answer("Let's get started! Please share your business name.")

@router.message(F.text == "Services")
async def services(message: Message):
    await message.answer(
        "We offer:\n"
        "• Lead Generation\n"
        "• Customer Acquisition\n"
        "• Marketing Automation"
    )

@router.message(F.text == "Contact Admin")
async def contact_admin(message: Message):
    await message.answer("Contact our admin: @Gupcupp")
