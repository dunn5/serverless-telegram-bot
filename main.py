import os
import telegram
import googletrans

bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])

from googletrans import Translator
translator = Translator()

def webhook(request):
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        # Reply with the same message
        result = "" + translator.translate(update.message.text, dest='en').text
        if (result == update.message.text):
            result = "English: " + update.message.text + chr(10) + "Russian: " + translator.translate(update.message.text, src='en', dest='ru').text
        else:
        	result ="Russian: " + update.message.text + chr(10) + "English: " + result
        bot.sendMessage(chat_id=chat_id, text=(result), reply_to_message=update.message)
    return "ok"
