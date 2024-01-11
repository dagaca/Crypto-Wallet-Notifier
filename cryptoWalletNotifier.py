import requests
import time
import winsound  # Windows için ses çalma kütüphanesi
import keyboard
import sys

# API endpoint ve cüzdan adresi
API_URL = "API_URL_ADDRESS"  # PolygonScan veya başka bir servis sağlayıcısının API URL'si
API_KEY = "YOUR_API_KEY"  # Servis sağlayıcısından alınan API anahtarı
WALLET_ADDRESS = "WALLET_ADDRESS"  # İzlenen cüzdanın adresi
TOKEN_CONTRACT_ADDRESS = "TOKEN_CONTRACT_ADDRESS"  # Takip edilen tokenın kontrat adresi

# Belirli bir tokenın varlığını sorgulamak için API isteği için parametreler
PARAMS = {
    'module': 'account',
    'action': 'tokenbalance',
    'contractaddress': TOKEN_CONTRACT_ADDRESS,
    'address': WALLET_ADDRESS,
    'apikey': API_KEY,
}

THRESHOLD = 500  # NOT: Bu değeri kontrol etmek istediğiniz değer olarak güncelleyin

def send_notification(message):
    """Bildirim gönderme fonksiyonu."""
    print(message)
    winsound.Beep(1000, 4000)  # Windows için bildirim sesi çalma (4 saniye)

def main():
    """Ana program döngüsü."""
    try:
        while True:
            # API'ye istek gönderme
            response = requests.get(API_URL, params=PARAMS)
            data = response.json()

            # API'den alınan verileri işleme
            token_balance_str = data.get('result', '0')  # Result anahtarından token varlığı alınır

            # Veriyi ondalık olarak işleme
            token_balance = float(token_balance_str) / 1e18  # 1e18'e bölerek ondalık değeri elde edin

            # Eğer token varlığı belirlenen eşik değerini aşıyorsa bildirim gönder
            if token_balance > THRESHOLD:
                message = f"Bildirim: Token varlığı {THRESHOLD}'ün üzerine çıktı! ({token_balance} BTC)"
                send_notification(message)

            time.sleep(120)  # Her 2 dakikada bir kontrol etmek için bekleyin

            # Q tuşuna basıldığında programı kapat
            if keyboard.is_pressed('q'):
                print("\nProgram kapatılıyor...")
                sys.exit(0)

    except KeyboardInterrupt:
        print("\nProgram kapatılıyor...")
        sys.exit(0)

if __name__ == "__main__":
    main()
