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