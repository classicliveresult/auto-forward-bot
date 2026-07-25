from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

TARGET_GROUPS = [
    -1001234567890,  # येथे Group ID टाका
]

async def auto_forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        for group in TARGET_GROUPS:
            try:
                await context.bot.copy_message(
                    chat_id=group,
                    from_chat_id=update.channel_post.chat.id,
                    message_id=update.channel_post.message_id
                )
            except Exception as e:
                print(e)

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, auto_forward))

print("Bot Started...")
app.run_polling()
