import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    InputMediaVideo,
    Message,
)
from config import LOGGER_ID as LOG_GROUP_ID
from BrandrdXMusic import app
from BrandrdXMusic.core.userbot import Userbot
from BrandrdXMusic.utils.database import delete_served_chat
from BrandrdXMusic.utils.database import get_assistant


# Tüm fotoğraflar tek linke ayarlandı
photo = [
    "https://ibb.co/0jsDgHSj",
    "https://ibb.co/0jsDgHSj",
    "https://ibb.co/0jsDgHSj",
    "https://ibb.co/0jsDgHSj",
    "https://ibb.co/0jsDgHSj",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            # Bot gruba eklendiyse
            if members.id == (await app.get_me()).id:
                count = await app.get_chat_members_count(chat.id)
                username = message.chat.username if message.chat.username else "Özel Grup"
                msg = (
                    f"**📝 Müzik Botu Yeni Bir Gruba Eklendi (#NEW_GROUP)**\n\n"
                    f"**📌 Sohbet Adı:** {message.chat.title}\n"
                    f"**🍂 Sohbet ID:** {message.chat.id}\n"
                    f"**🔐 Sohbet Kullanıcı Adı:** @{username if message.chat.username else 'yok'}\n"
                    f"**📈 Grup Üye Sayısı:** {count}\n"
                    f"**🤔 Ekleyen:** {message.from_user.mention}"
                )
                await app.send_photo(
                    LOG_GROUP_ID,
                    photo=random.choice(photo),
                    caption=msg,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "😍 Ekleyen Kişi 😍",
                                    url=f"tg://openmessage?user_id={message.from_user.id}",
                                )
                            ]
                        ]
                    ),
                )
                # Kullanıcı adı varsa kullanıcı adıyla, yoksa yine de dene (orijinal mantık korunuyor)
                await userbot.join_chat(f"{username}")
    except Exception as e:
        print(f"Hata: {e}")