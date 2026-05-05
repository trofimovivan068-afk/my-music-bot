import http.server
import socketserver
import threading
import telebot
import google.generativeai as genai
import os

# 1. RENDER ҮЧҮН ЖАСАЛМА СЕРВЕР (КАТА БЕРБЕШ ҮЧҮН)
def run_dummy_server():
    PORT = int(os.environ.get("PORT", 8080))
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

# Серверди фондо иштетүү
threading.Thread(target=run_dummy_server, daemon=True).start()

# 2. ТОКЕНДЕР
API_TOKEN = "8214859958:AAHz1JKP_ylFjmjOUK42UMgA4xE_hR0gMq8"
AI_KEY = "AIzaSyA9PRhWqTnIa9DF-EolqdD31hsm1IjBOvo" # Жаңы ачкычың

genai.configure(api_key=AI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Салам, Арген! 😊 Мен Анисамын. Жаңы API ачкыч менен ишке кирдим, эми баарлаша берсек болот!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text
    
    try:
        # Анисанын мүнөзүн түзүү
        prompt = (
            f"Сен Аниса аттуу кыргыз кызысың. Колдонуучунун аты Арген. "
            f"Абдан жылуу, сылык жана акылдуу жооп бер. "
            f"Колдонуучу мындай деди: {user_text}"
        )
        res = model.generate_content(prompt)
        bot.reply_to(message, res.text)
    except Exception as e:
        # Эгер дагы деле бир нерсе туура эмес болсо, катаны так көрсөтөт
        bot.reply_to(message, f"Кечиресиз, кичине мүчүлүштүк болду... ✨")

if __name__ == "__main__":
    print("Аниса жаңы ачкыч менен иштеп жатат...")
    bot.infinity_polling()
