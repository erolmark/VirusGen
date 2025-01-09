import os
import shutil
from tqdm import tqdm
from time import sleep

def logo():
    """Logoyu bloklu şekilde göster."""
    print("\033[1;36m")  # Turkuaz renkte yazı
    print("#" * 40)
    print("#" + " " * 10 + "VERSATECH" + " " * 10 + "#")
    print("#" * 40)
    print("\033[0m")  # Renk sıfırlama

def menu():
    """Kullanıcıya seçenekleri sunar."""
    print("\033[1;34m")  # Mavi renkte yazı
    print("Lütfen bir APK seçeneği belirleyin:")
    print("\033[0m")  # Renk sıfırlama
    print("\033[1;33m")  # Sarı renkte yazı
    print("1 - Uygulama 1")
    print("2 - Uygulama 2")
    print("3 - Uygulama 3")
    print("0 - Çıkış")
    print("\033[0m")  # Renk sıfırlama

def apk_indir(secim):
    """APK dosyasını belirlenen dizine indirir."""
    apk_klasoru = "apk_dosyalar"  # APK dosyalarının bulunduğu klasör
    hedef_klasor = "/storage/emulated/0/VersaTech"  # İndirilen dosyaların hedefi

    apk_dosyasi = {
        1: "apks/FnafPhp.apk",
        2: "apks/ErolSigmaNigga.apk",
    }.get(secim, None)

    if apk_dosyasi:
        kaynak_dosya = os.path.join(apk_klasoru, apk_dosyasi)

        if os.path.exists(kaynak_dosya):
            # Hedef klasör yoksa oluştur
            if not os.path.exists(hedef_klasor):
                os.makedirs(hedef_klasor)

            hedef_dosya = os.path.join(hedef_klasor, apk_dosyasi)

            # Yüklenme animasyonu
            with tqdm(total=100, desc="İndiriliyor", bar_format="{l_bar}{bar} [Zaman: {elapsed}]") as pbar:
                for _ in range(5):  # Yükleme simülasyonu için 5 adım
                    sleep(0.5)  # Yükleme hızını simüle etmek için bekleme
                    pbar.update(20)

            # Dosyayı kopyala
            shutil.copy(kaynak_dosya, hedef_dosya)
            print("\033[1;32m")  # Yeşil renkte yazı
            print(f"{apk_dosyasi} başarıyla indirildi!")
            print(f"İndirilen dosya: {hedef_dosya}")
            print("\033[0m")  # Renk sıfırlama
        else:
            print("\033[1;31m")  # Kırmızı renkte yazı
            print("Hata: Seçilen APK dosyası bulunamadı!")
            print("\033[0m")  # Renk sıfırlama
    else:
        print("\033[1;31m")  # Kırmızı renkte yazı
        print("Geçersiz bir seçim yaptınız!")
        print("\033[0m")  # Renk sıfırlama

def main():
    """Ana program döngüsü."""
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')  # Konsolu temizle
        logo()
        menu()

        try:
            secim = int(input("Seçiminizi yapın: "))
            if secim == 0:
                print("Çıkış yapılıyor...")
                sleep(1)
                break
            elif secim in [1, 2, 3]:
                apk_indir(secim)
            else:
                print("Geçersiz bir seçim! Lütfen tekrar deneyin.")
        except ValueError:
            print("Hatalı giriş! Lütfen bir sayı girin.")
        sleep(2)

if __name__ == "__main__":
    main()
