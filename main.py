import telebot
import http.server
import socketserver
import threading
import os

# 1. RENDER ӨЧҮРҮП САЛБАШЫ ҮЧҮН ЖАСАЛМА СЕРВЕР
def run_dummy_server():
    PORT = int(os.environ.get("PORT", 8080))
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

threading.Thread(target=run_dummy_server, daemon=True).start()

# 2. БОТТУН ТОКЕНИ
API_TOKEN = "8214859958:AAHz1JKP_ylFjmjOUK42UMgA4xE_hR0gMq8"
bot = telebot.TeleBot(API_TOKEN)

# 3. БИР ГАНА ТОЧКАГА ЖООП БЕРҮҮ
@bot.message_handler(func=lambda message: message.text == ".")
def handle_dot_message(message):
    text = (
        "Салам! Мен <b>𝐊𝐆𝐙🇰🇬 𝐙𝐄𝐑𝐎</b> группасынын ботумун! 🤖\n\n"
        "✨ <b>Биздин группа:</b> таанышуу жана сырдашуу максатында ачылды.\n"
        "👥 <b>Сураныч:</b> Кирип, адам кошуп, бизди колдоп бериңиздер!\n\n"
        "👑 <b>Владелец:</b> <a href='tg://user?id=6643265773'>ARGEN</a>\n\n"
        "<i>Кош келиңиздер!</i>"
    )
    bot.send_message(message.chat.id, text, parse_mode='HTML')

if __name__ == "__main__":
    print("Бот иштеп жатат. Точканы күтүүдө...")
    bot.infinity_polling()
