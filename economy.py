"""
================================================================================
Project: Zadanie_NPG (Battleships Game)
Module: economy.py
Author: Patryk Jacak
Version: 1.1
Description: 
Moduł odpowiedzialny za zarządzanie pieniędzmi gracza, obliczanie cen w sklepie
biorąc pod uwagę inflacje oraz wszystkie transakcje np. nagroda za trafieni okrętu
================================================================================
"""

class Economy:
    def __init__(self, starting_credits=1000):
        # Główny portfel
        self.credits = starting_credits
        
        # Słownik do śledzenia liczby zakupów (kluczowe dla inflacji)
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
        
        # Flaga dla bonusu "Last Chance"
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