#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın en gelişmiş otobüs bekleme simülatörü.
Şoför çay içmeyi bitirene kadar bekle.
"""

import time
import random

def neden_gelmiyor():
    nedenler = [
        "Şoför çay içiyor, simit de yiyor.",
        "Otobüsün lastiği patlamış, tamirci de çay içiyor.",
        "Trafik var ama aslında yok, sadece evren böyle.",
        "Otobüs senin ruhunu ölçüyor, sabrını test ediyor.",
        "Şoför 'bir dakika' dedi, o dakika 47 yıldır sürüyor."
    ]
    return random.choice(nedenler)

def bekle():
    print("Otobüs bekleniyor...")
    for i in range(1, 11):
        print(f"{i}. dakika geçti... Hâlâ yok.")
        time.sleep(0.5)  # Gerçek bekleme simülasyonu için artırabilirsin
        if i % 3 == 0:
            print(f"   → {neden_gelmiyor()}")
    print("\nÖZET: Otobüs gelmedi. Çünkü gelmeyecekti zaten.")
    print("Tavsiye: Yürü. Veya çay iç. Şoför gibi.")

if __name__ == "__main__":
    bekle()

# Gizli not: Bu simülasyon aslında hayatın kendisi. Beklersin, gelmez, alışırsın.
# Saklı anlam: Sabır taşı çatladığında otobüs de gelir, ama o zaman artık ihtiyacın kalmamıştır.
