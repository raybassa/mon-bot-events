import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("TUTO", callback_data='tuto'), InlineKeyboardButton("RETOUR", callback_data='start')],
        [InlineKeyboardButton("EVENTS", callback_data='events'), InlineKeyboardButton("RETOUR", callback_data='start')],
        [InlineKeyboardButton("REDIFF", url="https://t.me/+1wIOqGBFY9s5ZTk0"), InlineKeyboardButton("DON", callback_data='don')]
    ]
    await update.message.reply_text("LIEN SPORT DU JOUR

Choisis une option:", reply_markup=InlineKeyboardMarkup(keyboard))

async def button(update, context):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'tuto':
        text = "TUTO DEBROUILLE

1. Anti-pub: AdGuard
2. PPV.TO
3. LOKKE"
        keyboard = [[InlineKeyboardButton("RETOUR", callback_data='start')]]
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == 'events':
        text = "EVENTS 9 DEC

FOOTBALL: 21h PSG-OM
UFC: 17h UFC Paris
BOXE: 22h Tyson-Usyk"
        keyboard = [[InlineKeyboardButton("RETOUR", callback_data='start')]]
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == 'don':
        text = "SOUTIENS NOUS

Choisis:"
        keyboard = [[InlineKeyboardButton("Revolut", url="https://revolut.me/tonnom")], [InlineKeyboardButton("Wallet", url="https://t.me/tonbot")], [InlineKeyboardButton("RETOUR", callback_data='start')]]
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == 'start':
        keyboard = [
            [InlineKeyboardButton("TUTO", callback_data='tuto'), InlineKeyboardButton("RETOUR", callback_data='start')],
            [InlineKeyboardButton("EVENTS", callback_data='events'), InlineKeyboardButton("RETOUR", callback_data='start')],
            [InlineKeyboardButton("REDIFF", url="https://t.me/+1wIOqGBFY9s5ZTk0"), InlineKeyboardButton("DON", callback_data='don')]
        ]
        await query.edit_message_text("LIEN SPORT DU JOUR

Choisis une option:", reply_markup=InlineKeyboardMarkup(keyboard))

if __name__ == '__main__':
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()
