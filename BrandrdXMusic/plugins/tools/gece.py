from pyrogram import filters
from BrandrdXMusic import app
from config import BANNED_USERS
from pyrogram.types import Message
import datetime
import random

@app.on_message(filters.command(["gece"], prefixes=["/", "!", "."]) & ~BANNED_USERS)
async def gece_mesaji(_, message: Message):
    # Türkiye saat dilimi
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3)))
    saat = now.hour

    # Gece mesajları
    gece_mesajlari = [
        "?? Gece çok sessiz ve huzurlu...",
        "⭐ Gökyüzü yıldızlarla dolu, iyi geceler!",
        "?? Derin bir sessizlik hakim, tatlı rüyalar!",
        "?? Yat ve güzel rüyalar gör...",
        "?? Şehrin ışıkları altında huzur bul...",
        "?? Ay ışığı odanı aydınlatsın!",
        "?? Sessizlik ruhunu saracak, iyi geceler!",
        "?? Rüyaların yıldızlarla dolu olsun!",
        "?? Huzurlu bir uyku seni bekliyor...",
        "?? Geceyi hisset, derin nefes al ve rahatla!",
        "?? Yastığa kafanı koy, hayaller başlasın!",
        "?? Gece sessiz, kalbin rahat olsun!"
    ]

    # Sabah mesajları
    sabah_mesajlari = [
        "?? Günaydın! Yeni bir gün başlıyor!",
        "☕ Kahveni al ve güne enerjik başla!",
        "?? Bugün güzel şeyler seni bekliyor!",
        "?? Sabahın tazeliğiyle dolu ol!",
        "?? Güzel bir kahvaltı yapmayı unutma!",
        "?? Kuşlar seni selamlıyor, günaydın!",
        "?? Yeni umutlarla dolu bir gün dilerim!",
        "?? Bugün harika şeyler yapabilirsin!",
        "?? Güne gülümseyerek başla!",
        "?? Işık dolu bir sabah seni bekliyor!",
        "?? Şans seninle olsun!",
        "??‍♂️ Huzurlu bir sabah meditasyonu yap!"
    ]

    # Öğlen mesajları
    oglen_mesajlari = [
        "☀️ Öğle vakti geldi, enerjini toplamalısın!",
        "?? Öğle yemeği zamanı!",
        "?? Hava güzel, biraz dışarı çıkabilirsin!",
        "?? Zaman hızla geçiyor, keyfini çıkar!",
        "?? Öğle molası ile kendini yenile!",
        "?? Hafif bir öğle yemeği ile enerji kazan!",
        "☕ Kahve molası ver, biraz dinlen!",
        "?? Güne devam et, motivasyonunu kaybetme!",
        "?? Su içmeyi unutma, sağlığın önemli!",
        "?? Hafif bir müzik ile öğlen keyfi yap!"
    ]

    # Akşam mesajları
    aksam_mesajlari = [
        "?? Akşam olmuş, günün yorgunluğunu at!",
        "?? Gün batımı çok güzel görünüyor!",
        "?? Akşam rahatla ve dinlen!",
        "?? Yıldızlar seni bekliyor, huzurlu bir akşam!",
        "?? Akşam müziği ile ruhunu besle!",
        "?? Evde keyifli bir akşam geçirebilirsin!",
        "?? Mum ışığında sakin bir akşam...",
        "?? Gökyüzüne bak, derin nefes al ve rahatla!",
        "☕ Akşam çayı ile kendini ödüllendir!",
        "?? Yarın için enerji topla, iyi akşamlar!"
    ]

    # Saat aralığına göre mesaj seç
    if 0 <= saat < 6:
        mesaj = random.choice(gece_mesajlari)
    elif 6 <= saat < 12:
        mesaj = random.choice(sabah_mesajlari)
    elif 12 <= saat < 18:
        mesaj = random.choice(oglen_mesajlari)
    else:
        mesaj = random.choice(aksam_mesajlari)

    await message.reply_text(f"?? Türkiye saatiyle: {now.strftime('%H:%M')}\n{mesaj}")
