import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

SMALL_CAPS_MAP = {
    "a": "ᴀ","b": "ʙ","c": "ᴄ","d": "ᴅ","e": "ᴇ","f": "ꜰ","g": "ɢ",
    "h": "ʜ","i": "ɪ","j": "ᴊ","k": "ᴋ","l": "ʟ","m": "ᴍ","n": "ɴ",
    "o": "ᴏ","p": "ᴘ","q": "q","r": "ʀ","s": "ꜱ","t": "ᴛ","u": "ᴜ",
    "v": "ᴠ","w": "ᴡ","x": "x","y": "ʏ","z": "ᴢ",
}

def to_small_caps(text: str) -> str:
    return "".join(SMALL_CAPS_MAP.get(c.lower(), c) for c in text)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me text to convert 😎")

async def convert_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        converted = to_small_caps(update.message.text)
        await update.message.reply_text(converted)

async def main():
    BOT_TOKEN = "8745249835:AAGYyqJMyIQEaS5S1agSoj68Xa10S47e7dM"  # ⚠️ token yaha daal

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, convert_text_message))

    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
