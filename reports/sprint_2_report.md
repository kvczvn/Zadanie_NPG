# Data raportu: 12.05.2026

## 1. METRYKA SPOTKANIA

| Dzień | Godzina | Miejsce/Platforma | Uczestnicy |
| :--- | :--- | :--- | :--- |
| 12.05.2026 | 17:00 - 19:15 | Discord | Patryk, Małgorzata, Franek, Rafał, Michał |

---

## 2. AGENDA I USTALENIA

Podsumowanie tego, co udało się omówić i jakie decyzje zapadły:
- Zaprojektowanie backendu ekonomicznego (klasa portfela, transakcje, mechanizmy inflacyjne).
- Integracja struktur danych masztów okrętowych z logiką punktów wytrzymałości (HP).
- Inicjalizacja centralnej struktury raportowania i dokumentacji postępów prac.

---

## 3. STATUS PRAC

Szczegółowy przebieg realizacji zadań w ramach **SPRINT 2: Rdzeń Rozgrywki i Logika Portfela**:

1. **Patryk Jacak (Scrum Master)**:
   - Wdrożenie produkcyjne klasy `Economy` (Issue #7).
   - Implementacja algorytmu progresywnego wzrostu cen towarów (Issue #18 – Inflacja amunicji).
   - Implementacja funkcji ratunkowej (Issue #25 – Bonus Last Chance 80%).

2. **Małgorzata**:
   - Zaktualizowanie i rozbudowa klasy `Ship` (Issue #6).
   - Wprowadzenie wewnętrznych list reprezentujących stan zniszczenia poszczególnych masztów.

3. **Franek**:
   - Bieżąca integracja zmian strukturalnych wewnątrz pliku głównego `statki.py` oraz zabezpieczanie spójności typów danych.

4. **Rafał & Michał**:
   - Kooperacja nad infrastrukturą dokumentacyjną – utworzenie katalogu `reports` oraz zainicjowanie centralnego pliku sprawozdań.

---

## 4. UWAGI I WNIOSKI NA KOLEJNY ETAP

Ważne spostrzeżenia, które musimy wziąć pod uwagę przy następnym sprincie:
- **Kamień milowy**: Integracja modułu finansowego ze strukturą statku, pozwalająca na dynamiczną modyfikację punktów życia jednostki poprzez zakup usługi naprawczej.
- **Wnioski**: Synchronizacja interfejsów metod klasy `Economy` na początku sprintu zapobiegła blokadom integracyjnym podczas łączenia gałęzi deweloperskich.
