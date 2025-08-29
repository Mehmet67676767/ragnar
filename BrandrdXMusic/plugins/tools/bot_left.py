import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import LOGGER_ID as LOG_GROUP_ID
from BrandrdXMusic import app
from BrandrdXMusic.utils.database import get_assistant, delete_served_chat

# Tek fotoğraf linki (gerekirse doğrudan görsel URL'siyle değiştirin)
photo = [
    "https://ibb.co/0jsDgHSj"
]


@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    try:
        userbot = await get_assistant(message.chat.id)

        left_chat_member = message.left_chat_member
        # Bot gruptan çıkarıldıysa/ayrıldıysa logla
        if left_chat_member and left_chat_member.id == (await app.get_me()).id:
            remove_by = (
                message.from_user.mention if message.from_user else "Bilinmeyen Kullanıcı"
            )
            title = message.chat.title
            username = (
                f"@{message.chat.username}" if message.chat.username else "Özel Sohbet"
            )
            chat_id = message.chat.id

            left = (
                "✫ <b><u>#GRUPTAN_AYRILDI</u></b> ✫\n\n"
                f"🔹 Sohbet Başlığı : {title}\n"
                f"🔹 Sohbet Türü    : {username}\n"
                f"🔹 Sohbet ID      : <code>{chat_id}</code>\n"
                f"🔹 Kimin Tarafından: {remove_by}\n"
                f"🔹 Bot            : @{app.username}"
            )

            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
            await delete_served_chat(chat_id)
            await userbot.leave_chat(chat_id)
    except Exception:
        return