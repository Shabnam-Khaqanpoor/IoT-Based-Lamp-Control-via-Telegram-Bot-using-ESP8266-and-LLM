from telegram.ext import ApplicationBuilder

def main():
    TELEGRAM_BOT_TOKEN = "" #put your own token

    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    print("Bot started...\nPlease search @aiot8266bot in your telegram account.")    #you can change the ID of the bot

if __name__ == '__main__':
    main()