from pyrogram import Client, filters
import random

# Tokat mesajları listesi
TOKAT_MESAJLARI = [
    "{tokatlayan}, eline terliği aldı ve {tokatlanan} kişisine sağlam bir tokat attı! 🩴😵",
    "{tokatlayan}, {tokatlanan} kişisini tokat manyağı yaptı! 🤜😤",
    "{tokatlayan}, sinirini {tokatlanan} üzerinden çıkardı! 😡👋",
    "{tokatlayan}, yavaşça yaklaştı... ve BAM! {tokatlanan} artık yok... 💥",
    "{tokatlayan}, tokadı yapıştırdı: {tokatlanan} şimdi sessiz modda. 🤫",
    "{tokatlayan}, {tokatlanan} kişisine dijital Osmanlı tokadı attı! 🧿",
]

@Client.on_message(filters.command("tokatla") & filters.group)
async def tokatla(client, message):
    tokatlayan = message.from_user.mention

    # Eğer birine cevap verilmişse o kişiyi tokatla
    if message.reply_to_message:
        tokatlanan = message.reply_to_message.from_user.mention
    elif len(message.command) > 1:
        tokatlanan = message.text.split(" ", 1)[1]
    else:
        # Hiç kimse belirtilmemişse rastgele bir kullanıcı seç
        tokatlanan = "gruptaki bilinmeyen biri"

    # Tokat mesajını seç ve gönder
    mesaj = random.choice(TOKAT_MESAJLARI).format(
        tokatlayan=tokatlayan,
        tokatlanan=tokatlanan
    )
    await message.reply(mesaj)
