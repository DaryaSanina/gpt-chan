from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

import gpt_queries


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    This function starts when the user enters the "/start" command
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=gpt_queries.greet())


async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    response = gpt_queries.answer(query)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
