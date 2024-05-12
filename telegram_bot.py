from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from pathlib import Path

import gpt_queries
import text_to_speech


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    This function starts when the user enters the "/start" command
    """
    response = gpt_queries.greet()  # Generate a greeting
    voice_message_path = text_to_speech.generate_sound(response)  # Text to speech

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)  # Send the text message
    await context.bot.send_audio(chat_id=update.effective_chat.id, audio=voice_message_path)  # Send the voice message


async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    This function answers the user's message with another message and an audio version of the response
    """
    query = update.message.text  # Get the user's message
    response = gpt_queries.answer(query)  # Generate the response
    voice_message_path = text_to_speech.generate_sound(response)  # Text to speech

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)  # Send the text message
    await context.bot.send_audio(chat_id=update.effective_chat.id, audio=voice_message_path)  # Send the voice message

