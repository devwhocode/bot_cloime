#Функция обработки вызова тех. поддержки
async def handle_tech_support(bot, dp, message):
    await bot.send_message(message.chat.id, 'Техническая поддержка')
    