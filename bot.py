import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')
BOT_USERNAME = "ton_bot_username"
REDIFF_CHANNEL = "https://t.me/nom_de_ton_canal"
TUTO_TV_MESSAGE = """
📺 **TUTO TV** 📺

Voici comment regarder les événements :

1️⃣ **Clique sur le bouton ÉVÉNEMENT** pour voir les liens
2️⃣ **Sélectionne l'événement** que tu veux regarder
3️⃣ **Appuie sur le lien** pour accéder au stream
4️⃣ **Profite du match !** 🍿

**💡 Conseil :** Si le stream lag, actualise la page
**❓ Problème ?** Rejoins notre canal REDIFF pour les alternatives

Bon visionnage ! 🎉
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📺 TUTO TV", callback_data='tuto')],
        [InlineKeyboardButton("🎬 ÉVÉNEMENT", callback_data='evenement')],
        [InlineKeyboardButton("🔄 REDIFF", url=REDIFF_CHANNEL)],
        [InlineKeyboardButton("❤️ REMERCIEMENT (Tip)", callback_data='tips')],
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🎉 Bienvenue !

"
        "Choisis ce que tu veux faire :",
        reply_markup=reply_markup
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'tuto':
        await query.edit_message_text(
            text=TUTO_TV_MESSAGE,
            parse_mode='Markdown'
        )
    
    elif query.data == 'evenement':
        keyboard = [
            [InlineKeyboardButton("🔴 UFC 304 EN DIRECT", url="https://exemple.com/ufc")],
            [InlineKeyboardButton("⚽ Match Football Live", url="https://exemple.com/foot")],
            [InlineKeyboardButton("🥊 Boxe - Stream HD", url="https://exemple.com/boxe")],
            [InlineKeyboardButton("🏋️ Catch WrestleEvent", url="https://exemple.com/catch")],
            [InlineKeyboardButton("◀️ Retour au menu", callback_data='retour')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            text="📺 Voici les événements disponibles en ce moment :

Clique sur l'événement pour le regarder !",
            reply_markup=reply_markup
        )
    
    elif query.data == 'tips':
        keyboard = [
            [InlineKeyboardButton("💰 Envoyer un Tip (5€)", callback_data='tip_5')],
            [InlineKeyboardButton("💰 Envoyer un Tip (10€)", callback_data='tip_10')],
            [InlineKeyboardButton("💰 Envoyer un Tip (25€)", callback_data='tip_25')],
            [InlineKeyboardButton("◀️ Retour au menu", callback_data='retour')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            text="❤️ **Merci de soutenir le canal !**

"
                 "Ton soutien nous aide à offrir du meilleur contenu.
"
                 "Choisis un montant :",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif query.data.startswith('tip_'):
        amount = query.data.split('_')[1]
        user_first_name = query.from_user.first_name
        
        await query.edit_message_text(
            text=f"❤️ Merci {user_first_name} !

"
                 f"Ton tip de {amount}€ a été reçu avec gratitude 🙏

"
                 f"Tu aides à maintenir le service en ligne 24/7 !

"
                 f"Si tu veux officialiser via le Telegram Wallet :
"
                 f"Utilise : /pay {amount}"
        )
    
    elif query.data == 'retour':
        keyboard = [
            [InlineKeyboardButton("📺 TUTO TV", callback_data='tuto')],
            [InlineKeyboardButton("🎬 ÉVÉNEMENT", callback_data='evenement')],
            [InlineKeyboardButton("🔄 REDIFF", url=REDIFF_CHANNEL)],
            [InlineKeyboardButton("❤️ REMERCIEMENT (Tip)", callback_data='tips')],
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            text="🎉 Bienvenue !

Choisis ce que tu veux faire :",
            reply_markup=reply_markup
        )

async def evenement_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔴 UFC 304 EN DIRECT", url="https://exemple.com/ufc")],
        [InlineKeyboardButton("⚽ Match Football Live", url="https://exemple.com/foot")],
        [InlineKeyboardButton("🥊 Boxe - Stream HD", url="https://exemple.com/boxe")],
        [InlineKeyboardButton("🏋️ Catch WrestleEvent", url="https://exemple.com/catch")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        text="📺 Voici les événements disponibles :",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("evenement", evenement_command))
    app.add_handler(CallbackQueryHandler(button_callback))
    
    print("✅ Bot lancé ! Il tournera 24/24 sur Render...")
    app.run_polling()

if __name__ == '__main__':
    main()
