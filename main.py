import aiogram
from aiogram import types, executor
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from plugins.support_main import handle_tech_support
from plugins.order import handle_order
from plugins.personal_cabinet import handle_personal_cabinet as pc_handler



# Инициализация бота
bot = aiogram.Bot('TOKEN')
dp = aiogram.Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply( "Вас приветсвует Бот студии разработки Slim. \n\n"
        "1️⃣ Здесь вы можете оформить заказ \n\n"
        "2️⃣ Связаться с технической поддержкой. \n\n"
        "3️⃣ Узновать информацию о нас, получать уведомления быстрее чем остальные.\n\n"
    "Используйте кнопки ниже из меню:",
    reply_markup=ReplyKeyboardRemove()
)

    markup = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton('Группа вконтакте', url='https://vk.com/slim_group')
    button2 = InlineKeyboardButton('Сайт', url='https://slim.kz')
    markup.add(button1, button2)
    await bot.send_message(message.chat.id, 'Информация:', reply_markup=markup)

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button3 = KeyboardButton('Личный кабинет')
    button4 = KeyboardButton('Оформить заказ')
    button5 = KeyboardButton('Техническая поддержка')
    button6 = KeyboardButton('О нас')
    keyboard.add(button3, button4, button5, button6)
    await bot.send_message(message.chat.id, 'Выбери действие:', reply_markup=keyboard)



@dp.message_handler(lambda message: message.text == 'Личный кабинет')
async def wrapper_personal_cabinet(message: types.Message, bot: aiogram.Bot, dp: aiogram.Dispatcher):
    await pc_handler(bot, dp, message)


@dp.message_handler(lambda message: message.text == 'Оформить заказ')
async def wrapper_order(message: types.Message, bot: aiogram.Bot, dp: aiogram.Dispatcher):
    await handle_order(bot, dp, message)


@dp.message_handler(lambda message: message.text == 'Техническая поддержка')
async def wrapper_tech_support(message: types.Message, bot: aiogram.Bot, dp: aiogram.Dispatcher):
    await handle_tech_support(bot, dp, message)


@dp.message_handler(lambda message: message.text == 'О нас')
async def wrapper_about_us(message: types.Message, bot: aiogram.Bot, dp: aiogram.Dispatcher):
    await handle_about_us(bot, dp, message)

#Запуск бота и передача диспетчера и bot
if __name__ == '__main__':
    executor.start_polling(dp, bot)