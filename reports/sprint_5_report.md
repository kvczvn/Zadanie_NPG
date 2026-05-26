# Data raportu: 23.05.2026

## 1. METRYKA SPOTKANIA

| Dzień | Godzina | Miejsce/Platforma | Uczestnicy |
| :--- | :--- | :--- | :--- |
| 23.05.2026 | 13:00 - 14:30 | Discord | Franek, Rafał, Michał, Patryk, Małgorzata |

---

## 2. AGENDA I USTALENIA

Podsumowanie tego, co udało się omówić i jakie decyzje zapadły:
- Kompleksowa refaktoryzacja kodu źródłowego i rozwiązanie konfliktów scalania (merge conflicts).
- Przygotowanie, przetestowanie i wdrożenie wersji gotowej do prezentacji.

---

## 3. STATUS PRAC

Szczegółowy przebieg realizacji zadań w ramach **SPRINT 5: Integracja Systemowa, Sztuczna Inteligencja i Finalizacja**:

1. **Franek (Scrum Master)**:
   - Integracja wszystkich podmodułów w jednolitą architekturę (Issue #33 – Wersja minimalna).
   - Oprogramowanie stanów pętli tury gracza (Issue #22) oraz widoku końcowego (Issue #24 – Game Over).

2. **Rafał**:
   - Refaktoryzacja modułu decyzyjnego – wdrożenie pamięci strzałów eliminującej dublowanie tych samych współrzędnych (Issue #21).
   - Obsługa wyjątków kolizji krawędziowych floty komputerowej (Issue #26).

3. **Michał**:
   - Projekt architektoniczny i wykonanie funkcji zbiorczej `draw_fleet_and_misses` oraz graficznego interfejsu menu sklepu (Issue #19).

4. **Patryk Jacak**:
   - Usunięcie skryptów symulacyjnych z kodu produkcyjnego, utworzenie niezależnego środowiska testowego `test_economy.py`.
   - Wdrożenie bezpiecznej logiki fizycznej naprawy punktów zdrowia poszczególnych masztów (Issue #30).

5. **Małgorzata**:
   - Dodanie dynamicznego zachowania do obiektów środowiskowych poprzez implementację metody `move` w klasie `Treasure` (Issue #31).

---

## 4. UWAGI I WNIOSKI NA KOLEJNY ETAP

Ważne spostrzeżenia, które musimy wziąć pod uwagę przy następnym sprincie:
- **Kamień milowy**: Rozwiązanie konfliktów scalania w module ekonomii i pomyślny merge wszystkich gałęzi do repozytorium `main`, kończący się w pełni uruchamialną aplikacją.
- **Wnioski**: Przeprowadzony Sprint Review oraz Retrospekcja pozwoliły podsumować wkład zespołu.
