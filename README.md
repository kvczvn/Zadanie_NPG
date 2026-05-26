# Zadanie_NPG

# ⚓ Projekt Statki
Projekt jest rozszerzoną wersją klasycznej gry w statki, przygotowaną w języku Python z wykorzystaniem biblioteki Pygame. Gra łączy tradycyjne zasady polegające na zatapianiu floty przeciwnika z dodatkowymi mechanikami, takimi jak ekonomia, amunicja, sklep, ruch statków, bombardowanie, rafineria oraz złoty skarb.
Gracz rywalizuje z komputerem. Każda strona posiada własną flotę statków rozmieszczoną na planszy. Celem gry jest zatopienie wszystkich statków przeciwnika, zanim komputer zatopi flotę gracza


## 📝 Podstawowe zasady Gry
1.	Każdy gracz posiada własną planszę o rozmiarze **15x15**.
2.	Na planszy rozmieszczone są statki.
3.	Przeciwnik nie zna położenia statków drugiej strony.
4.	Gracze na zmianę wybierają pola, w które chcą strzelić.
5.	Jeśli na wybranym polu znajduje się statek, następuje trafienie.
6.	Jeśli pole jest puste, strzał jest pudłem.
7.	Statek zostaje zatopiony, gdy wszystkie jego pola zostaną trafione.
8.	Wygrywa osoba, która jako pierwsza zatopi całą flotę przeciwnika.
W tej wersji gry zasady zostały rozszerzone o ekonomię, sklep, amunicję, ruch statków oraz dodatkowe akcje specjalne.

    

  
## 📝 Cel Gry
Celem gry jest zniszczenie całej floty komputera. Gracz robi to przez strzelanie w pola na planszy przeciwnika. Komputer również strzela w planszę gracza. Wygrywa ta strona, która jako pierwsza zatopi wszystkie statki przeciwnika.  
Gra kończy się, gdy:  
•	gracz zatopi wszystkie statki komputera — gracz wygrywa,  
•	komputer zatopi wszystkie statki gracza — gracz przegrywa.  

## Plansza gry
Gra toczy się na dwóch planszach o rozmiarze 15 × 15 pól:  
•	lewa plansza to plansza gracza,  
•	prawa plansza to plansza komputera.  
Na planszy gracza widoczne są własne statki. Na planszy komputera statki są ukryte, dopóki nie zostaną trafione lub zatopione.  

## Flota
W grze występują statki o różnych rozmiarach. Rozmiar statku oznacza liczbę pól, które zajmuje na planszy.
Flota składa się ze statków o długościach:  
4, 3, 3, 2, 2, 1, 1  
Każde pole statku można traktować jako jeden maszt lub jeden punkt życia. Jeżeli gracz albo komputer trafi w dane pole statku, ta część zostaje uszkodzona. Statek zostaje zatopiony dopiero wtedy, gdy wszystkie jego pola zostaną trafione.  

## Oznaczenia na planszy
W grze używane są następujące oznaczenia:  
Niebieskie pole	- Sprawny statek gracza  
Czerwone pole z X - Trafiona część statku  
Szare pole z O - Pudło  
Żółte kółko na statku - Dziób statku  
Zielony statek - Statek pełniący funkcję rafinerii  
Złote kółko - Złoty skarb  


## Fazy Rozgrywki
Gra składa się z kilku faz. Po zakończeniu jednej fazy gracz przechodzi do kolejnej.

### 1. SETUP — rozstawianie statków
Na początku gry gracz rozmieszcza swoje statki na lewej planszy.  
Gracz ustawia statki klikając pola na planszy. Statki są ustawiane po kolei, zgodnie z ich długością. Aktualnie ustawiany statek jest wskazany komunikatem na ekranie, np.:  
Rozstaw statek: 4 masztów.  
Przycisk na dole ekranu pozwala zmienić kierunek ustawiania statku:  
•	poziomo,  
•	pionowo.  
Statek nie może:  
•	wychodzić poza planszę,  
•	nakładać się na inny statek.  
Po rozmieszczeniu wszystkich statków rozpoczyna się właściwa gra.  

### 2. SHOOT — faza strzału
W tej fazie gracz strzela w planszę komputera, czyli w prawą planszę.  
Każdy zwykły strzał zużywa 1 jednostkę amunicji. Jeżeli gracz ma amunicję, może kliknąć dowolne pole na planszy komputera.  
Możliwe wyniki strzału:  
•	trafienie — jeśli na polu znajduje się statek komputera,  
•	pudło — jeśli pole jest puste.  
Za trafienia gracz otrzymuje kredyty:  
Akcja - Nagroda  
Trafienie części statku - +50 CR  
Zatopienie całego statku - dodatkowe +150 CR  
Po strzale gracza komputer wykonuje swój strzał w planszę gracza.  

### 3. SHOP — sklep
Po fazie strzału gracz przechodzi do sklepu. W sklepie można wykorzystać zdobyte kredyty na ulepszenia i pomoc w dalszej grze.  
Dostępne zakupy:  
Przedmiot - Cena bazowa - Działanie  
Amunicja +10 - 100 CR - Dodaje 10 jednostek amunicji  
Naprawa - 250 CR - Naprawia jedną trafioną część statku  
Nalot / bombardowanie - 300 CR - Pozwala wykonać atak obszarowy 2 × 5 pól  
Rafineria - 400 CR - Zamienia jeden żywy statek w rafinerię  
Po zakończeniu zakupów należy kliknąć przycisk:  
ZAKOŃCZ ZAKUPY  
Wtedy gra przechodzi do fazy ruchu.  

### 4. MOVE — ruch floty
W tej fazie statki mogą się przemieścić. Po kliknięciu przycisku:  
WYKONAJ RUCH  
cała flota gracza i komputera przesuwa się o jedno pole zgodnie z kierunkiem ruchu każdego statku.  
Jeżeli statek miałby wyjść poza planszę albo wejść w kolizję z innym statkiem, program próbuje go obrócić. Statki obracają się wokół dziobu, czyli ostatniego pola statku zaznaczonego żółtym kółkiem.  
W fazie ruchu gracz może również kliknąć własny statek, aby ręcznie obrócić go o 90 stopni wokół dziobu. Obrót zostanie wykonany tylko wtedy, gdy statek po obrocie:  
•	nadal mieści się na planszy,  
•	nie nachodzi na inny statek.  
Po wykonaniu ruchu gra wraca do fazy strzału.  

## System Ekonomiczny

Gra posiada system ekonomiczny oparty na kredytach oznaczanych jako CR.  
Na początku gry gracz posiada:  
- 100 CR  
- 30 jednostek amunicji  
- 0 bombardowań  
  
Kredyty można zdobywać przez:  
Źródło - Zysk  
Trafienie statku przeciwnika - +50 CR  
Zatopienie statku przeciwnika - +150 CR  
Złapanie złotego skarbu - +200 CR  
Pasywny dochód co turę - +25 CR  
Pasywny dochód z rafinerią - dodatkowe +50 CR  

## Inflacja cen
Każdy kolejny zakup tego samego przedmiotu zwiększa jego cenę. Cena rośnie według mnożnika 1,5.  
Oznacza to, że jeśli gracz kilka razy kupuje amunicję, każda kolejna paczka amunicji będzie droższa od poprzedniej.  

## Mechanika Last Chance
Jeżeli graczowi zostanie tylko jeden niezatopiony statek, aktywuje się mechanika:  
LAST CHANCE  
W tym trybie ceny w sklepie są obniżone o 80%.  
Dzięki temu gracz, który jest blisko przegranej, ma jeszcze szansę na odwrócenie sytuacji.  

## Amunicja
Amunicja jest potrzebna do wykonywania zwykłych strzałów.  
Każdy zwykły strzał zużywa:  
1 jednostkę amunicji  
Jeżeli graczowi skończy się amunicja, nie może wykonać zwykłego strzału. Może wtedy dokupić amunicję w sklepie, jeśli posiada odpowiednią liczbę kredytów.  

## Specjalne Jednostki i Mechaniki
### Bombardowanie  
Bombardowanie to specjalny atak obszarowy. Można je kupić w sklepie jako nalot.  
Po zakupie bombardowania w fazie strzału pojawia się przycisk:  
UŻYJ BOMBARDOWANIA  
Po jego kliknięciu gracz wybiera pole na planszy komputera. Bombardowanie obejmuje obszar:  
2 × 5 pól  
Atak działa od klikniętego pola w dół i w prawo. Oznacza to, że jednym bombardowaniem można trafić kilka części statków przeciwnika.  
Po użyciu bombardowania liczba dostępnych bombardowań zmniejsza się o 1.  

### Rafineria  
Rafineria to specjalne ulepszenie statku. Można ją kupić w sklepie.  
Po zakupie jeden losowy żywy statek gracza zostaje oznaczony jako rafineria. Taki statek ma zielony kolor.  
Rafineria zwiększa pasywny dochód gracza:  
+50 CR na turę  
Standardowy dochód pasywny wynosi +25 CR, więc z aktywną rafinerią gracz otrzymuje łącznie:  
75 CR na turę  
Rafineria działa tylko wtedy, gdy statek pełniący tę funkcję nie został zatopiony.  

### Złoty skarb
Na planszy gracza może pojawić się złoty skarb. Jest oznaczony złotym kółkiem.  
Skarb pojawia się na losowym wolnym polu, czyli takim, na którym nie stoi statek gracza. W trakcie gry skarb może przemieszczać się o jedno pole w losowym kierunku.  
Jeżeli statek gracza wpłynie na pole ze skarbem, gracz otrzymuje:  
+200 CR  
Następnie skarb pojawia się ponownie w innym losowym miejscu.  

## Ruch statków
Jedną z najważniejszych różnic względem klasycznej gry w statki jest to, że statki nie pozostają cały czas w tym samym miejscu.  
Każdy statek posiada kierunek ruchu. Po zakończeniu zakupów i przejściu do fazy ruchu flota może przemieścić się o jedno pole.  
Jeżeli statek nie może przesunąć się dalej, bo:  
•	wyszedłby poza planszę,  
•	zderzyłby się z innym statkiem,  
program próbuje obrócić go o 90 stopni wokół dziobu.  
Dziób statku jest oznaczony żółtym kółkiem.  

## Trafienia, pudła i zatopienia
Każdy statek składa się z określonej liczby pól. Każde pole statku ma własny stan:  
•	sprawne,  
•	trafione.  
Jeśli wszystkie pola statku zostaną trafione, statek zostaje zatopiony.  
Przykład:  
Statek trzymasztowy zajmuje trzy pola. Jeśli trafione jest tylko jedno pole, statek nadal istnieje. Jeśli trafione zostaną wszystkie trzy pola, statek zostaje zatopiony.  

## Warunki zwycięstwa i przegranej
Gracz wygrywa, gdy wszystkie statki komputera zostaną zatopione.  
Na ekranie pojawi się wtedy komunikat:  
Wygrałeś! Zniszczyłeś flotę komputera!  
Gracz przegrywa, gdy komputer zatopi wszystkie statki gracza.  
Na ekranie pojawi się wtedy komunikat:  
Przegrałeś! Komputer zniszczył Twoją flotę.  


## 💻 Technologie
* **Język:** Python 3.x  
* **Biblioteka:** Pygame  
