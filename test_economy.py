"""
================================================================================
Project: Zadanie_NPG (Battleships Game)
Module: test_economy.py
Author: Patryk Jacak
Description: 
skrypt testowy do weryfikacji modułu economy.py .
================================================================================
"""
from economy import Economy

if __name__ == "__main__":
    print("=== [TEST] URUCHAMIANIE SYMULACJI SYSTEMU EKONOMII ===")
    
    game_eco = Economy(starting_credits=500)
    print(f"Stan początkowy konta: {game_eco.credits} kredytów\n")
    
    print("--- KROK 1: Początek tury (pasywny dochód) ---")
    income = game_eco.apply_passive_income()
    print(f"[Dochód] Przyznano: +{income} kredytów. Aktualny stan: {game_eco.credits}")
    
    print("\n--- KROK 2: Nagrody za trafienia ---")
    r1 = game_eco.add_reward("hit")
    r2 = game_eco.add_reward("sink")
    print(f"[Walka] Trafienie okrętu: +{r1} kredytów")
    print(f"[Walka] Zatopienie okrętu: +{r2} kredytów")
    print(f"Aktualny stan konta: {game_eco.credits} kredytów")
    
    print("\n--- KROK 3: Test Inflacji ---")
    print(f"Cena bazowa amunicji: {game_eco.get_item_price('ammo')} kredytów")
    game_eco.buy_item("ammo")
    print(f"Cena amunicji po 1. zakupie: {game_eco.get_item_price('ammo')} kredytów")
    game_eco.buy_item("ammo")
    print(f"Cena amunicji po 2. zakupie: {game_eco.get_item_price('ammo')} kredytów")
    
    print("\n--- KROK 4: Sytuacja krytyczna + Test logiki naprawy masztu (#30) ---")
    
    class MockShip:
        def __init__(self):
            self.hp = 2
            self.max_hp = 3

    test_ship = MockShip()
    print(f"Stan techniczny okrętu przed naprawą: {test_ship.hp}/{test_ship.max_hp} masztów")
    print(f"Cena naprawy przed bonusem: {game_eco.get_item_price('repair')} kredytów")
    
    game_eco.last_chance_active = True
    print("Aktywowano system 'Last Chance'")
    print(f"Nowa cena naprawy z rabatem 80%: {game_eco.get_item_price('repair')} kredytów")
    
    game_eco.buy_item("repair", ship=test_ship)
    print(f"Stan techniczny okrętu po naprawie: {test_ship.hp}/{test_ship.max_hp} masztów")
    
    print("\n=== [TEST] SYMULACJA ZAKOŃCZONA SUKCESEM ===")
    print(f"Końcowe kredyty: {game_eco.credits}")
    print(f"Słownik zakupów gracza: {game_eco.items_bought}")