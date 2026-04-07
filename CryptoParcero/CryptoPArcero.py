from config import TELEGRAM_TOKEN
import telebot


class CryptoCompadre_Bot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.registrar_manejadores()

    # ------------------- HANDLERS -------------------

    def registrar_manejadores(self):

        @self.bot.message_handler(commands=["start", "inicio"])
        def comando_inicio(message):
            self.bienvenida_a_usuario(message)

        @self.bot.message_handler(commands=["compadre"])
        def comando_compadre(message):
            self.mostrar_menu_activos(message)


        @self.bot.message_handler(commands=["syp500"])
        def comando_syp500(message):
            self.bot.send_message(
                message.chat.id,
                "🏛️ Has seleccionado /syp500.\n\n(Aquí se mostrará el S&P 500 próximamente)"
            )

        @self.bot.message_handler(content_types=["text"])
        def manejar_texto(message):
            if message.text.startswith("/"):
                self.bot.send_message(message.chat.id, "❌ Comando incorrecto, compa.")
            else:
                self.bot.send_message(
                    message.chat.id,
                    "🤖 Solo me comunico con comandos. Usa /start para comenzar."
                )

    # ------------------- BIENVENIDA -------------------

    def bienvenida_a_usuario(self, message):
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

        btn1 = telebot.types.KeyboardButton("/compadre")
        btn2 = telebot.types.KeyboardButton("/syp500")

        markup.row(btn1, btn2)

        texto_bienvenida = (
            "🤠 ¡Hola, compadre! Soy tu CryptoCompadre!\n\n"
            "Por ahora puedes usar estas opciones:\n\n"
            "🔥 /compadre → Ver activos (próximamente)\n"
            "🏛️ /syp500 → Ver índice S&P 500 (próximamente)\n\n"
            "🚀 ¡Vamos a hacer esos números!"
        )

        self.bot.send_message(
            message.chat.id,
            texto_bienvenida,
            reply_markup=markup
        )

    def mostrar_menu_activos(self, message):  # 🔥 AQUÍ LO PEGAS
        markup = telebot.types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            one_time_keyboard=False
        )

        btn1 = telebot.types.KeyboardButton("BTC")
        btn2 = telebot.types.KeyboardButton("ETH")
        btn3 = telebot.types.KeyboardButton("AAPL")
        btn4 = telebot.types.KeyboardButton("TSLA")

        markup.row(btn1, btn2)
        markup.row(btn3, btn4)

        self.bot.send_message(
            message.chat.id,
            "📊 Selecciona un activo:",
            reply_markup=markup
        )



if __name__ == '__main__':
    bot = CryptoCompadre_Bot(TELEGRAM_TOKEN)  # creas el objeto
    print('iniciando el bot')
    bot.bot.infinity_polling()  # accedes al bot interno
    print('fin')










