# Telegram Small Caps Bot (Python)

A Telegram bot that converts normal text into a small caps Unicode style.

## Features

- Uses `python-telegram-bot`
- Responds to any text message
- Converts letters to small caps Unicode
- Keeps numbers, spaces, and special characters unchanged
- `/start` command replies with: `Send me text to convert 😎`
- Async handlers (`async def`) for bot commands/messages

## 1) Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 2) Configure bot token

1. Create a bot with [@BotFather](https://t.me/BotFather)
2. Copy your bot token
3. Open `bot.py` and replace:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
```

with your real token.

## 3) Run the bot

```bash
python bot.py
```

When the bot is running, send `/start` or any text message in Telegram.

## Notes

- Mapping follows the exact requested conversion:
  - `a → ᴀ, b → ʙ, c → ᴄ, d → ᴅ, e → ᴇ, f → ꜰ, g → ɢ, h → ʜ, i → ɪ, j → ᴊ, k → ᴋ, l → ʟ, m → ᴍ, n → ɴ, o → ᴏ, p → ᴘ, q → q, r → ʀ, s → ꜱ, t → ᴛ, u → ᴜ, v → ᴠ, w → ᴡ, x → x, y → ʏ, z → ᴢ`
- Uppercase letters are also converted by first lowercasing each character.

## Optional extension ideas

- Add `/style` command for `small caps`, `bold`, `fancy`
- Add inline keyboard buttons to choose style per message
