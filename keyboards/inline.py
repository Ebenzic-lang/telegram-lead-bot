from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Get Started", callback_data="get_started")],
        [InlineKeyboardButton(text="Services", callback_data="services")],
        [InlineKeyboardButton(text="Contact Admin", callback_data="contact_admin")]
    ]
)
