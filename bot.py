import telegram
bot = telegram.Bot(token="7245572263:AAHRGAQE3v8EN4wUvTiKiLONyTiYiCBHLJI")
print(bot.get_me())
bot.send_message(text='Всем привет!', chat_id="@space_photos0")
bot.send_document(chat_id="@space_photos0", document=open('images/epic_0.png', 'rb'))