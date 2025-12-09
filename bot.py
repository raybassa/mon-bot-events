import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = os.getenv('TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [[InlineKeyboardButton("TUTO", callback_data='t')], [InlineKeyboardButton("EVENEMENT", callback_data='e')], [InlineKeyboardButton("REDIFF", url="https://t.me/test")], [InlineKeyboardButton("TIP", callback_data='tip')]]
    await update.message.reply_text("Menu :", reply_markup=InlineKeyboardMarkup(kb))

async def btn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    if q.data == 't':
        await q.edit_message_text("TUTO: Clique EVENEMENT pour voir les liens")
    elif q.data == 'e':
        kb = [[InlineKeyboardButton("UFC", url="https://exemple.com")], [InlineKeyboardButton("Foot", url="https://exemple.com")], [InlineKeyboardButton("Retour", callback_data='r')]]
        await q.edit_message_text("Evenements :", reply_markup=InlineKeyboardMarkup(kb))
    elif q.data == 'tip':
        kb = [[InlineKeyboardButton("5 euros", callback_data='tp5')], [InlineKeyboardButton("10 euros", callback_data='tp10')], [InlineKeyboardButton("Retour", callback_data='r')]]
        await q.edit_message_text("Merci !", reply_markup=InlineKeyboardMarkup(kb))
    elif q.data.startswith('tp'):
        await q.edit_message_text("Merci pour ton tip !")
    elif q.data == 'r':
        kb = [[InlineKeyboardButton("TUTO", callback_data='t')], [InlineKeyboardButton("EVENEMENT", callback_data='e')], [InlineKeyboardButton("REDIFF", url="https://t.me/test")], [InlineKeyboardButton("TIP", callback_data='tip')]]
        await q.edit_message_text("Menu :", reply_markup=InlineKeyboardMarkup(kb))

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(btn))

if __name__ == '__main__':
    app.run_polling()
