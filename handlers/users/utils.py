import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()
#
# def find_id_handler(message, odamla: dict, random_number: int, chat_id):
#     if message.text in odamla.keys():
#         userr = cursor.execute(f"SELECT * FROM users WHERE chat_id='{chat_id}'").fetchone()
#         userr1 = cursor.execute(f"SELECT score FROM users WHERE random_number_id='{random_number}'").fetchone()
#         cursor.execute(f"UPDATE users SET score={userr[-1] + 1} WHERE random_number_id={random_number}")
#         cursor.execute(f"UPDATE users SET score={userr1[-1] - 1} WHERE chat_id={chat_id}")
#         name = cursor.execute(f"SELECT full_name FROM users WHERE random_number_id={random_number}").fetchone()
#         id = cursor.execute(f"SELECT random_number_id FROM users WHERE random_number_id={random_number}").fetchone()
#         text1 = f"""
# ✅ Succefully Gaved
# Name: {name}
# ID: {id}
# """
#         return text1
#     text2 = "❌ Your ID Not Found!"
#     return text2

# cursor.execute("DROP TABLE users;")
# conn.commit()
