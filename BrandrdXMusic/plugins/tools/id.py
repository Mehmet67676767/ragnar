from BrandrdXMusic import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        button = InlineKeyboardButton("✯ Kapat ✯", callback_data="close")
        markup = InlineKeyboardMarkup([[button]])
        message.reply_text(
            f"Kullanıcı {reply.from_user.first_name} ID'si: `{reply.from_user.id}`",
            reply_markup=markup
        )
    else:
        button = InlineKeyboardButton("✯ Kapat ✯", callback_data="close")
        markup = InlineKeyboardMarkup([[button]])
        message.reply(
           f"Bu grubun ID'si: `{message.chat.id}`",
           reply_markup=markup
        )