import asyncio
from TikTokLive import TikTokLiveClient
from TikTokLive.events import ChestEvent
from telegram import Bot

# Telegram Bilgileri
TOKEN = "8646421782:AAGvDU3PzSCNQqiE1EyRcepr2rnivKuCGJs"
CHAT_ID = "-1004293699906"

# İzlencek TikTok yayıncılarının listesi
TARGET_USERS = [
    "Eyeaglereal00",
    "Queenziliya12",
    "rufet_02_",
    "Arif.bakinski",
    "ouhoud.hk",
    "ashkan.slemany",
    "banken054",
    "eqpej",
    "choko.natali",
    "chavoliveyedekk",
    "toshidensethu",
    "allok111",
    "xd133339998",
    "n___1z1",
    "daizrf",
    "izlenecekbirsey1",
    "bromennx",
    "estrella_7_8",
    "lindapassarinheira",
    "gurunglaxmi70",
    "loveru1224",
    "nora_mai_mai",
    "pattychan006",
    "primero_live",
    "aritan625",
    "06lolyy",
    "nanaka_73"
]

bot = Bot(token=TOKEN)

async def start_listener(username):
    client = TikTokLiveClient(unique_id=username)

    @client.on(ChestEvent)
    async def on_chest(event: ChestEvent):
        live_url = f"https://www.tiktok.com/@{username}/live"
        
        message_text = (
            "🎁 **YENİ TİKTOK SANDIĞI YAKALANDI!** 🎁\n\n"
            f"👤 **Yayıncı:** {username}\n"
            "⏰ **Sandık Açılmadan Yayına Katıl!**\n\n"
            f"🔗 **Canlı Yayın Linki:** {live_url}"
        )
        
        try:
            await bot.send_message(
                chat_id=CHAT_ID,
                text=message_text,
                parse_mode="Markdown"
            )
            print(f"[{username}] Sandık bildirimi gönderildi. 30 saniye bekleniyor...")
            await asyncio.sleep(30)
        except Exception as e:
            print(f"[{username}] Telegram mesajı gönderilemedi: {e}")

    try:
        print(f"[{username}] Yayını dinlenmeye başlandı...")
        await client.start()
    except Exception as e:
        print(f"[{username}] Bağlantı hatası veya yayın kapalı: {e}")

async def main():
    tasks = [start_listener(user) for user in TARGET_USERS]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
