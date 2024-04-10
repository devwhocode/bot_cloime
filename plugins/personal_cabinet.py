from integration.database import connect_to_remote_db
from aiogram import ReplyKeyboardMarkup, KeyboardButton 


async def handle_personal_cabinet(bot, dp, message):
    connection = connect_to_remote_db()
    cursor = connection.cursor()
    cursor.execute("SELECT `user`, `balance`, `name` FROM `users` WHERE `user_id` = %s", (message.from_user.id,))
    result = cursor.fetchone()
    if result is not None:
        user, balance, name = result
        fields = [
            ('Имя:', name),
            ('Баланс:', balance),
            ('Юзер:', user)
        ]
        markup = ReplyKeyboardMarkup(row_width=2)
        for field in fields:
            markup.add(KeyboardButton(f'{field[0]} {field[1]}'))
        await bot.send_message(message.chat.id, 'Личный кабинет:', reply_markup=markup)
    if result is not None:
        cursor.close()
        connection.close()

