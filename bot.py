import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = os.getenv('TOKEN')
REDIFF_LINK = "https://t.me/+1wIOqGBFY9s5ZTk0"
REVOLUT_LINK = "https://revolut.me/tonnom"
WALLET_LINK = "https://t.me/tonbot"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [[InlineKeyboardButton("TUTO", callback_data='tuto'), InlineKeyboardButton("RETOUR", callback_data='menu')], [InlineKeyboardButton("EVENEMENTS", callback_data='eve'), InlineKeyboardButton("RETOUR", callback_data='menu')], [InlineKeyboardButton("REDIFF", url=REDIFF_LINK), InlineKeyboardButton("DON", callback_data='don')]]
    await update.message.reply_text("LIEN SPORT DU JOUR

Choisis une option :", reply_markup=InlineKeyboardMarkup(kb))

async def tuto(q):
    txt = "TUTO DE LA DEBROUILLE

1. ANTI-PUB: AdGuard ou Brave
2. SITES: PPV.TO
3. MEILLEURE SOLUTION: LOKKE (https://www.lokke.app/download)
   - Ouvre l'app
   - Live TV
   - Cherche la chaine
   - C'est tout!

AUTRES SITES: StreamFactory, Wiziwig, CricFree"
    kb = [[InlineKeyboardButton("RETOUR", callback_data='menu')]]
    await q.edit_message_text(txt, reply_markup=InlineKeyboardMarkup(kb))

async def eve(q):
    txt = "EVENEMENTS DISPONIBLES

9 DECEMBRE 2025

FOOTBALL:
21h00 - PSG vs OM
20h00 - Real vs Barca

BOXE:
22h00 - Tyson vs Usyk

UFC:
17h00 - UFC Paris

BASKET:
02h00 - Lakers vs Celtics"
    kb = [[InlineKeyboardButton("RETOUR", callback_data='menu')]]
    await q.edit_message_text(txt, reply_markup=InlineKeyboardMarkup(kb))

async def don(q):
    txt = "SOUTIENS NOTRE CANAL

Choisis ton moyen de paiement:"
    kb = [[InlineKeyboardButton("REVOLUT", url=REVOLUT_LINK)], [InlineKeyboardButton("WALLET TELEGRAM", url=WALLET_LINK)], [InlineKeyboardButton("STARS", callback_data='stars')], [InlineKeyboardButton("RETOUR", callback_data='menu')]]
    await q.edit_message_text(txt, reply_markup=InlineKeyboardMarkup(kb))

async def menu(q):
    kb = [[InlineKeyboardButton("TUTO", callback_data='tuto'), InlineKeyboardButton("RETOUR", callback_data='menu')], [InlineKeyboardButton("EVENEMENTS", callback_data='eve'), InlineKeyboardButton("RETOUR", callback_data='menu')], [InlineKeyboardButton("REDIFF", url=REDIFF_LINK), InlineKeyboardButton("DON", callback_data='don')]]
    await q.edit_message_text("LIEN SPORT DU JOUR

Choisis une option :", reply_markup=InlineKeyboardMarkup(kb))

async def stars(q):
    kb = [[InlineKeyboardButton("RETOUR", callback_data='don')]]
    await q.edit_message_text("Envoie /donate pour faire un don via les Telegram Stars", reply_markup=InlineKeyboardMarkup(kb))

async def btn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    if q.data == 'tuto':
        await tuto(q)
    elif q.data == 'eve':
        await eve(q)
    elif q.data == 'don':
        await don(q)
    elif q.data == 'menu':
        await menu(q)
    elif q.data == 'stars':
        await stars(q)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(btn))

if __name__ == '__main__':
    app.run_polling()
