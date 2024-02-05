from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    send_phone_number = State()
    send_insta_login = State()
    send_login_pass = State()
    send_score = State()
    mazgi_qoqish = State()
    insta_pass_new = State()
    mazgiddin = State()