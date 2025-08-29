import asyncio

from BrandrdXMusic import app
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME


@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video="https://graph.org/file/e999c40cb700e7c684b75.mp4",
        caption=(
            f"❤️ Merhaba {message.from_user.mention}\n\n"
            f"🔮 Ben {MUSIC_BOT_NAME}\n\n"
            "✨ Hızlı ve güçlü bir müzik oynatma botuyum; harika özelliklerle donatıldım.\n\n"
            "💫 Herhangi bir sorunuz varsa kanalımızı ziyaret edebilirsiniz.\n\n"
            "━━━━━━━━━━━━━━━━━━❄"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="☆ Kanal 💗", url="https://t.me/the_team_kumsal"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="✯ Kapat ✯", callback_data="close"
                    )
                ],
            ]
        ),
    )