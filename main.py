import http.server
import socketserver
import threading
import telebot
import google.generativeai as genai
import os

# Render үчүн порт
def run_dummy_server():
    PORT = int(os.environ.get("PORT", 8080))
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

threading.Thread(target=run_dummy_server, daemon=True).start()

# ТОКЕНДЕР
API_TOKEN = "8214859958:AAHz1JKP_ylFjmjOUK42UMgA4xE_hR0gMq8"
AI_KEY = "AIzaSyCPv-Ermo2mt56fpHD27swl3YCEvHp4QGs"

genai.configure(api_key=AI_KEY)
# Модельди 'gemini-1.5-flash' кылып өзгөрттүк (бул туруктуураак)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text.lower()
    
    if "аниса" in user_text or message.chat.type == "private":
        query = user_text.replace("аниса", "").strip()
        
        try:
            prompt = f"Сен Аниса аттуу кыргыз кызысың. Абдан жылуу жооп бер: {query if query else 'Салам'}"
            res = model.generate_content(prompt)
            bot.reply_to(message, res.text)
        except Exception as e:
            # Ката эмне экенин так көрүү үчүн:
            bot.reply_to(message, f"Ката чыкты: {str(e)[:50]}... Жаңы API Key керек окшойт.")

if __name__ == "__main__":
    bot.infinity_polling()
      
