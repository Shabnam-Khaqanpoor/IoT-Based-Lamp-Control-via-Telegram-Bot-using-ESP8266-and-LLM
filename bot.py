from telegram.ext import ApplicationBuilder ,MessageHandler,ContextTypes, filters
from telegram import Update


ESP8266_IP = "" #put your own IP
ESP8266_PORT = 80
AUTHORIZED_CHAT_IDS = [] #add IDs to this list

async def send_to_esp8266_aiohttp(message: str) -> str:
    pass

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    user_chat_id = update.message.chat_id

    if user_chat_id in AUTHORIZED_CHAT_IDS:
        print(f"Message from {user_chat_id}: {user_message}")

        esp8266_response = await send_to_esp8266_aiohttp(user_message)

        await update.message.reply_text(f"ESP8266 Response: {esp8266_response}")
    else:
        await update.message.reply_text(f"Unauthorized access. You are not allowed to send commands.\nYour ID: {user_chat_id}")
def main():
    TELEGRAM_BOT_TOKEN = "" #put your own token

    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    print("Bot started...\nPlease search @aiot8266bot in your telegram account.")    #you can change the ID of the bot
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()
if __name__ == '__main__':
    main()