import os
import random
from datetime import datetime
from telegraph import upload_file
from PIL import Image, ImageDraw
from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import *

# BOT
from BrandrdXMusic import app
from BrandrdXMusic.mongo.couples_db import _get_image, get_couple  # (kullanıyorsan aktif et)

# Grup butonu (senin verdiğin link)
POLICE = [
    [
        InlineKeyboardButton(
            text="🌟 Sohbet Grubumuz",
            url="https://t.me/the_team_kumsal",
        ),
    ],
]


def dt():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    dt_list = dt_string.split(" ")
    return dt_list


def dt_tom():
    a = (
        str(int(dt()[0].split("/")[0]) + 1)
        + "/"
        + dt()[0].split("/")[1]
        + "/"
        + dt()[0].split("/")[2]
    )
    return a


tomorrow = str(dt_tom())
today = str(dt()[0])


@app.on_message(filters.command("couples"))
async def ctest(_, message):
    cid = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply_text("Bu komut yalnızca gruplarda çalışır.")
    try:
        # Kaydetme/okuma kullanacaksan alttakileri aç
        # is_selected = await get_couple(cid, today)
        # if not is_selected:
        msg = await message.reply_text("Çift görseli oluşturuluyor...")

        # Kullanıcı listesini al (botları hariç tut)
        list_of_users = []
        async for i in app.get_chat_members(message.chat.id, limit=50):
            if not i.user.is_bot:
                list_of_users.append(i.user.id)

        # Yeterli kullanıcı yoksa
        if len(list_of_users) < 2:
            await msg.edit("Yeterli kullanıcı yok. En az 2 gerçek kullanıcı gerekli.")
            return

        # Rastgele iki farklı kullanıcı seç
        c1_id = random.choice(list_of_users)
        c2_id = random.choice(list_of_users)
        while c1_id == c2_id:
            c1_id = random.choice(list_of_users)

        # Profil fotoğrafları ve isimler
        photo1 = (await app.get_chat(c1_id)).photo
        photo2 = (await app.get_chat(c2_id)).photo

        N1 = (await app.get_users(c1_id)).mention
        N2 = (await app.get_users(c2_id)).mention

        try:
            p1 = await app.download_media(photo1.big_file_id, file_name="pfp.png")
        except Exception:
            p1 = "BrandrdXMusic/assets/upic.png"
        try:
            p2 = await app.download_media(photo2.big_file_id, file_name="pfp1.png")
        except Exception:
            p2 = "BrandrdXMusic/assets/upic.png"

        # Görselleri işle
        img1 = Image.open(p1)
        img2 = Image.open(p2)
        # Arkaplan şablonu (mevcut dosya yoluna göre ayarla)
        img = Image.open("BrandrdXMusic/assets/cppicbranded.jpg")

        img1 = img1.resize((437, 437))
        img2 = img2.resize((437, 437))

        mask = Image.new("L", img1.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + img1.size, fill=255)

        mask1 = Image.new("L", img2.size, 0)
        draw = ImageDraw.Draw(mask1)
        draw.ellipse((0, 0) + img2.size, fill=255)

        img1.putalpha(mask)
        img2.putalpha(mask1)

        draw = ImageDraw.Draw(img)

        # Konumları şablona göre ayarla
        img.paste(img1, (116, 160), img1)
        img.paste(img2, (789, 160), img2)

        out_path = f"test_{cid}.png"
        img.save(out_path)

        TXT = f"""
**Günün Çifti:**

{N1} + {N2} = 💚

Bir sonraki çift **{tomorrow}** tarihinde seçilecektir!
"""

        await message.reply_photo(
            out_path,
            caption=TXT,
            reply_markup=InlineKeyboardMarkup(POLICE),
        )
        await msg.delete()

        # Telegraph'a yükleme (isteğe bağlı)
        try:
            uploaded = upload_file(out_path)
            for x in uploaded:
                telegraph_url = "https://graph.org/" + x
                # Kaydetmek istersen:
                # couple = {"c1_id": c1_id, "c2_id": c2_id}
                # await save_couple(cid, today, couple, telegraph_url)
        except Exception:
            pass

        # else:
        #     msg = await message.reply_text("Bugünün çift görseli getiriliyor...")
        #     b = await _get_image(cid)
        #     c1_id = int(is_selected["c1_id"])
        #     c2_id = int(is_selected["c2_id"])
        #     c1_name = (await app.get_users(c1_id)).first_name
        #     c2_name = (await app.get_users(c2_id)).first_name
        #     TXT = f"""
        # **Bugünün Seçilmiş Çifti 🎉:**
        # [{c1_name}](tg://openmessage?user_id={c1_id}) + [{c2_name}](tg://openmessage?user_id={c2_id}) = ❣️
        # Bir sonraki çift **{tomorrow}** tarihinde seçilecektir!
        # """
        #     await message.reply_photo(b, caption=TXT)
        #     await msg.delete()

    except Exception as e:
        print(str(e))

    # Geçici dosyaları temizle
    try:
        os.remove("./downloads/pfp1.png")
    except Exception:
        pass
    try:
        os.remove("./downloads/pfp2.png")
    except Exception:
        pass
    try:
        os.remove(f"test_{cid}.png")
    except Exception:
        pass


__mod__ = "COUPLES"
__help__ = """
**/couples** - Grubun bugünkü çiftlerini etkileşimli görselle oluşturur.
"""