"""
================================================================================
Project: Zadanie_NPG (Battleships Game)
Module: economy.py
Author: Patryk Jacak
Version: 1.3
Description: 
Moduł odpowiedzialny za zarządzanie pieniędzmi gracza, obliczanie cen w sklepie
uwzględniając inflację, system nagród oraz pasywny dochód.
================================================================================
"""

class Economy:
    def __init__(self, starting_credits=1000):
        # Główny portfel gracza
        self.credits = starting_credits
        
        # Słownik do śledzenia liczby zakupów (kluczowe dla inflacji #18)
        self.items_bought = {
            "ammo": 0,
            "repair": 0,
            "upgrade": 0
        }
        
        # Ceny bazowe zdefiniowane w dokumentacji 
        self.base_prices = {
            "ammo": 100,
            "repair": 250
        }
        
        # Flaga dla bonusu "Last Chance" (#25)
        self.last_chance_active = False

    def get_item_price(self, item_name):
        """
        Oblicza aktualną cenę przedmiotu uwzględniając inflację i bonusy.
        Zgodnie z Issue #18 i #25.
        """
        if item_name not in self.base_prices:
            return None
            
        base = self.base_prices[item_name]
        bought_count = self.items_bought.get(item_name, 0)
        
        # Formuła inflacji: +50% ceny bazowej za każdy kupiony przedmiot (#18)
        current_price = base + (bought_count * 0.5 * base)
        
        # Bonus Last Chance: -80% ceny (czyli płacimy 20%) (#25)
        if self.last_chance_active:
            current_price *= 0.2
            
        return int(current_price)

    def add_reward(self, hit_type):
        """
        Przyznaje nagrodę za akcje na polu bitwy.
        hit_type: 'hit' (trafienie) lub 'sink' (zatopienie).
        """
        rewards = {
            "hit": 50,
            "sink": 150
        }
        
        reward = rewards.get(hit_type, 0)
        self.credits += reward
        return reward

    def apply_passive_income(self):
        """
        Dodaje pasywny dochód co turę (Issue #25).
        Podstawowy dochód to 25 jednostek.
        """
        income = 25
        self.credits += income
        return income

    def buy_item(self, item_name):
        """
        Realizuje zakup przedmiotu przez gracza.
        Sprawdza dostępność kredytów, pobiera opłatę i aktualizuje licznik zakupów dla inflacji.
        """
        # 1. Sprawdź, czy przedmiot w ogóle istnieje w cenniku
        price = self.get_item_price(item_name)
        if price is None:
            print(f"[Sklep] Błąd: Przedmiot '{item_name}' nie istnieje w ofercie.")
            return False
            
        # 2. Sprawdź, czy gracz ma wystarczająco dużo kredytów
        if self.credits < price:
            print(f"[Sklep] Brak funduszy na zakup {item_name}. Potrzebujesz: {price}, posiadasz: {self.credits}.")
            return False
            
        # 3. Realizacja transakcji
        self.credits -= price
        
        # Zwiększamy licznik zakupów (to automatycznie podbije cenę na przyszłość przez inflację!)
        if item_name in self.items_bought:
            self.items_bought[item_name] += 1
        else:
            self.items_bought[item_name] = 1
            
        print(f"[Sklep] Zakupiono udanie: {item_name} za {price} kredytów.")
        return True