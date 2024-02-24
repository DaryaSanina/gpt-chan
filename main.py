from telegram.ext import filters, ApplicationBuilder, CommandHandler, MessageHandler
from dotenv import load_dotenv
import os
import sys

import gpt_queries
import voice_input
import text_to_speech
import telegram_bot

OPENAI_API_KEY = ""
ELEVEN_LABS_API_KEY = ""
TELEGRAM_BOT_TOKEN = ""

# Get API keys
path = os.path.join(os.path.dirname(__file__), '.env')  # Path to .env file (in the same directory as this code)
if os.path.exists(path):  # If the .env file exists
    load_dotenv(path)
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')  # Get the OpenAI API key
    ELEVEN_LABS_API_KEY = os.environ.get('ELEVEN_LABS_API_KEY')  # Get the ElevenLabs API key
    TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')  # Get the Telegram bot token
else:
    print("No .env file")
    sys.exit()

if __name__ == '__main__':
    gpt_queries.load_api(OPENAI_API_KEY)  # Load the OpenAI API key

    text_to_speech.load_api(ELEVEN_LABS_API_KEY, 'Domi')  # Load the ElevenLabs API key

    # Build the Telegram app
    telegram_app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    start_handler = CommandHandler('start', telegram_bot.start)
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), telegram_bot.answer)
    telegram_app.add_handler(start_handler)
    telegram_app.add_handler(message_handler)

    telegram_app.run_polling()
