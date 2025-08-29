from pyrogram.types import InlineKeyboardButton

import config
from BrandrdXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
            InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT,  # t.me/... ya da https://...
            ),
        ],
    ]
    return buttons


def private_panel(_):
    # OWNER_ID butonunu user_id yerine tg:// url ile veriyoruz
    owner_url = (
        f"tg://user?id={config.OWNER_ID}"
        if hasattr(config, "OWNER_ID")
        else (f"tg://user?id={config.OWNER_IDS[0]}" if hasattr(config, "OWNER_IDS") and config.OWNER_IDS else None)
    )

    row_owner_support = []
    if owner_url:
        row_owner_support.append(
            InlineKeyboardButton(text=_["S_B_5"], url=owner_url)
        )
    row_owner_support.append(
        InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT)
    )

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        # Bu callback_data bir handler tarafından yakalanacak kısa bir anahtar olmalı
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        row_owner_support,
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
        ],
        # Burada URL vermek istiyorsun; o yüzden callback_data değil url kullan
        [
            InlineKeyboardButton(text=_["S_B_7"], url="https://t.me/yanilgisohbet"),
        ],
    ]
    return buttons