---
description: Python ile telegram botu oluşturma ve otomatik olarak mesaj cevaplama
---

# 🤖 Telegram Botu Oluşturma

## 👀 Hızlı Bakış

* Whatapp alternatifi mesajlaşma uygulamasıdır, grup üye sayısı sınırsızdır
* Açık kaynak bir uygulama olduğundan yazılımlar ile erişebilen bir API hizmeti sunar
* API üzerinden kişisel botlar oluşturabilir ve kendi iş akışınızı geliştirebilirsiniz

{% hint style="info" %}
👨‍💻 Programlama işleri ile ilgilenenler için telegram ideal bir chat uygulamasıdır.
{% endhint %}

## 🤖 Bot Oluşturma

* Telegram üzerinden [BotFather](https://telegram.me/botfather) kanalına mesaj atmalısın 
* `/newbot` komutu ile bot oluşturma isteğinde bulun
* İlk önce botun için isim oluştur, bu isim **türkçe karakter içerebilir ve uzun olabili**r
* Ardından botun için **eşsiz** bir kullanıcı adı belirlemen gerekir
* Bot oluşturulduktan sonra sana **token** bilgisi verilecek bu bilgiyi kopyalamalı ve saklamalısın
* Botuna erişmek için `t.me/<botkullanıcı_adı>` bağlantısına bakmalısın

## 🆔 Bot için Chat ID Alma

* Chat ID, botunuza her mesaj atan kullanıcının id bilgisidir
* Chat ID ile istediğiniz kullanıcıya mesaj gönderebilirsiniz
* Chat ID değerini almak için .[https://api.telegram.org/botXXX:YYYY/getUpdates](https://api.telegram.org/botXXX:YYYY/getUpdates) bağlantısındaki
  * XXX:YYYY alanına daha önceden kopyaladığınız token bilginizi yapıştırın
  * Örneğin: `https://api.telegram.org/bot12345:TOKEN_DEVAMI/getUpdates` 
* Döndürülen JSON metninde `id:` alanı içerisinde Chat ID bilgisini alabilirsiniz

{% code title="Örnek JSON çıktısı" %}
```javascript
{
    "ok": true,
    "result": [
        {
            "update_id": 0,
            "message": {
                "message_id": 0,
                "from": {
                    "id": 0,
                    "is_bot": false,
                    "first_name": "",
                    "last_name": "",
                    "language_code": ""
                },
                "chat": {
                    "id": 0,
                    "first_name": "",
                    "last_name": "",
                    "type": ""
                },
                "date": 0,
                "text": ""
            }
        }
    ]
}
```
{% endcode %}

## 📩 Bot ile Mesaj Gönderme

```javascript
import requests

def telegram_bot_sendtext(bot_message):

   bot_token = "1306224394:AAFUBwGCciNOiOQQQz0j9YNb5OniwEPfsHg"
   bot_chatID = '431846525'
   send_text = 'https://api.telegram.org/bot' + bot_token \
      + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' \
      + bot_message

   response = requests.get(send_text)

   return response.json()


test = telegram_bot_sendtext("Testing Telegram bot")
print(test)
```

## 📦 Hazır Paketler ile Telegram Yönetimi

```javascript
import logging

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

BOT_TOKEN = "Token değerini buraya atayın"

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    # update.message.text
    update.message.reply_text("/mekan_ekle ile mekan ekleyin")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

```

