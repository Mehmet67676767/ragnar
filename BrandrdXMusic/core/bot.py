from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config
from ..logging import LOGGER


class Hotty(Client):
    def __init__(self):
        LOGGER(__name__).info("Starting Bot...")
        super().__init__(
            name="BrandrdXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
            parse_mode=ParseMode.HTML,  # Mesajlarda varsayılan HTML
        )

    async def start(self):
        await super().start()

        # Bot bilgilerini güvenli şekilde çek
        try:
            me = await self.get_me()
        except Exception as ex:
            LOGGER(__name__).error(f"get_me() başarısız: {type(ex).__name__}.")
            raise

        self.id = me.id
        self.name = (me.first_name or "").strip()
        if me.last_name:
            self.name += f" {me.last_name.strip()}"
        self.username = me.username or "unknown"
        # Pyrogram User.mention (HTML) özelliğini güvenli al
        try:
            self.mention = me.mention  # v2'de property olarak mevcut
        except Exception:
            self.mention = f"<a href=\"tg://user?id={me.id}\">{self.name or 'Bot'}</a>"

        start_video_path = "https://litter.catbox.moe/d27zsvy6qmzqw3by.mp4"
        start_caption = (
            f"<u><b>» {self.mention} bot başlatıldı :</b></u>\n\n"
            f"ID : <code>{self.id}</code>\n"
            f"Ad : {self.name or '—'}\n"
            f"Kullanıcı adı : @{self.username}"
        )

        # Başlangıç videosunu log grubuna gönder
        try:
            await self.send_video(
                chat_id=config.LOGGER_ID,
                video=start_video_path,
                caption=start_caption,
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Bot log grup/kanalına erişemedi. Lütfen botu log grubuna/kanalına ekleyip tekrar deneyin."
            )
        except Exception as ex:
            LOGGER(__name__).error(f"Video gönderilemedi. Sebep: {type(ex).__name__}.")

        # Botun log grubunda admin olup olmadığını kontrol et
        try:
            member = await self.get_chat_member(int(config.LOGGER_ID), self.id)
            if member.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error(
                    "Lütfen botu log grup/kanalında yönetici yapın."
                )
        except Exception as ex:
            LOGGER(__name__).error(
                f"Log grubunda üye kontrolü başarısız: {type(ex).__name__}."
            )

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()