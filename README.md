# Crypto Wallet Notifier
Bu Python script'i, belirli bir kripto cüzdanındaki bir tokenin varlığını kontrol eder ve belirlenen eşik değerini aştığında kullanıcıya bildirim gönderir.

## Kullanım
1. Repoyu bilgisayarınıza klonlayın.
2. Gerekli bağımlılıkları yüklemek için terminal veya komut istemcisine aşağıdaki komutu girin:
   ```bash
   pip install requests keyboard
   ```
3. cryptoWalletNotifier.py dosyasını açarak aşağıdaki değerleri kendi bilgilerinizle güncelleyin:
   ```bash
   API_URL_ADDRESS = "API_URL_ADDRESS"  # Kripto blockchain sağlayıcısının API URL'si
   YOUR_API_KEY = "YOUR_API_KEY"  # API anahtarı
   WALLET_ADDRESS = "WALLET_ADDRESS"  # İzlenen cüzdanın adresi
   TOKEN_CONTRACT_ADDRESS = "TOKEN_CONTRACT_ADDRESS"  # Takip edilen tokenin kontrat adresi
   ```
4. cryptoWalletNotifier.py dosyasını çalıştırarak programı başlatın.

## Notlar
- **THRESHOLD değerini, kontrol etmek istediğiniz token miktarına göre güncelleyin.**
- **Programı kapatmak için herhangi bir zaman Q tuşuna basabilirsiniz.**

- Bu repo, çeşitli kripto blockchain sağlayıcılarının API'lerini kullanarak cüzdan adresinizdeki bir tokenin varlığını izlemek için başlangıç noktası olarak kullanılabilir.
