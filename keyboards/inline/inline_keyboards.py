from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

send_score = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💸 Send 1 Score To Others...", callback_data="send_score")
        ]
    ]
)

exit_send = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="❌ Exit Sending!", callback_data="exit_send")
        ]
    ]
)
