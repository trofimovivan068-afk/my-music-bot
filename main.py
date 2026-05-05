import telebot
import google.generativeai as genai
import os

# Render'деги Environment Variables'ден алат
API_TOKEN = os.getenv("BOT_TOKEN")
AI_KEY = os.getenv("AI_KEY")

genai.configure(api_key=AI_KEY)
model = genai.GenerativeModel('gemini-pro')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    if "аниса" in text:
        query = text.replace("аниса", "").strip()
        if not query:
            bot.reply_to(message, "Ооба, угуп жатам? 😊")
            return
        try:
            prompt = f"Сен Аниса аттуу кыргыз кызысың. Арген аттуу колдонуучу менен жылуу баарлаш: {query}"
            res = model.generate_content(prompt)
            bot.reply_to(message, res.text)
        except:
            bot.reply_to(message, "Бир аз ойлонуп калдым... ✨")

if __name__ == "__main__":
    bot.infinity_polling()
