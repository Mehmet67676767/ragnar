import logging
from googlesearch import search
from pyrogram import filters

from BrandrdXMusic import app
from SafoneAPI import SafoneAPI


# Google Arama
@app.on_message(filters.command(["google", "gle"]))
async def google(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text("Örnek:\n\n`/google Atatürk`")
        return

    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = " ".join(message.command[1:])

    b = await message.reply_text("**🔍 Google'da aranıyor...**")
    try:
        a = search(user_input, advanced=True)
        txt = f"**Arama Sorgusu:** {user_input}\n\n**Sonuçlar:**"
        for result in a:
            txt += f"\n\n[❍ {result.title}]({result.url})\n<b>{result.description}</b>"
        await b.edit(
            txt,
            disable_web_page_preview=True,
        )
    except Exception as e:
        await b.edit(str(e))
        logging.exception(e)


# Play Store Uygulama Arama
@app.on_message(filters.command(["app", "apps"]))
async def app(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text("Örnek:\n\n`/app WhatsApp`")
        return

    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = " ".join(message.command[1:])

    cbb = await message.reply_text("**📱 Play Store'da aranıyor...**")
    a = await SafoneAPI().apps(user_input, 1)
    b = a["results"][0]

    icon = b["icon"]
    id = b["id"]
    link = b["link"]
    ca = b["description"]
    title = b["title"]
    dev = b["developer"]

    info = (
        f"<b>[Uygulama Adı: {title}]({link})</b>\n"
        f"<b>ID:</b> <code>{id}</code>\n"
        f"<b>Geliştirici:</b> {dev}\n"
        f"<b>Açıklama:</b> {ca}"
    )

    try:
        await message.reply_photo(icon, caption=info)
        await cbb.delete()
    except Exception as e:
        await message.reply_text(str(e))