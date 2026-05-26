# Data raportu: 19.05.2026

## 1. METRYKA SPOTKANIA

| Dzień | Godzina | Miejsce/Platforma | Uczestnicy |
| :--- | :--- | :--- | :--- |
| 19.05.2026 | 17:00 - 19:45 | Discord | Michał, Małgorzata, Patryk, Rafał, Franek |

---

## 2. AGENDA I USTALENIA

Podsumowanie tego, co udało się omówić i jakie decyzje zapadły:
- Uruchomienie procedur autonomicznego poruszania się floty przeciwnika.
- Implementacja systemu losowego generowania skarbów i zasobów na mapie.
- Rozbudowa wymiarów planszy i wizualizacja zdarzeń (celne/niecelne strzały).

---

## 3. STATUS PRAC

Szczegółowy przebieg realizacji zadań w ramach **SPRINT 4: Zaawansowane Mechaniki i System Skarbów**:

1. **Michał (Scrum Master)**:
   - Wdrożenie renderowania rozszerzonej siatki o wymiarach 15x15 (Issue #9).
   - Graficzna wizualizacja niecelnych strzałów oznaczanych dedykowanym symbolem 'O' (Issue #32).

2. **Małgorzata**:
   - Implementacja klasy kontenerowej `Treasure` (Issue #23) odpowiedzialnej za algorytmiczne generowanie skrzyń ze złotem na losowych współrzędnych mapy.

3. **Patryk Jacak**:
   - Zaimplementowanie i otestowanie metody transakcyjnej `buy_item` (Issue #20).
   - Implementacja systemu natychmiastowego naliczania profitów finansowych za trafienie (hit) i zatopienie (sink) okrętu (Issue #13).

4. **Rafał**:
   - Zaprogramowanie algorytmu losowego, bezkolizyjnego rozstawiania floty AI (Issue #11).
   - Implementacja funkcji przesunięcia statków o określony wektor kierunkowy (Issue #17).

5. **Franek**:
   - Prace przygotowawcze pod integrację modułu sterowania turami z nowym rozmiarem siatki 15x15.

---

## 4. UWAGI I WNIOSKI NA KOLEJNY ETAP

Ważne spostrzeżenia, które musimy wziąć pod uwagę przy następnym sprincie:
- **Kamień milowy**: Pomyślne wdrożenie algorytmu automatycznego, bezkolizyjnego rozmieszczania floty przeciwnika na planszy.
- **Wnioski**: Wspólne spojrzenie na kod pozwoliło na zoptymalizowanie złożoności obliczeniowej algorytmu losowania pozycji floty, co zapobiegło zamrażaniu pętli gry.
