# AviaxMusic/plugins/tools/song.py

from BrandrdXMusic import app   # Mevcut botun app'ini alıyoruz
import os
import asyncio
from pyrogram import filters
from pyrogram.types import Message
import yt_dlp
from yt_dlp.utils import DownloadError

# ----------------- AYARLAR -----------------
COOKIE_FILE = "/root/edamuzik/Ceydamuzik/cookies/BrandrdXMusic"
DOWNLOAD_PATH = "./downloads"
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

# ----------------- ARAMA VE GÖNDERME FONKSİYONU -----------------
async def search_and_send(message: Message, search_type="music"):
    if len(message.command) < 2:
        await message.reply_text(
            f"❌ Aramak istediğiniz {'şarkı' if search_type=='music' else 'video'} adını yazın.\n"
            f"Örnek: /{'bul' if search_type=='music' else 'vbul'} Taladro"
        )
        return

    if not os.path.exists(COOKIE_FILE):
        await message.reply_text("❌ Cookie dosyası bulunamadı.")
        return

    query = " ".join(message.command[1:])
    status_msg = await message.reply_text(f"?? `{query}` için arama yapılıyor ve indiriliyor, lütfen bekleyin...")

    # ----------------- ARAMA -----------------
    ydl_opts_search = {
        "quiet": True,
        "format": "bestaudio/best" if search_type=="music" else "best",
        "noplaylist": True,
        "cookiefile": COOKIE_FILE,
        "skip_download": True,
        "extract_flat": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts_search) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)
            entries = info.get("entries", [])

            if not entries:
                await status_msg.edit_text("❌ Sonuç bulunamadı.")
                return

            first_result = entries[0]
            url = first_result.get("url")
            title = first_result.get("title")

        # ----------------- İNDİRME -----------------
        safe_title = "".join([c if c.isalnum() or c in " _-" else "_" for c in title])
        file_name = os.path.join(DOWNLOAD_PATH, f"{safe_title}.{'mp3' if search_type=='music' else 'mp4'}")

        ydl_opts_download = {
            "format": "bestaudio/best" if search_type=="music" else "best",
            "outtmpl": file_name,
            "cookiefile": COOKIE_FILE,
            "quiet": True,
        }

        await status_msg.edit_text(f"⬇️ `{title}` indiriliyor...")
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, lambda: yt_dlp.YoutubeDL(ydl_opts_download).download([url]))

        # ----------------- CHAT'E GÖNDER -----------------
        await status_msg.edit_text(f"✅ `{title}` indirildi, gönderiliyor...")
        if search_type == "music":
            await message.reply_audio(file_name, caption=title)
        else:
            await message.reply_video(file_name, caption=title)

        os.remove(file_name)
        await status_msg.delete()

    except DownloadError as e:
        await status_msg.edit_text(f"❌ Youtube hatası: {e}")
    except Exception as e:
        await status_msg.edit_text(f"❌ Hata oluştu: {e}")


# ----------------- KOMUT BAĞLAMA -----------------
@app.on_message(filters.command("bul") & filters.private)
async def music_search(client, message: Message):
    await search_and_send(message, search_type="music")

@app.on_message(filters.command("vbul") & filters.private)
async def video_search(client, message: Message):
    await search_and_send(message, search_type="video")