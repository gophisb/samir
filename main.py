
   import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ أهلاً بك في متجر سمير الإلكتروني! 🛍️\nللطلب أو الاستفسار، يرجى إرسال رسالتك.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    print("البوت يعمل بنجاح على السحابة...")
    application.run_polling()
