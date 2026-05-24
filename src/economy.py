"""
================================================================================
Project: Zadanie_NPG (Battleships Game)
Module: economy.py
Author: Patryk Jacak
Version: 1.5
Description: 
Moduł odpowiedzialny za zarządzanie pieniędzmi gracza, obliczanie cen w sklepie
uwzględniając inflację, proces transakcji, naprawę masztów, system nagród 
oraz pasywny dochód.
================================================================================
"""

class Economy:
    def __init__(self, starting_credits=1000):
        self.credits = starting_credits
        self.items_bought = {
            "ammo": 0,
            "repair": 0,
            "upgrade": 0
        }
        self.base_prices = {
            "ammo": 100,
            "repair": 250
        }
        self.last_chance_active = False

    def get_item_price(self, item_name):
        if item_name not in self.base_prices:
            return None
            
        base = self.base_prices[item_name]
        bought_count = self.items_bought.get(item_name, 0)
        current_price = base + (bought_count * 0.5 * base)
        
        if self.last_chance_active:
            current_price *= 0.2
            
        return int(current_price)

    def add_reward(self, hit_type):
        rewards = {
            "hit": 50,
            "sink": 150
        }
        reward = rewards.get(hit_type, 0)
        self.credits += reward
        return reward

    def apply_passive_income(self):
        income = 25
        self.credits += income
        return income

    def buy_item(self, item_name, ship=None):
        if item_name == "repair":
            if ship is None:
                print("[Sklep] Błąd: Aby dokonać naprawy, musisz wskazać uszkodzony statek.")
                return False
            if hasattr(ship, 'hp') and hasattr(ship, 'max_hp'):
                if ship.hp >= ship.max_hp:
                    print("[Sklep] Błąd: Ten okręt jest w pełni sprawny! Nie potrzebuje naprawy.")
                    return False

        price = self.get_item_price(item_name)
        if price is None:
            print(f"[Sklep] Błąd: Przedmiot '{item_name}' nie istnieje w ofercie.")
            return False
            
        if self.credits < price:
            print(f"[Sklep] Brak funduszy na zakup {item_name}. Potrzebujesz: {price}, posiadasz: {self.credits}.")
            return False
            
        self.credits -= price
        
        if item_name == "repair" and ship is not None:
            if hasattr(ship, 'hp'):
                ship.hp += 1
                print(f" [Sklep] Naprawiono 1 maszt statku! Nowe HP okrętu: {ship.hp}")
        
        if item_name in self.items_bought:
            self.items_bought[item_name] += 1
        else:
            self.items_bought[item_name] = 1
            
        print(f"[Sklep] Zakupiono udanie: {item_name} za {price} kredytów.")
        return True