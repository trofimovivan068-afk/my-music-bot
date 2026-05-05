import http.server
import socketserver
import threading
import telebot
import google.generativeai as genai
import os

# 1. RENDER ҮЧҮН ЖАСАЛМА ПОРТ АЧУУ (КАТА БОЛБОШУ ҮЧҮН)
def run_dummy_server():
    PORT = int(os.environ.get("PORT", 8080))
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Сервер {PORT} портунда иштеп жатат")
        httpd.serve_forever()

# Серверди фондо иштетүү
threading.Thread(target=run_dummy_server, daemon=True).start()

# 2. БОТТУН МААЛЫМАТТАРЫ
API_TOKEN = "8214859958:AAHz1JKP_ylFjmjOUK42UMgA4xE_hR0gMq8"
AI_KEY = "AIzaSyCPv-Ermo2mt56fpHD27swl3YCEvHp4QGs"

genai.configure(api_key=AI_KEY)
model = genai.GenerativeModel('gemini-pro')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Салам! Мен Анисамын. 🌸 Эми мен Render'де 24/7 иштейм. Жаза бериңиз!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text.lower()
    
    # "Аниса" деп кайрылса же жеке чатта жазса жооп берет
    if "аниса" in user_text or message.chat.type == "private":
        query = user_text.replace("аниса", "").strip()
        
        try:
            prompt = f"Сен Аниса аттуу кыргыз кызысың. Колдонуучуга абдан жылуу жана сылык жооп бер: {query if query else 'Салам'}"
            res = model.generate_content(prompt)
            bot.reply_to(message, res.text)
        except:
            bot.reply_to(message, "Бир аз ойлонуп калдым... ✨")

if __name__ == "__main__":
    print("Аниса ишке кирди...")
    bot.infinity_polling()
