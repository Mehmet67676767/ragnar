import io

from gtts import gTTS
from pyrogram import filters

from BrandrdXMusic import app


@app.on_message(filters.command("tts"))
async def text_to_speech(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "Lütfen sese dönüştürülecek bir metin giriniz."
        )

    text = message.text.split(None, 1)[1]
    tts = gTTS(text, lang="tr")  # Türkçe için "tr"
    audio_data = io.BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)

    audio_file = io.BytesIO(audio_data.read())
    audio_file.name = "ses.mp3"
    await message.reply_audio(audio_file)


__HELP__ = """
**Metni Sese Dönüştürme Komutu**

`/tts` komutunu kullanarak yazdığınız metni sesli hale getirebilirsiniz.

- `/tts <metin>` : Girilen metni **Türkçe seslendirmeye** çevirir.

**Örnek:**
- `/tts Merhaba Dünya`

**Not:**  
`/tts` komutundan sonra mutlaka çevrilecek bir metin yazmalısınız.
"""

__MODULE__ = "TTS"