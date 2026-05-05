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

# 2. ЖАҢЫ БОТ ТОКЕНИ
API_TOKEN = "8501525188:AAGYwiiBE_Mi9unRT93jF74iSUh4jv9_qPw"
bot = telebot.TeleBot(API_TOKEN)

# 3. ЖООП БЕРҮҮЧҮ ФУНКЦИЯ
@bot.message_handler(func=lambda message: message.text is not None and (
    "группа" in message.text.lower() or 
    message.text == "/my" or 
    message.text == "."
))
def send_korolevskie_info(message):
    text = (
        "✨ <b>Салам Алейкум!</b> ✨\n\n"
        "🏰 Биздин <b>𝑲 𝑶 𝑹 𝑶 𝑳 𝑬 𝑽 𝑺 𝑲 𝑰 𝑬</b> группабызга кош келиңиз!\n\n"
        "🤝 Группа таанышуу жана достошуу максатында ачылган.\n"
        "☕ Келип олтуруп, көңүл ачып кетиңиздер! 😊\n\n"
        "🧕🏻 <b>Владелецка:</b> <a href='https://t.me/korolevsken'>NURI</a>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "👑 <b>𝑲 𝑶 𝑹 𝑶 𝑳 𝑬 𝑽 𝑺 𝑲 𝑰 𝑬</b>\n\n"
        "🔗 https://t.me/korolevsken"
    )
    bot.send_message(message.chat.id, text, parse_mode='HTML', disable_web_page_preview=False)

if __name__ == "__main__":
    print("Бот жаңы токен менен иштеп жатат...")
    bot.infinity_polling()
  
