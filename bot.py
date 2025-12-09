import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = os.getenv('TOKEN')
REDIFF_LINK = "https://t.me/+1wIOqGBFY9s5ZTk0"
REVOLUT_LINK = "https://revolut.me/tonusername"  # À remplacer par ton lien Revolut
WALLET_LINK = "https://t.me/tonbot?start=wallet"  # Ton wallet Telegram

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [
        [InlineKeyboardButton("📺 TUTO", callback_data='tuto'), InlineKeyboardButton("🔙 RETOUR", callback_data='menu')],
        [InlineKeyboardButton("🎬 EVENEMENTS", callback_data='eve'), InlineKeyboardButton("🔙 RETOUR", callback_data='menu')],
        [InlineKeyboardButton("🔄 REDIFF", url=REDIFF_LINK), InlineKeyboardButton("💰 DON", callback_data='don')],
    ]
    await update.message.reply_text("⚽ LIEN SPORT DU JOUR ⚽

Bienvenue ! Choisis une option :", reply_markup=InlineKeyboardMarkup(kb))

async def tuto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tuto_text = """🎓 TUTO DE LA DEBROUILLE 🎓

📱 **ÉTAPE 1 : Installer un ANTI-PUB**
• AdGuard (meilleur)
• Brave Browser (gratuit)
• AdBlock Plus
→ Essentiel pour éviter les pop-ups !

🌐 **ÉTAPE 2 : Sites gratuits sans inscription**
• PPV.TO → Tous les sports (Football, UFC, Boxe, etc)
  Cherche ton sport → sélectionne l'événement

🚀 **ÉTAPE 3 : LA SOLUTION ULTIME → LOKKE**
• Télécharge : https://www.lokke.app/download
• Dispo sur : Android, Amazon, Windows, Mac, Linux
• Fonctionnement ultra simple :
  1. Ouvre l'app Lokke
  2. Va dans "Live TV"
  3. Cherche la chaîne que tu veux
  4. C'EST TOUT ! 🎉

💡 **CONSEIL** : Lokke = la meilleure solution (libre, rapide, sans pub)

📌 **AUTRES SITES** :
• StreamFactory
• Wiziwig
• CricFree

✨ Bon visionnage ! 🎬"""
    kb = [[InlineKeyboardButton("🔙 RETOUR", callback_data='menu')]]
    await update.callback_query.edit_message_text(tuto_text, reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

async def evenements(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # À personnaliser avec tes événements du jour
    eve_text = """🎬 EVENEMENTS DISPONIBLES AUJOURD'HUI 🎬

📅 **9 DÉCEMBRE 2025**

⚽ **FOOTBALL**
• 21h00 - PSG vs OM - Ligue 1
• 20h00 - Real Madrid vs Barcelone - La Liga

🥊 **BOXE**
• 22h00 - Tyson Fury vs Oleksandr Usyk II

🤼 **UFC**
• 17h00 - UFC Paris 17 - Main Card
• 04h00 - UFC Las Vegas

🏀 **BASKET**
• 02h00 - Lakers vs Celtics NBA

📺 **AUTRES**
• 19h30 - Wimbledon Tennis
• 15h00 - MotoGP"""
    kb = [[InlineKeyboardButton("🔙 RETOUR", callback_data='menu')]]
    await update.callback_query.edit_message_text(eve_text, reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

async def don(update: Update, context: ContextTypes.DEFAULT_TYPE):
    don_text = """💰 SOUTIENS NOTRE CANAL 💰

Merci de nous aider à maintenir le service 24/7 !

Choisis ton moyen de paiement préféré :"""
    kb = [
        [InlineKeyboardButton("💳 REVOLUT", url=REVOLUT_LINK)],
        [InlineKeyboardButton("👛 WALLET TELEGRAM", url=WALLET_LINK)],
        [InlineKeyboardButton("⭐ STARS (Telegram)", callback_data='stars')],
        [InlineKeyboardButton("🔙 RETOUR", callback_data='menu')],
    ]
    await update.callback_query.edit_message_text(don_text, reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [
        [InlineKeyboardButton("📺 TUTO", callback_data='tuto'), InlineKeyboardButton("🔙 RETOUR", callback_data='menu')],
        [InlineKeyboardButton("🎬 EVENEMENTS", callback_data='eve'), InlineKeyboardButton("🔙 RETOUR", callback_data='menu')],
        [InlineKeyboardButton("🔄 REDIFF", url=REDIFF_LINK), InlineKeyboardButton("💰 DON", callback_data='don')],
    ]
    await update.callback_query.edit_message_text("⚽ LIEN SPORT DU JOUR ⚽

Choisis une option :", reply_markup=InlineKeyboardMarkup(kb))

async def stars(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.edit_message_text("⭐ Les Telegram Stars sont disponibles directement dans Telegram !

Envoie /donate pour faire un don via les étoiles.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 RETOUR", callback_data='don')]]))

async def btn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    if q.data == 'tuto':
        await tuto(update, context)
    elif q.data == 'eve':
        await evenements(update, context)
    elif q.data == 'don':
        await don(update, context)
    elif q.data == 'menu':
        await menu(update, context)
    elif q.data == 'stars':
        await stars(update, context)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(btn))

if __name__ == '__main__':
    app.run_polling()
