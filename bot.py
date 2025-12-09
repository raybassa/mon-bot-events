import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = os.getenv('TOKEN')

async def start(update, context):
    kb = [[InlineKeyboardButton("TUTO", callback_data='tuto'), InlineKeyboardButton("RETOUR", callback_data='menu')], [InlineKeyboardButton("EVENEMENTS", callback_data='eve'), InlineKeyboardButton("RETOUR", callback_data='menu')], [InlineKeyboardButton("REDIFF", url="https://t.me/+1wIOqGBFY9s5ZTk0"), InlineKeyboardButton("DON", callback_data='don')]]
    await update.message.reply_text("LIEN SPORT DU JOUR

Choisis :", reply_markup=InlineKeyboardMarkup(kb))

async def handle_buttons(update, context):
    q = update.callback_query
    await q.answer()
    
    if q.data == 'tuto':
        txt = "TUTO DEBROUILLE

1. Anti-pub: AdGuard
2. Sites: PPV.TO
3. LOKKE: https://www.lokke.app/download"
        kb = [[InlineKeyboardButton("RETOUR", callback_data='menu')]]
        await q.edit_message_text(txt, reply_markup=InlineKeyboardMarkup(kb))
    
    elif q.data == 'eve':
        txt = "EVENEMENTS 9 DEC

FOOTBALL: 21h PSG-OM
UFC: 17h UFC Paris
BOXE: 22h Tyson-Usyk"
        kb = [[InlineKeyboardButton("RETOUR", callback_data='menu')]]
        await q.edit_message_text(txt, reply_markup=InlineKeyboardMarkup(kb))
    
    elif q.data == 'don':
        txt = "SOUTIENS NOUS

Choisis:"
        kb = [[InlineKeyboardButton("Revolut", url="https://revolut.me/tonnom")], [InlineKeyboardButton("Wallet", url="https://t.me/tonbot")], [InlineKeyboardButton("RETOUR", callback_data='menu')]]
        await q.edit_message_text(txt, reply_markup=InlineKeyboardMarkup(kb))
    
    elif q.data == 'menu':
        kb = [[InlineKeyboardButton("TUTO", callback_data='tuto'), InlineKeyboardButton("RETOUR", callback_data='menu')], [InlineKeyboardButton("EVENEMENTS", callback_data='eve'), InlineKeyboardButton("RETOUR", callback_data='menu')], [InlineKeyboardButton("REDIFF", url="https://t.me/+1wIOqGBFY9s5ZTk0"), InlineKeyboardButton("DON", callback_data='don')]]
        await q.edit_message_text("LIEN SPORT DU JOUR

Choisis :", reply_markup=InlineKeyboardMarkup(kb))

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_buttons))
app.run_polling()
