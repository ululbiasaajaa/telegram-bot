import os
import telebot
from groq import Groq

TELEGRAM_TOKEN = '8922799030:AAGz_5O_QwEvJllkMACQGACWK4YvbVFON8E'
GROQ_API_KEY = "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"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = Groq(api_key=GROQ_API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Yo! Bot AI udah aktif nih, bre. Mau ngobrol pake bahasa apa aja, gaul, Inggris, Jepang, gasss tanyain aja!")

@bot.message_handler(func=lambda message: True)
def chat_with_ai(message):
    try:
        system_prompt = (
            "Lu adalah asisten AI yang santai, asik diajak ngobrol, pake bahasa gaul, "
            "tapi tetap cerdas dan menjawab pertanyaan user dengan akurat. "
            "Lu bisa nyesuaiin bahasa apa aja yang dipakai user (Inggris, Jepang, Spanyol, dll)."
        )

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message.text}
            ]
        )
        
        reply_text = response.choices[0].message.content
        bot.reply_to(message, reply_text)
        
    except Exception as e:
        bot.reply_to(message, f"Waduh bre, otaknya konslet dikit: {e}")

print("Bot AI sedang berjalan... Siap diajak gowes!")
bot.infinity_polling()