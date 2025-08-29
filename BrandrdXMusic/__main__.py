
# /root/ragnar/BrandrdXMusic/__main__.py

import asyncio
import importlib
from pyrogram import idle

import config
from BrandrdXMusic import LOGGER, app, userbot
from BrandrdXMusic.core.call import Hotty
from BrandrdXMusic.misc import sudo
from BrandrdXMusic.plugins import ALL_MODULES
from BrandrdXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

# --- PyTgCalls/NTgCalls uyumlu import ---
try:
    # py-tgcalls (önerilen)
    from pytgcalls.exceptions import NoActiveGroupCall  # type: ignore
except Exception:  # ntgcalls ortamlarında bu modül bulunmayabilir
    class NoActiveGroupCall(Exception):
        """Fallback: Aktif grup çağrısı yoksa atılan exception için yer tutucu."""
        pass


async def init():
    # Assistant (userbot) stringleri hiçbiri tanımlı değilse erken çık
    if not any([config.STRING1, config.STRING2, config.STRING3, config.STRING4, config.STRING5]):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        return

    # Sudo ve ban listelerini yükle
    await sudo()
    try:
        for user_id in await get_gbanned():
            BANNED_USERS.add(user_id)
        for user_id in await get_banned_users():
            BANNED_USERS.add(user_id)
    except Exception as e:
        LOGGER("BrandrdXMusic").warning(f"Ban listelerini yüklerken uyarı: {e}")

    # Ana botu başlat
    await app.start()

    # Pluginleri içeri al
    for mod in ALL_MODULES:
        importlib.import_module(f"BrandrdXMusic.plugins.{mod}")
    LOGGER("BrandrdXMusic.plugins").info("Successfully imported modules...")

    # Assistant userbot ve çağrı istemcisini başlat
    await userbot.start()
    await Hotty.start()

    # Log grubunda/kanalda video sohbet açık mı kontrol etmek için kısa bir ısıtma yayını
    try:
        await Hotty.stream_call("https://graph.org/file/e999c40cb700e7c684b75.mp4")
    except NoActiveGroupCall:
        LOGGER("BrandrdXMusic").error(
            "Log grubu/kanalında görüntülü sohbet kapalı. Lütfen açın ve tekrar deneyin. Bot durduruluyor..."
        )
        return
    except Exception as e:
        # Isıtma akışı zorunlu değil; sadece bilgi ver
        LOGGER("BrandrdXMusic").warning(f"Warmup stream atlanıyor: {e}")

    # Handler/decorator kurulumları
    await Hotty.decorators()

    LOGGER("BrandrdXMusic").info(
        "ᴅʀᴏᴘ ʏᴏᴜʀ ɢɪʀʟꜰʀɪᴇɴᴅ'ꜱ ɴᴜᴍʙᴇʀ ᴀᴛ @BRANDED_PAID_CC ᴊᴏɪɴ @BRANDRD_BOT , @BRANDED_WORLD ꜰᴏʀ ᴀɴʏ ɪꜱꜱᴜᴇꜱ"
    )

    # Çalışır halde bekle
    await idle()

    # Kapatma
    await app.stop()
    await userbot.stop()
    LOGGER("BrandrdXMusic").info("Stopping Brandrd Music Bot...")


if __name__ == "__main__":
    asyncio.run(init())