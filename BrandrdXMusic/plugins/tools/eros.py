import random
from pyrogram import filters
from BrandrdXMusic import app  # YukkiMusic yerine AviaxMusic olacak

def get_random_message(love_percentage):
    if love_percentage <= 30:
        return random.choice(
            [
                "Aşk var ama biraz kıvılcım gerekiyor.",
                "Güzel bir başlangıç, ama daha çok yol var.",
                "Bu sadece güzel bir şeyin başlangıcı.",
            ]
        )
    elif love_percentage <= 70:
        return random.choice(
            [
                "Güçlü bir bağ var. Onu beslemeye devam et.",
                "Şansın yüksek, üzerine git.",
                "Aşk filizleniyor, devam et.",
            ]
        )
    else:
        return random.choice(
            [
                "Vay canına! Tam bir aşk masalı!",
                "Mükemmel eşleşme! Bu bağı koru.",
                "Kader sizi birleştirmiş. Tebrikler!",
            ]
        )

@app.on_message(filters.command("ihtimal", prefixes=["/", "!"]))
async def love_command(client, message):
    command, *args = message.text.split(" ")
    if len(args) >= 2:
        name1 = args[0].strip()
        name2 = args[1].strip()

        love_percentage = random.randint(10, 100)
        love_message = get_random_message(love_percentage)

        response = f"{name1} 💕 + {name2} 💕 = %{love_percentage}\n\n{love_message}"
    else:
        response = "Lütfen /ihtimal komutundan sonra iki isim yaz."

    await app.send_message(message.chat.id, response)

__MODULE__ = "Aşk Ölçer"
__HELP__ = """
**Aşk Ölçer:**

• `/love [isim1] [isim2]` — İki kişi arasındaki aşk yüzdesini hesaplar.
"""
