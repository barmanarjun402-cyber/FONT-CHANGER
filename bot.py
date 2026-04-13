"""
Telegram Small Caps Converter Bot

This bot listens for any text message and replies with the same text converted
into a small caps Unicode style. Numbers, spaces, and special characters are
left unchanged.
"""

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Mapping for lowercase alphabet -> small caps/fallback characters.
# Characters without a true Unicode small-caps equivalent use the requested fallback.
SMALL_CAPS_MAP = {
    "a": "ᴀ",
    "b": "ʙ",
    "c": "ᴄ",
    "d": "ᴅ",
    "e": "ᴇ",
    "f": "ꜰ",
    "g": "ɢ",
    "h": "ʜ",
    "i": "ɪ",
    "j": "ᴊ",
    "k": "ᴋ",
    "l": "ʟ",
    "m": "ᴍ",
    "n": "ɴ",
    "o": "ᴏ",
    "p": "ᴘ",
    "q": "q",
    "r": "ʀ",
    "s": "ꜱ",
    "t": "ᴛ",
    "u": "ᴜ",
    "v": "ᴠ",
    "w": "ᴡ",
    "x": "x",
    "y": "ʏ",
    "z": "ᴢ",
}


def to_small_caps(text: str) -> str:
    """
    Convert input text into small caps based on SMALL_CAPS_MAP.

    - Letters are converted case-insensitively.
    - Numbers, spaces, punctuation, and unsupported characters remain unchanged.
    """
    converted_chars = []

    for char in text:
        lower_char = char.lower()
        if lower_char in SMALL_CAPS_MAP:
            converted_chars.append(SMALL_CAPS_MAP[lower_char])
        else:
            converted_chars.append(char)

    return "".join(converted_chars)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command."""
    await update.message.reply_text("Send me text to convert 😎")


async def convert_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Convert any incoming text message to small caps and reply."""
    if update.message and update.message.text:
        converted = to_small_caps(update.message.text)
        await update.message.reply_text(converted)


def main() -> None:
    """
    Start the Telegram bot.

    Replace BOT_TOKEN with your token from @BotFather before running.
    """
    BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

    app = Application.builder().token(BOT_TOKEN).build()

    # Register command and message handlers.
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, convert_text_message))

    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()


if __name__ == "__main__":
    main()
