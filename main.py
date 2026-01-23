# Bu program, [Proje Amacı] için Python dersi kapsamında geliştirilmiştir.
import string
import re
from collections import Counter

def metni_temizle(metin):
    """Metindeki noktalama işaretlerini kaldırır ve kelime listesi döndürür."""
    tablo = str.maketrans('', '', string.punctuation)
    temiz_metin = metin.translate(tablo)
    return temiz_metin.split()

def kelime_sayisi(metin):
    """Metin içindeki toplam kelime miktarını hesaplar."""
    kelimeler = metni_temizle(metin)
    return len(kelimeler)

def cumle_sayisi(metin):
    """Düzenli ifadeler (Regex) kullanarak metindeki cümle sayısını bulur."""
    # . ! veya ? işaretlerine göre metni böler
    cumleler = re.split(r'[.!?]+', metin)
    return len([c for c in cumleler if c.strip()])

def en_sik_kelime(metin):
    """Metinde en çok tekrar eden kelimeyi bulur."""
    kelimeler = metni_temizle(metin)
    if not kelimeler:
        return ""
    sayac = Counter(kelimeler)
    # En yüksek frekansa sahip ilk öğeyi döndürür
    # most_common(1) -> [('Kelime', sayı)] döndürür
    return sayac.most_common(1)[0][0]

def en_uzun_kelime(metin):
    """Metindeki en uzun karakterli kelimeyi belirler."""
    kelimeler = metni_temizle(metin)
    if not kelimeler:
        return ""
    return max(kelimeler, key=len)

def en_kisa_kelime(metin):
    """Metindeki en kısa karakterli kelimeyi belirler."""
    kelimeler = metni_temizle(metin)
    if not kelimeler:
        return ""
    return min(kelimeler, key=len)

def kelime_tekrar(metin, kelime):
    """Belirli bir kelimenin metin içinde kaç kez geçtiğini sayar."""
    kelimeler = metni_temizle(metin)
    return kelimeler.count(kelime)

def main():
    """Programın ana giriş noktası."""
    girilen_metin = input("Metni giriniz: ")
    
    toplam_karakter = len(girilen_metin)
    
    aranacak = input("Aranacak kelimeyi giriniz: ")
    
    # Sonuçların ekrana yazdırılması
    print("-" * 30)
    print(f"Toplam karakter sayısı: {toplam_karakter}")
    print(f"Kelime sayısı: {kelime_sayisi(girilen_metin)}")
    print(f"Cümle sayısı: {cumle_sayisi(girilen_metin)}")
    print(f"En sık geçen kelime: {en_sik_kelime(girilen_metin)}")
    print(f"En uzun kelime: {en_uzun_kelime(girilen_metin)}")
    print(f"En kısa kelime: {en_kisa_kelime(girilen_metin)}")
    print(f"\"{aranacak}\" kelimesi metinde {kelime_tekrar(girilen_metin, aranacak)} kez geçmektedir")

if __name__ == "__main__":

    main()
