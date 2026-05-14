import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_TOKEN = "YOUR_BOT_TOKEN"

API_KEY = "f88b5332980e46a56fd129141c13e1e34355c19b"

async def lookup_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = update.message.text.strip()

    api_url = f"https://api.lookupnow.top/api/v1/query.php?key={API_KEY}&number={number}"

    try:
        response = requests.get(api_url)
        data = response.json()

        if data["status"] == "success":
            info = data["data"]

            msg = f"""
╭─── 🔍 LOOKUP RESULT
│
├ 👤 Name: {info.get('name', 'N/A')}
├ 📱 Number: {info.get('international_format', 'N/A')}
├ 🌍 Country: {info.get('country', 'N/A')}
├ 📡 Carrier: {info.get('carrier', 'N/A')}
├ 🏷 Type: {info.get('type', 'N/A')}
│
╰── 👨‍💻 Dev: ACS TANVIR AHMED
"""

        else:
            msg = "❌ Number information not found."

    except Exception as e:
        msg = f"❌ Error: {e}"

    await update.message.reply_text(msg)

# Bot setup
app = Application.builder().token(BOT_TOKEN).build()

# Any text message handler
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, lookup_number))

print("Bot Running...")
app.run_polling()
