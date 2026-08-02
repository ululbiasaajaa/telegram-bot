import os
from groq import Groq

# Token Telegram lu dari BotFather
TELEGRAM_TOKEN = '8922799030:AAGz_5O_QwEvJllkMACQGACWK4YvbVFON8E'

# API Key Groq (Gratis, nanti lu bisa ambil di console.groq.com)
# Untuk sementara lu bisa pakai kode uji coba ini atau daftar sendiri gratis
GROQ_API_KEY = os.getenv("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")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = Groq(api_key=GROQ_API_KEY)

# Perintah /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Yo! Bot AI udah aktif nih, bre. Mau ngobrol pake bahasa apa aja, gaul, Inggris, Jepang, gasss tanyain aja!")

# Handle semua pesan teks dan lempar ke AI
@bot.message_handler(func=lambda message: True)
def chat_with_ai(message):
    try:
        # Kasih tahu bot cara bertingkah laku lewat system prompt
        system_prompt = (
            "Lu adalah asisten AI yang santai, asik diajak ngobrol, pake bahasa gaul, "
            "tapi tetap cerdas dan menjawab pertanyaan user dengan akurat. "
            "Lu bisa nyesuaiin bahasa apa aja yang dipakai user (Inggris, Jepang, Spanyol, dll)."
        )

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Model AI gratis yang super pintar
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