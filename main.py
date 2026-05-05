import http.server
import socketserver
import threading
import telebot
import google.generativeai as genai
import os

# Render үчүн сервер
def run_dummy_server():
    PORT = int(os.environ.get("PORT", 8080))
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

threading.Thread(target=run_dummy_server, daemon=True).start()

# ТОКЕНДЕР
API_TOKEN = "8214859958:AAHz1JKP_ylFjmjOUK42UMgA4xE_hR0gMq8"
AI_KEY = "AIzaSyA9PRhWqTnIa9DF-EolqdD31hsm1IjBOvo"

genai.configure(api_key=AI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Анисанын жообу
        prompt = f"Сен Аниса аттуу кыргыз кызысың. Колдонуучунун аты Арген. Жылуу жооп бер: {message.text}"
        res = model.generate_content(prompt)
        
        if res.text:
            bot.reply_to(message, res.text)
        else:
            bot.reply_to(message, "AI жооп бере алган жок, бирок байланыш бар.")
            
    except Exception as e:
        # КАТАНЫ ТҮЗ ТЕЛЕГРАМГА ЧЫГАРУУ
        error_message = str(e)
        bot.reply_to(message, f"❌ Ката кетти: {error_message[:100]}")

if __name__ == "__main__":
    bot.infinity_polling()
