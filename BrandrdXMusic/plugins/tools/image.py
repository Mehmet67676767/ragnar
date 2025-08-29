import os
import shutil
from re import findall
from bing_image_downloader import downloader
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto, Message
from BrandrdXMusic import app

@app.on_message(filters.command(["imgs", "image"], prefixes=["/", "!"]))
async def google_img_search(client: Client, message: Message):
    chat_id = message.chat.id

    try:
        query = message.text.split(None, 1)[1]
    except IndexError:
        return await message.reply("Aramak için bir görsel sorgusu giriniz!")

    lim = findall(r"lim=\d+", query)
    try:
        lim = int(lim[0].replace("lim=", ""))
        query = query.replace(f"lim={lim}", "")
    except IndexError:
        lim = 5  # Varsayılan limit 5 görsel

    download_dir = "downloads"

    try:
        downloader.download(query, limit=lim, output_dir=download_dir, adult_filter_off=True, force_replace=False, timeout=60)
        images_dir = os.path.join(download_dir, query)
        if not os.listdir(images_dir):
            raise Exception("Hiç görsel indirilemedi.")
        lst = [os.path.join(images_dir, img) for img in os.listdir(images_dir)][:lim]  # Sadece lim kadar görsel al
    except Exception as e:
        return await message.reply(f"Görseller indirilirken hata oluştu: {e}")

    msg = await message.reply("🔍 Görseller aranıyor ve indiriliyor...")

    count = 0
    for img in lst:
        count += 1
        await msg.edit(f"✅ {count} görsel başarıyla indirildi...")

    try:
        await app.send_media_group(
            chat_id=chat_id,
            media=[InputMediaPhoto(media=img) for img in lst],
            reply_to_message_id=message.id
        )
        shutil.rmtree(images_dir)
        await msg.delete()
    except Exception as e:
        await msg.delete()
        return await message.reply(f"Görseller gönderilirken hata oluştu: {e}")