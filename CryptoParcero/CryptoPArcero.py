from config import *
import telebot

bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=["start", "inicio"])
def cmd_start(message):
    """"""
    bot.reply_to(message, ""
                          "**¡Hola, compadre! Soy tu CryptoCompadre!** 🤠\n\n"
                          "Soy un bot financiero diseñado para darte **tres datos clave** sobre tus activos favoritos en un solo lugar:\n"
                          "1. **Precio Actual** 📈\n"
                          "2. **Últimas Noticias** 📰\n"
                          "3. **Gráfico Histórico** 📊\n\n"
                          "Usa el comando ** /compadre ** para elegir un activo de nuestro menú exclusivo.\n"
                          "O usa ** /syp500 ** para ver el índice bursátil más importante de USA.\n\n"
                          "**¡Vamos a hacer esos números!** 🚀"
                 )

if __name__ == '__main__':
    print('iniciando el bot')
    bot.infinity_polling()
    print('fin')













