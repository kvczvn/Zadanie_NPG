# Data raportu: 15.05.2026

## 1. METRYKA SPOTKANIA

| Dzień | Godzina | Miejsce/Platforma | Uczestnicy |
| :--- | :--- | :--- | :--- |
| 15.05.2026 | 21.00 - 22:00 | Discord | Małgorzata, Michał, Franek, Rafał, Patryk |

---

## 2. AGENDA I USTALENIA

Podsumowanie tego, co udało się omówić i jakie decyzje zapadły:
- Konwersja surowych danych logicznych gry na reprezentację wizualną Pygame.
- Implementacja obsługi zdarzeń wejścia użytkownika (mysz/klawiatura).

---

## 3. STATUS PRAC

Szczegółowy przebieg realizacji zadań w ramach **SPRINT 3: Interfejs Użytkownika, Grafika i Interakcja**:

1. **Małgorzata (Scrum Master)**:
   - Zaprogramowanie zaawansowanej metody rotacji geometrycznej statku wokół jego dziobu (Issue #16).

2. **Michał**:
   - Stworzenie modułu renderującego `graphics.py` (Issue #5).
   - Implementacja globalnych stałych RGB dla zróżnicowanych stanów planszy.

3. **Franek**:
   - Implementacja algorytmu transformacji pikseli okna systemowego na współrzędne siatki logicznej gry (Issue #10).

4. **Rafał**:
   - Opracowanie ujednoliconego szkieletu dokumentacji inżynierskiej w formacie Markdown wewnątrz repozytorium.

5. **Patryk**:
   - Wsparcie przy integracji modułu graficznego z logiką ekonomiczną i testowanie poprawności wyświetlania stanu konta.

---

## 4. UWAGI I WNIOSKI NA KOLEJNY ETAP

Ważne spostrzeżenia, które musimy wziąć pod uwagę przy następnym sprincie:
- **Kamień milowy**: Wyświetlenie siatki taktycznej gry i mapowanie kliknięć kursora na konkretne indeksy tablicy dwuwymiarowej.
- **Wnioski**: Wykryto i sprawnie wyeliminowano problemy z przesunięciem (offsetem) renderowania obiektów względem siatki dzięki szybkiemu standupowi technicznemu.
