import os
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# СЕНИН МААЛЫМАТТАРЫҢ
API_TOKEN = "8214859958:AAHz1JKP_ylFjmjOUK42UMgA4xE_hR0gMq8"
# API ачкычты Render'ден GEMINI_API_KEY деп кошсоң болот, же бул жерге түз чапта:
GEMINI_KEY = os.getenv("GEMINI_API_KEY") or "AIzaSyCPv-Ermo2mt56fpHD27swl3YCEvHp4QGs"

# Сүрөт (Сен жөнөткөн Анисанын сүрөтү)
PHOTO_URL = "https://raw.githubusercontent.com/Argen-Eclipse/AnisaBot/main/anisa.jpg" 

# AI жөндөө
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer_photo(
        PHOTO_URL, 
        caption="Салам! Мен Анисамын. 🌸\nМага сөзсүз 'Аниса' деп кайрылыңыз, ошондо мен сизге жооп берем. Сиз менен баарлашууга кубанычтамын!"
    )

@dp.message_handler()
async def talk(message: types.Message):
    text = message.text.lower()
    
    if "аниса" in text:
        prompt = text.replace("аниса", "").strip()
        
        if not prompt:
            await message.reply_photo(PHOTO_URL, caption="Угуп жатам? 😊")
            return

        try:
            # Анисанын мүнөзү
            ai_instruction = f"Сен - Анисасың. Абдан жагымдуу, акылдуу кыргыз кызысың. Колдонуучу сага мындай деди: '{prompt}'. Ага кыргызча абдан жылуу жооп бер."
            response = model.generate_content(ai_instruction)
            await message.reply(response.text)
        except Exception:
            await message.reply("Бир аз ойлонуп калдым... ✨")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
  
