# Zadanie_NPG

Franek - mechanika gry  
Michał - mapa  
Małgorzata - klasy statków  
Patryk - ekonomia  
Rafał - integracja i działanie przeciwnika


# ⚓ Projekt Statki

Witamy w zaawansowanej wersji klasycznej gry w statki! Projekt został stworzony z myślą o dynamicznej rozgrywce oraz rozbudowanej ekonomii.

---

## 📝 Zasady Gry

Gra toczy się na dwóch mapach o rozmiarze **15x15**. Celem gry jest zatopienie całej floty przeciwnika przy jednoczesnym dbaniu o własne zasoby i fundusze.

### 1. Fazy Rozgrywki
Gra podzielona jest na cztery cykliczne fazy:

* **📍 SETUP (Rozstawianie):** Gracze rozmieszczają swoje statki na mapie. Możesz obracać statki, aby stworzyć nieprzewidywalną formację.
* **🎯 SHOOT (Ostrzał):** Wybierasz pole na mapie komputera. Każdy strzał zużywa **1 jednostkę amunicji**. Jeśli trafisz, otrzymujesz kredyty!
* **💰 SHOP (Sklep):** Za zarobione pieniądze możesz naprawić statki, dokupić amunicję lub zainwestować w ulepszenia.
* **🌊 MOVE (Ruch):** Po każdej turze cała flota przesuwa się o jeden krok. Statki odbijają się od krawędzi mapy, co całkowicie zmienia sytuację taktyczną.

---

### 💵 System Ekonomiczny

| Akcja / Przedmiot | Koszt / Zysk | Opis |
| :--- | :--- | :--- |
| **Trafienie masztu** | +50 CR | Nagroda za celny strzał. |
| **Zatopienie statku** | +150 CR | Premia za całkowite wyeliminowanie jednostki. |
| **Złoty Skarb** | +200 CR | Pojawia się losowo. Wpłyń na niego, by zebrać bonus. |
| **Pasywny dochód** | +25 CR / tura | Stały dopływ gotówki w każdej turze. |
| **Amunicja (+10)** | Cena bazowa: 100 CR | Niezbędna do prowadzenia ostrzału. |
| **Naprawa (1 HP)** | Cena bazowa: 250 CR | Przywraca sprawność jednemu masztowi. |

> [!IMPORTANT]
> **Inflacja:** Każdy kolejny zakup tego samego przedmiotu zwiększa jego cenę o 50%!
> **Last Chance:** Jeśli zostanie Ci tylko jeden statek, otrzymujesz **80% zniżki** w sklepie!

---

### 🛠️ Specjalne Jednostki i Mechaniki

* **🏭 Rafineria:** Możesz ulepszyć statek do roli Rafinerii. Zwiększa ona pasywny dochód o **+50 CR**.

---

## 💻 Technologie
* **Język:** Python 3.x
* **Biblioteka:** Pygame
