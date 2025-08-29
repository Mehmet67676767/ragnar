import random

mani = (
    """**Çadıra serdim keçe
Koyunu sürdüm gece
O günlerde gelir mi?
Elin elime geçe**""",
    """**Çalıştım arı gibi
Peteğin balı gibi
Kız sen beni erittin
Dağların karı gibi**""",
    """
**Patlıcanı haşladım
Doldurmaya başladım
Dediler yarin gelmiş
Oynamaya başladım**""",
    """**Su gelir akmayınan
Dereyi yıkmayınan
Seven yâre doyar mı?
Uzaktan bakmayın**""",
    """**Portakal dilim dilim
Gel otur benim gülüm
Ben sana ne dedim ki
Tutulsun benim dilim**""",
    """**Mani maniyi açar
Mani gönlümü açar
İki sen söyle bir ben
Hangimiz üste çıkar**""",
    """**Bahçelerde babaçça
Açılır akça akça
Kaçtım karşıma çıktı
Tombul yanaklı Hatça**""",
    """**Çilekten yaptım reçel
Kara gün gelir geçer
Derdimi söyleyemem
Kalbimden neler geçer**""",
    """**Leçenin bucağında
Od olur ocağında
Allah canımı alsın
O yârin kucağında**""",
    """
**Bağa girdim hurmaya
Avcı geldi vurmaya**""",
    """**Ele bağışlanır mı
Bahçede ekşi elma**""",
    """**Dolu vurdu bağıma
Yel attı yaprağını
Korkarım garip ölem
El atar toprağımı**""",
    """**Penceresi Orhun’dan
Bir yar sevdim Zorkun’dan
Keşke sevmez olaydım
Ödü koptu korkudan**""",
    """**Bahçelerde mum direk
Suyu nerden indirek
İrezil gelin gidiyo
Uyuz ite bindirek**""",
    """**Sıra sıra kazanlar
Kara yazı yazanlar
Cennet yüzü görmesin
Aramızı bozanlar**""",
    """**Bağa girdim hurmaya
Avcı geldi vurmaya**""",
    """**Dürüp cebime koydum
Ne güzelsin Maşallah
Macirin kızlarını
Şeytan çarpar inşallah**""",
    """**Faytonun penceresi
Elindedir ceresi
Küçükken gelin olmuş
Ne bunun acelesi**""",
    """**Kaleden indim durdum
Bir çift güvercin vurdum
Kız mendilin ne güzel**""",
    """**Postanede pulcusun
Ormanlarda kolcusun
Meyil versem söz versem
El kulakta yolcusun**""",
    """**Höbek höbek dikenler
Aba gömlek biçenler
Bakışından bellidir
Kara sevda çekenler**""",
    """**Kaşların karasına
Mim çekmiş arasına
Seni cerrah diyorlar
Yürekler yarasına**""",
    """**Hapisanenin kapısı
Demirdendir yapısı
Yârimin günü varmış
Bir ay daha hapisi**""",
    """**Örtünü eğirmişsin
Kaşına değirmişin
Çokta güzel değildin
Kendini sevdirmişin**""",
    """**Kız entarin eflatun
Dön de arkana bakın
Senin gibi güzeli
Vermem ellerden sakın**""",
    """**Bir dalda iki vişne
Güzelim aşka düşme
Bu aşkın sonu yoktur
Boş yere dile düşme**""",
    """**Bahçede ekşi elma
Ne güzelsin Maşallah
Macirin kızlarını
Şeytan çarpar inşallah**""",
    """**Mantuvarım mantuvar
Mantuvarın vakti var
Mantuvara gelenin
Cennette bir tahtı var**""",
    """**Nazlıya bak nazlıya
Evin engin değil mi?
Doğru söylen komşular
Nazlı dengim değil mi?**""",
    """**Oğlanın adı Yılmaz
Olmaz aslanım olmaz
İçin gel gel demezse
O evde geçim olmaz**""",
    """**Ay doğar sini gibi
Sininin yanı gibi
Oyar beni seviyor
Beden de canı gibi**""",
    """**Merdiveni kırkayak
Kırkına vurdum dayak
Yar geliyor dediler
Seyirttim yalınayak.**""",
    """**Şu tepenin alıcı
Kırmızıdır pabucu
Şeftali vermeyenin
Kabul olmaz orucu.**""",
    """**Yeşil sandık kilidi
Üstünü gül bürüdü
Kız sen orada ben burda
İman tahtam çürüdü**""",
    """**Kekliğim seker ağlar
Tüyünü döker ağlar
Anasız gelin olan
İçini çeker ağlar**""",
    """**Sırma belikli yârim
Beyaz bilekli yârim
Nasıl bensiz durursun
Mermer yürekli yârim**""",
    """**Sunam sesemi geldin
Ayak basamı geldin
Sağlığımda gelmedin
Öldüm yasamı geldin**""",
    """**Küçük ovalı geldi
Atlı develi geldi
Başıma bu sevdalar
Seni seveli geldi**""",
    """**Kaşların emi emi
Ne bakan kinle beni
Yat dizimin üstüne
Çekeyim sana ninni.**""",
    """**Yanamam bile bile
Ben düştüm gurbet ile
Yedi mendil çürüttüm
Gözüm yaşın sile sile.**""",
    """**Siyah zülüflü canım
Neşter vur aksın kanım
Nar göbek fincan olsun
Doldur içeyim canım.**""",
    """**Ağaçlarda mazılar
Gönül seni arzular
Yar aklıma gelince
Yüreciğim sızılar.**""",
    """**Karşıda duran sensin
Zülfünü buran sensin
Bana cellât kar etmez
Boynumu vuran sensin.**""",
    """**Bugün hava karardı
Betim benzim sarardı
Baş ecel yastığında
Kolum yâri sarardı.**""",
    """**Kar yağar kiriş gibi
Eridim gümüş gibi
Ben yâri arzuladım
Tufanda yemiş gibi.**""",
    """**Yel vurur kazak oynar
Başımda tozak oynar
Ben yârime ne yaptım
O benden uzak oynar**""",
    """**Tarla başı pıtırak
Duralım tarak tarak
Çok çalıştık yetmez mi?
Gelin kızlar oturak**""",
    """**Mendilleri kokulu
Yan cebinde sokulu
Ne zaman kapanacak
Dağıstan’ın Okulu**""",
    """**Gel yakına yakına
Çeşmenin arkasına
Kırmızı gül takayım
Ceketin yakasına**""",
    """**Kayalardan kayarım
Bu kız benim ayarım
Ayşe benim olmazsa
Kaderime yanarım**""",
    """**Yel vurur kazak oynar
Başımda tozak oynar
Ben yârime ne yaptım
O benden uzak oynar**""",
    """**Tarla başı pıtırak
Duralım tarak tarak
Çok çalıştık yetmez mi?
Gelin kızlar oturak**""",
    """**Mendilleri kokulu
Yan cebinde sokulu
Ne zaman kapanacak
Dağıstan’ın Okulu**""",
    """**Gel yakına yakına
Çeşmenin arkasına
Kırmızı gül takayım
Ceketin yakasına**""",
    """**Kayalardan kayarım
Bu kız benim ayarım
Ayşe benim olmazsa
Kaderime yanarım**""",
    """**Bahçe bahçe gezerim
İnci boncuk düzerim
Bakın işte yüzüme
Bu köyde en güzelim**""",
    """**Kara taşın kenarı
Üstünde kırdım narı
Tutulası dillerim
Nasıl darılttın yarı**""",
    """**Yuvasında kırlangıç
Kanadı ayrıç ayrıç
Döne Kızı sevenler
Kan kussun avuç avuç**""",
    """**Elinde var yelpaze
Kuş dadanmış kiraza
Yakında geleceğim
Çekme kendini naza**""",
    """**Mani mani nideyim
Hangi günde geleyim
Ellerin yâri güzel
Ben çirkini nideyim**""",
    """**Masa üstünde bıçak
Sanki bana vuracak
Anne haberin olsun
Abim kız kaçıracak**""",
    """**Gül gibi oyum oyum
Kısacık kaldı boyum
Alacaksan al kalan
Yeter ettiğin oyun**""",
    """**Çaya vardım çayladım
Çayda balık avladım
Balık değil amacım
Ben gönlümü eğledim**""",
    """**Tren yolunda tütün
Yaprağı bütün bütün
Hem ana hem babadan
Koyma Allah’ım yetim**""",
    """**Gide gide yoruldum
Bir kenara oturdum
Güzelliğine değil
Çalımına vuruldum**""",
    """**Caminin minaresi
Mektebin penceresi
Şu Macirin kızları
Bulaşık tenceresi**""",
    """**Kiraz dalı budaklı
Meryem kiraz dudaklı
Yârim dünya güzeli
Elma gibi yanaklı**""",
    """**Derelere gidelim
Koyun kuzu güderim
İkimizi görmüşler
Nasıl inkâr ederim**""",
    """**Mezarlığın taşını
Koyun mu sandın yârim
Sevipte ayrılmayı
Oyun mu sandın yârim**""",
    """**Al giydim alsın diye
Mor giydim sarsın diye
İsteyene varmadım
Sevdiğim alsın diye**""",
    """**Karşıdan yar geliyor
Fistanı dar geliyor
Ben sevdim eller aldı
O bana ar geliyor**""",
    """**Gökyüzünde tayyare
Önündedir pervane
Kaş göz oynatsam oğlan
Olacak bir divane**""",
    """**Bakkallarda toz şeker
Şekerler kilo çeker
Seni gâvurun oğlu
Gördüğüne ah çeker**""",
    """**Kızın adı gül Fatma
Ayranlara su katma
Utanıyorum canım
Yolda bana laf atma**""",
    """**Gide gide yoruldum
Bir duldaya oturdum
Pezevengin oğluna
Bir bakışta vuruldum**""",
    """**Annem entari almış
Beyaz çizgisi varmış
Bir yar sevdim bilmeden
Onunda yâri varmış**""",
    """**Karalar karda kaldı
Bülbüller zarda kaldı
Gönül kapısı kitli
Anahtar yarda kaldı**""",
    """**Kara kütük yanıyor
İçinde çay kaynıyor
Hele bakın eltiler
Ne de güzel oynuyor**""",
    """**Kahve piştiği yerde
Pişip taştığı yerde
Güzel çirkin aranmaz
Gönül düştüğü yerde**""",
    """**Osmaniye üst başta
Oturma kışın taşta
Ben senle eğleniyom
Benim sevdiğim başka**""",
    """**Mendilim yelleniyo
Şu gönlüm eğleniyo
Şu macirin kızları
Oğlanmı beğeniyo**""",
    """**Konağın penceresi
Ne zalimdir gecesi
Sana kim âşık olur
Sokaklar eğlencesi**""",
    """**Çeşmenin taşı gibi
Gözünün yaşı gibi
Öyle bir kız sevdim ki
Kanarya kuşu gibi**""",
    """**Kayalarda kayarım
Yoktur benim ayarım
Ben sevdadan ölürsem
Kaderime yanarım**""",
    """**Arabalar geliyo
Ablam gelin oluyo
O kocaya gidince
Sıra bana geliyo**""",
    """**Çay kıyında çalılık
Boğazında altılık
İyi bakın oğlanlar
Oynayanlar satılık**""",
    """**Kaşları ok sevdiğim
Canımdan çok sevdiğim
Hep güzeller geliyor
İçinde yok sevdiğim**""",
    """**Yumurtası hollukta
Oturuyor yollukta
Eller düğün yapıyor
Bizim düğün bollukta**""",
    """**Dam üstünde yuvarlak
Dere akıyor şarlak
Benim sevdiğim yârim
Doğan aylarda parlak**""",
    """**Sıra sıra çarşılar
Yârim beni karşılar
Gizli gizli konuştum
Şimdi duydu komşular**""",
    """**Bir taş attım kargaya
Dönüp baktım arkaya
Evvel candan severdim
Şimdi vurdum dalgaya**""",
    """**Elmayı yüke koydum
Ağzını dike koydum
Aldım yârin elinden
Boynunu büke koydum**""",
    """**Karanfil haşlanır mı?
Saksısı taşlanır mı?
Küçücükken yar sevdim
Ele bağışlanır mı?**""",
    """**Pencerede duran kız
Bayram geldi dolan kız
Kurbansız bayram olmaz
Sana olam kurban kız**""",
    """**Karşıdan bakma yârim
Kaşlarını çatma yârim
Ben eski zamparayım
Hiç çalım satma yârim**""",
    """**Kar yağar saçaklara
Dökülür sokaklara
Nasıl ana doğurmuş
Sığmıyor kucaklara**""",
    """**Yüzüğüm taşa geldi
Bir kalem başa geldi
Sevda nedir bilmezdim
Ne çare başa geldi.**""",
    """**Hapsanenin kapısı
Demirdendir yapısı
Yârimin günü varmış
Bir ay daha hapisi**""",
    """**Örtünü eğirmişsin
Kaşına değirmişin
Çokta güzel değildin
Kendini sevdirmişin**""",
    """**Kız entarin eflatun
Dön de arkana bakın
Senin gibi güzeli
Vermem ellerden sakın**""",
    """**Bir dalda iki vişne
Güzelim aşka düşme
Bu aşkın sonu yoktur
Boş yere dile düşme**""",
    """**Mantuvarım mantuvar
Mantuvarın vakti var
Mantuvara gelenin
Cennette bir tahtı var**""",
    """**Nazlıya bak nazlıya
Evlerin engin değil mi?
Doğru söylen komşular
Nazlı dengim değil mi?**""",
    """**Oğlanın adı Yılmaz
Olmaz aslanım olmaz
İçin gel gel demezse
O evde geçim olmaz**""",
    """**Ay doğar sini gibi
Sininin yanı gibi
Oyar beni seviyor
Beden de canı gibi**""",
    """**Dağda fıstık olur mu?
Ateş yastık olur mu?
Sen orada ben burada
Böyle dostluk olur mu?**""",
    """**İn dereye dereye
Dere çakıllı yârim
Her geçene bakıyor
Gel geç akıllı yârim**""",
    """**Bahçelerde portakal
Gitme yârim burada kal
Sen şehre inersen
Bana çam bardak al**"""

)

espri = [
    "Son gülen en geç anlayandır.",
    "İnsanların seni ezmesine izin verme. Ehliyet al, sen onları ez…",
    "İlahi Azrail … Sen adamı öldürürsün!",
    "Ben mafya babasıyım çünkü oğlumun adı Mafya.",
    "Kim vurduya gittim birazdan geleceğim.",
    "Zenginler et, fakirler hayalet yer.",
    "Hava korsanı uçağı kaçıracaktı ama yapamadı çünkü uçağı kaçırdı.",
    "GİT’Arı’ getir de biraz şarkı söyleyelim.\n   -Abi arı sokmasın!",
    "Canın sıkıldıysa gevşet.",
    "Almanya’da Almanlar, Sakarya’da sakarlar yaşar.",
    "Sana bir kıllık yapayım, kıllarını koyarsın.",
    "Seven unutmaz oğlum, eight unutur.",
    "Cem Uzan, üstünü örteyim.",
    "Haydi Unkapanı’na gidip birkaç kapan kuralım. Belki un yakalarız",
    "Adamın biri güneşte yanmış, ay da düz.",
    "Sinemada on dakika ara dedi, aradım aradım açmadı.",
    "Röntgen Filmi çektirdik, yakında sinemalarda.",
    "Geçen gün taksi çevirdim hala dönüyor.",
    "Ben hikâye yazarım Ebru Destan.",
    "Geçen gün geçmiş günlerimi aradım ama meşguldü.",
    "Tebrikler kazandınız, şimdi tencere oldunuz!",
    "Kaba kuvvet uygulama, kap kırılabilir.",
    "Ayna’nın karşısında süslenme, Manga’nın karşısında süslen.",
    "Geçen file çorap aldım, zürafaya almadım.",
    "Yılanlardan korkma, yılmayanlardan kork.",
    "Ben kahve içiyorum, Nurgül Yeşilçay.",
    "Bak şu karşıdaki uçak PİSTİ, ama bir türlü temizlemediler.",
    "Geçen gün geçmiş günlerimi aradım ama meşguldü.",
    "Adamın birisi televizyona çıkmış bir daha indirememişler.",
    "Adamın biri gülmüş, saksıya koymuşlar.",
    "Funda Arar dediler ama hala daha aramadı.",
    "Adamın kafası atmış bacakları eşek.",
    "Uzun lafın kısası: U.L.",
    "Yağmur yağmış, kar peynir!",
    "Sakla samanı, inekler aç kalsın.",
    "Baraj dendi mi, akan sular durur.",
    "Dünya dönermiş ay da köfte…",
    "Son gülen en geç anlayandır.",
    "Bu erikson, başka erik yok.",
    "Sen kamyonu al, Leonardo da vinci.",
    "Adamın biri gülmüş, bahçeye dikmişler.",
    "Top ağlarda, ben ağlamaz mıyım?",
    "Ben yürüyelim diyorum Gerard Depardieu.",
    "Ahmet Saz çaldı. Polis tutukladı.",
    "Beni ayda bir sinemaya götürme, Marsta bir sinemaya götür.",
    "Ben ekmek yedim Will Smith.",
    "Aaaaa siz çok terlemişsiniz durun size terlik getiriyim.",
    "Kalbinin sesini dinle güzelse kaset yap",
    "Bağırsaklarda yaşayan tenya kurtları bağırsakta yaşarlar bağırmasak da yaşar.",
    "Çiçeğin biri solmuş diğeri de sağ.",
    "Lütfen sessiz olun telefon faturasını yeni yatırdım uyuyor şimdi uyanmasın",
    "Nuri ölünce Çin’e gömsünler, nur içinde yatsın.",
    "Temel kahvede işe başlar, müşterilerden biri seslenir:\n   -Temel bize üç çay, biri açık olsun.\n   -Hangisi?",
    "Temel bir gün Fransa’ya gitmiş:\n   -Aaa burayı da mı Sabancı aldı, demiş.",
    "İngilizcem yok, tanıdığım bütün Cem’ler Türk.",
    "Sarımsağı havanda dövmüşsün, Ha Muş’ta.",
    "Dondurmayı ben yalamam, himalayalar.",
    "Yarasa yararlı bir hayvandır. Yararlı bir hayvan olmasaydı yaramasa derlerdi.",
    "Kelebekler, köstebekler ama ben beklemem.",
    "Bütün umutlarım suya düştü ama boğulmadılar. Çünkü onlara yüzme öğretmiştim",
    "Bu gece seni kınıyorum, çünkü kına gecesi.",
    "Basamakta durmayın otomatik kapı çarpar, böler, karekökünü alır.",
    "Hayırlı olsun Araba almışsın. Evet aldık. Niye Araba aldın ki kendine alsaydın.",
    "Çok Makbule geçti, şimdi de Fatma geçiyor.",
    "Alinin selamı var.\n   Hangi Ali?\n   Şehirlerarası otobüs termin-ali",
    "-Abi sana Sıla’nın selamı var.\n   -Hangi Sıla?\n   -Gayri Safi Milli HaSıla”",
    "Sen o çeteyi tanıyor musun\n   -Hangi çeteyi\n   -Peçeteyi.”",
    "Gözlüklerin numaralı mı?\n   -Yok kale arkası”",
    "Erkek ata ne denir?\n   Bayat”",
    "En güzel çay hangi dağda içilir?\n   Çay bar-dağı’nda”",
    "4. Murat neden intihar etmiş?\n   – İlk 3’e giremediği için",
    "Geçen gün arkadaşlarla fırında patates yiyorduk, fırın sıcak geldi bahçeye çıktık.",
    "Masada hangi örtü kullanılmaz?\n   – Bitki Örtüsü.",
    "Adamın kafası atmış bacakları eşek.",
    "Geçen gün geçmiş günlerimi aradım ama meşguldü.",
    "Sinüs 60, kosinüs tutmuş…",
    "Yağmur yağmış, kar peynir!",
    "Baraj dendi mi, akan sular durur.",
    "Kediler niçin havaalanına gidemez? Çünkü pist var."
]

slapmessage = [

    "{}, {}**'a Fosfor Bombası Attı! Yasalara Aykırı??!**",
    "{}, {}**'in Suratına Domates Fırlattı! Suratı kıpkırmızı oldu ??**", 
    "{}, {}**'in Saçını Çekti!**", 
    "{}, {}**'nin Suratına Yumruk attı ! Buz koy morarmasın ??**", 
    "{}, {}**'e Kafa Attı! Burnu kırıldı sanırım ??**", 
    "{}, {}**'e Uçan Tekme Attı! Jetli misin mübarek ??**", 
    "{}, {}**'e Kanepeyi Fırlattı! Öyle ölmez füze atsaydın ??**", 
    "{}, {}**'e İğne sapladı! Bu acıtmıştır sanırım ??**", 
    "{}, {}**'a Yumurta Fırlattı! Tam isabet ??**", 
    "{}, {}**'e Omuz attı! Ne bakıyon birader**", 
    "{}, {}**'e Sana Çelme taktı!**", 
    "{}, {}**'e Damacana Fırlattı! Damacanaya bişey olmamıştır umarım ??**", 
    "{}, {}**'e Üstüne Çay Döktü! Yanıyorsun Fuat Abii ??**", 
    "{}, {}**'in Kafasında Şişe Kırdı! Acımış olmalı ??**",
    "{}, {}**'in Yüzüne Tükürdü! İşte bunu yapmayacaktın ??**", 
    "{}, {}**'e Taş Attı! Aha kafası yarıldı ??**", 
    "{}, {}**'e Osmanlı Tokatı Attı! Resmen şamar oğlana çevirdi ??**", 
    "{}, {}**'e Kavanoz Fırlattı! Başka bişey bulamadı sanırım ??**",
    "{}, {}**'in Ayağının Önüne Muz Fırlattı! Basıp Kaydı ??**",
    "{}, {}**'e Çöp Kovası Fırlattı! Üstü Başı Hep Çöp Oldu ??**",
    "{}, {}**'in Üzerine Kamyon Sürdü! Kamyon'un Altında Kalmaktan Son Anda Kurtuldu ??**",
    "{}, {}**'in Gözüne Parmağını Soktu! Bu Gerçekten Acımış Olmalı ??**", 
    "{}, {}**'e Yolda Yürürken Ensene Tokat Attı ! Ve Kaçmaya Başladı??**",
    "{}, {}**'in Yüzüne Kezzap Attı! Ah Be Bergenim??**",   
    "{}, {}**'i Kıyma Makinesine Attı! Yenir Omega5??**",  
    "{}, {}**'e F35 Fırlattıı!! Savaş Başlasın??**",   
    "{}, {}**'e Pasta Attı!! Duş Almak Şart Oldu.??**",
    "{}, {}**'eTerlik Fırlattı!! Tam İsabet Anne Adayı mısın Beee????**",  
    "{}, {}**'in Üzerine Benzin Döktü Ve Ateşe Verdi!??**",
    "{}, {}**'in Kafasını Balık Dolu Bir Kovaya Soktu??**",
    "{}, {}**'in Yüzüne Pasta Fırlattı!??**",
    "{}, {}**'in Yüzüne Kahve Döktü!??**",
    "{}, {}**'in Yüzüne 150TL Fırlattı!??**",
    "{}, {}**'in Yüzüne Çay Döktü!??**",
    "{}, {}**'in Yüzüne Su Döktü!??**",
    "{}, {}**'İçin Aldığı Hediyeyi Parçaladı!??**",
    "{}, {}**'in Yüzüne 200TL Fırlattı!??**",
    "{}, {}**'in Yüzüne Kola Döktü!??**",
    "{}, {}**'e Tüplü TV Fırlattı!??**",
    "{}, {}**'in Kalbini Kırdı!??**",    
    "{}, {}**'in Yüzüne 1TL Fırlattı!??**",
    "{}, {}**'in Yüzüne 5TL Fırlattı!??**",
    "{}, {}**'in Yüzüne 10TL Fırlattı!??**",
    "{}, {}**'in Yüzüne 20TL Fırlattı!??**",
    "{}, {}**'in Yüzüne 50TL Fırlattı!??**",
    "{}, {}**'in Yüzüne 100TL Fırlattı!??**",
    "{}, {}**'in Yüzüne 150TL Fırlattı!??**",
    "{}, {}**'in Yüzüne 200TL Fırlattı!??**",
    "{}, {}**'in Yüzüne Bira Döktü!??**",
    "{}, {}**'in Yüzüne Tokat Attı!??**",
    "{}, {}**'in Kafasını Öptü!??**",
    "{}, {}**'e Çicek Verdi??**",
    "{}, {}**'e Su Fırlattı! Kurutma Makinası şart oldu??!**",
    "{}, {}**Al Şu 200'ü Bugün Eve Erken Git??!**",
    "{}, {}**'e Tabanca Çekti! Seninde Boş Olmaman Lazım??!**",
    "{}, {}**'e Şarj Aleti Fırlattı ! Elektrik Saçıyorsun Bebeğim?⚡️**",
    "{}, {}**'e Kitap Fırlattı! Al Şu Kitabı Da Biraz Oku Akıllan??!**",
    "{}, {}**'e TDK Sözlüğü Fırlattı ! Konuşmayı Bilmiyor Musun Yoksa??!**",
    "{}, {}**'e Çilek Fırlattı ! Al Ye Şunu??!**",
    "{}, {}**'e Ayna Fırlattı ! Bi Aynaya Bak Da Milletin Gözü Gönlü Açılsın???**",
    "{}, {}**'e Tasma Fırlattı! Lazım Olur Takarsın??!**",
    "{}, {}**'e Çiçek Fırlattı ! Evlenme Yaşın Gelmiş??!**",
    "{}, {}**'e Pantolon Fırlattı! Bizde Unutmuşsun??!**",
    "{}, {}**'e Keleş Fırlattı! Kürtlük Damarınız Tuttu TaTaTaTa??!**",
    "{}, {}**'e Erosun Okunu Fırlattı ! Sanırım Sana Âşık (çaktırma)??!**",
    "{}, {}**'e Arı Kovanı Fırlattı! Hızlı Kaç Arılar Geliyooor????!**",
    "{}, {}**'e Terazi Fırlattı! Dengine Göre Aslanım??!**",
    "{}, {}**'e Tartı Fırlattı! Oha Çok Kilolusun??!**",
    "{}, {}**'e Çanta Fırlattı! Okula Git Oku Oku??!**",
    "{}, {}**'e Premium Fırlattı! Sana Premium Alması Şart??!**",
    "{}, {}**'e Domestos Fırlattı! Süper Güçlerin Var Artık??!**",
    "{}, {}**'in Yanağından Öptü??**",
    "{}, {}**'nin üzerine benzin döktü ve ateşe verdi!** ??",
    "{}, {}**'nin kafasını balık dolu kovaya soktu!** ??",
    "{}, {}**'nin yüzüne pasta fırlattı! ??**",
    "{}, {}**'nin yüzüne bir fincan kahve döktü! **☕️",
    "{}, {}**'nin yüzüne 150 $ fırlattı!** ??",
    "{}, {}**'nin yüzüne bir demlik çay döktü!** ??",
    "{}, {}**'nin yüzüne bir bardak su döktü** ??",
    "{}, {}** için aldığı hediyeyi parçaladı! **??",
    "{}, {}**'nin yüzüne 200 $ fırlattı!**??",
    "{}, {}**'nin yüzüne bir şişe kola döktü! **??",
    "{}, {}**'nin üzerine tüplü TV fırlattı!** ??",
    "{}, {}**'nin kalbini kırdı!**??",
    "{}, {}**'ye çiçek verdi **??",
    "{}, {}**'nin yanağından öptü ??**",
    "{}, {}**'nin internetinin kablosunu kopardı** ??",
    "{}, {}**'nin proje ödevini yırttı!**??",
    "{}, {}**'nin camına taş attı! **??",
    "{}, {}**'nin ağzına tuvalet terliği ile vurdu **??",
    "{}, {}**'nin kafasına pofuduk terlik fırlattı**??", 
    "{}, {}**'nin burnuna leblebi tıkadı** ??",
    "{}, {}**'nin dişini kırdı** ??",
    "{}, {}**'nin arabasının lastiğini patlattı** ??",
    "{}, {}**'nin ciğerini çıkarıp kedilere verdi **??",
    "{}, {}**'nin kolunu cimcirdi** ??",
    "{}, {}**'nin saçlarına sakız yapıştırdı** ??",
    "{}, {}**'yi Satürn'e kaçırdı** ??",
    "{}, {}**'nin saçlarına yıldız taktı** ??",
    "{}, {}**'yi Everest'in tepesinden aşağıya attı** ??",
    "{}, {}**'ye kız kulesinde çay ısmarladı** ??",
    "{}, {}**'yi valse davet etti**????",
]
sarkilar = (
	"{},\n\n {}, için şarkı önerdi :\n\n**Müslüm Gürses - ayrılık**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İsmail yk - Allah belanı versin**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Güllü - Unut gitsin**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Ceza - Holocost**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İbrahim Tatlıses - Mutlu Ol yeter**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İbrahim Tatlıses - Mavi Mavi**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mahsun Kırmızıgül - Beşminare",
	"{},\n\n {}, için şarkı önerdi :\n\n**Halay - Delilo**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Derya uluğ - okyanus**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İntizar - Bu senede kahpelik moda**",
        "{},\n\n {}, için şarkı önerdi :\n\n**Ahmet Kaya - Arka Mahalle**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Herai Zerdüş - Mavi**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Herai Zerdüş - Sevgilim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Taladro - Dem**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Cem Karaca - Ben Ekmeğimi Böldüm de Yedim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İbrahim Erkal - Gönül**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Tripkolic - Gözlerinin Yeşilini Özledim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Dilber Ay - Zorundamıyım**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İbrahim Tatlıses - Aramam**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Kıraç - Yalnızlığın Kapıları**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Ahmet Kaya - Bu Yalnızlık Benim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Rei - Ah Canım Sevgilim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İbrahim Erkal - Çare Gelmez**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Bayhan - Tiryakinim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Ali Kınık - Ben Seni Severken Çocuk Gibiyim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Yıldız Tilbe - Yürü Anca Gidersin**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Yıldız Tilbe - Şarkıların Şarkısı",
	"{},\n\n {}, için şarkı önerdi :\n\n**İntizar - Uykum Firari**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Hadise - Aşk Kaç Beden Giyer**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Berk Baysal - Zamanla Geçer**",
        "{},\n\n {}, için şarkı önerdi :\n\n**Ahmet Kaya - Yakamoz**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Tarkan - Kuzu Kuzu**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Herai Zerdüş - Sende Beni Sevdin mi?**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Taladro - Deniz Kızı**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Ankaralı Yasemin - Çıldıralım**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Davut Güloğlu - Nurcanım**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Nalan - Acemi Balık**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mustafa Sandal - Aşka yürek gerek**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İbrahim Tatlıses - Leylim ley**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Nil İpek - Son Mektup**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Blok3 - Affetmem**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Blok3 - Vur**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mustafa Yıldızdoğan - Ölür müydün?**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İntizar - Ihlamurlar Altında**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Zara - Seni Yazdım Kalbime**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Zara - Beni Unutma**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Yıldız Tilbe - Emi",
	"{},\n\n {}, için şarkı önerdi :\n\n**Ebru Yaşar - Yoksun**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Burak Bulut - Cano**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Sura İskenderli - Dinle**",
        "{},\n\n {}, için şarkı önerdi :\n\n**Nahide babashlı - Söz Verdim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Deniz Toprak - Bilmeden Oldu**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mustafa Ceceli - Gün Ağarmadan**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Semicenk - Kader Sağolsun**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Semicenk - Batık Gemi**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Kazım Koyuncu - Hayde**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Kazım Koyunca - Koyverdin Gittin**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Dilber Ay - Zoruna mı gitti gardaş**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İbrahim Tatlıses - Ayağında Kundura**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Gazapizm - Süzülerek**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Sezen Aksu - İki Gözüm**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Sezen Aksu - Herkes Yaralı**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Celal Yarıcı - Dışarda Mevsim Baharmış**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Celal Yarıcı - Seni Sevmeyen Ölsün**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Sinan Akçıl - Bir Zamanlar Deli Gönlüm**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mustafa Ceceli - Maşallah**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Sezen Aksu - Tükeneceğiz",
	"{},\n\n {}, için şarkı önerdi :\n\n**Gülnare - Bir Yari var**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Merve Özbey - Haram**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Onurcan Özcan - Yaramızda Kalsın**",
        "{},\n\n {}, için şarkı önerdi :\n\n**Ahmet Kaya - Söyle**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Ahmet Kaya - Beni vur**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mustafa Ceceli- Sevgilim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Ahmet Kaya - Kum Gibi**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Cem Karaca - Dağlar Dağlar**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Emircan İğrek - Müzik Kutusu**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Tripkolic - Koyu Kahverengi**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Selda Bağcan - Sivasın Yollarına**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Tarkan - Öp**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Manga - Cevapsız Sorular**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Müslüm Gürses - Nilüfer**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Müslüm Gürses - Yıllar Utansın**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Hakkı Bulut - Kıskanıyorum**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Emircan İğrek - Can Dostum**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mabel Matiz - Sultan Süleyman**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mabel Matiz - Antidepresan**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Ümit Besen - Nikah Masası",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mor Ve Ötesi - Bir Derdim Var**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Seksendört - Ölürüm Hasretinle**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Model - Pembe Mezarlık**",
        "{},\n\n {}, için şarkı önerdi :\n\n**Ahmet Kaya - Metrisin önü**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Herai Zerdüş - Papatya**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Belkıs Akkale - Dağlar seni delik delik delerim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Sıla - Boş Yere**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İzzet Altınmeşe - Maden Dağı**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Neşet Ertaş - Gönül Dağı**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Uygar Doğanay- Duydum Bir oğlun Olmuş**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Şehinşah - Nabız**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Neşet Ertaş - Ah Yalan Dünya**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Gazapizm - Heyecanı Yok**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mehmet Akça - Bakma Doktor Yarama**",
)

sarki1 = [ 
	"Yaw sahibime neden Şarkı önereyim.😂",
	"Sahibime Şarkı Önermem O zaten Kendi Bilir ne dinleyeceğini 🥳",
]
sarki2 = [ 
	"Yaw kendi kendime şarkı önermem ben botum 😁",
	"Ben şarkı dinlemem ben botum canım ❤️ ",
]

dontslapme = [
    "**Yahu beni niye tokatlamaya çalışıyorsun** 🥺",
    "😳😳",
    "**Bunu yapmayacağım** 😊",
    "** :Dsfgasd?**",
    "**Kendimi tokatlattırmayacağım.** 😑"
]
dontslapown = [
    "**Sahibimi tokatlayamam :/**",
    "**Bunu çok istiyorum ama yapamam** 😔",
    "**Şaka yapıyor olmalısın :D**",
    "**Keşke mümkün olsa...**"
]