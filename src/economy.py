import random

class Economy:
    def __init__(self):
        
        self.credits = 100  
        self.ammo = 30     
        self.bombardments = 0 
        self.purchases = {'ammo': 0, 'repair': 0, 'bomb': 0, 'refinery': 0} 

    def get_price(self, item, alive_ships_count):
        if item == 'ammo': base_price = 100
        elif item == 'repair': base_price = 250
        elif item == 'bomb': base_price = 300
        elif item == 'refinery': base_price = 400
        else: return 0
        
        multiplier = 1.5 ** self.purchases.get(item, 0)
        price = base_price * multiplier
        
        if alive_ships_count == 1:
            price *= 0.2 
            
        return int(price)

    def apply_passive_income(self, has_refinery):
        self.credits += 25
        if has_refinery:
            self.credits += 50
        return self.credits

    def buy_item(self, item, player_ships):
        alive = sum(1 for ship in player_ships if not getattr(ship, 'is_sunk', lambda: False)())
        price = self.get_price(item, alive)
        
        if self.credits >= price:
            if item == 'ammo':
                self.ammo += 10
                self.credits -= price
                self.purchases['ammo'] += 1
                print(f"[Sklep] Kupiono amunicję. Stan: {self.ammo}")
                return True
                
            elif item == 'repair':
                repaired = False
                for ship in player_ships:
                    if not getattr(ship, 'is_sunk', lambda: False)():
                        if hasattr(ship, 'health') and type(ship.health) is list:
                            if False in ship.health:
                                idx = ship.health.index(False)
                                ship.health[idx] = True 
                                repaired = True
                                break
                        elif hasattr(ship, 'hp') and hasattr(ship, 'max_hp'):
                            if getattr(ship, 'hp') < getattr(ship, 'max_hp'):
                                ship.hp += 1
                                repaired = True
                                break
                                
                if repaired:
                    self.credits -= price
                    self.purchases['repair'] += 1
                    print("[Sklep] Sukces: Naprawiono jeden moduł statku!")
                    return True
                else:
                    print("[Sklep] Błąd: Wszystkie statki są w pełni sprawne.")
                    return False
                    
            elif item == 'bomb':
                self.bombardments += 1
                self.credits -= price
                self.purchases['bomb'] += 1
                print(f"[Sklep] Kupiono nalot dywanowy (bombę). Stan: {self.bombardments}")
                return True
                
            elif item == 'refinery':
                has_refinery = any(getattr(s, 'is_refinery', False) and not getattr(s, 'is_sunk', lambda: False)() for s in player_ships)
                if not has_refinery:
                    alive_ships_list = [s for s in player_ships if not getattr(s, 'is_sunk', lambda: False)()]
                    if alive_ships_list:
                        chosen_ship = random.choice(alive_ships_list)
                        chosen_ship.is_refinery = True
                        self.credits -= price
                        self.purchases['refinery'] += 1
                        print("[Sklep] Sukces: Zainstalowano rafinerię na losowym statku!")
                        return True
                    else:
                        print("[Sklep] Błąd: Brak żywych statków do instalacji rafinerii.")
                        return False
                else:
                    print("[Sklep] Błąd: Twoja flota posiada już działającą rafinerię.")
                    return False
        else:
            print(f"[Sklep] Odrzucono: Brak funduszy na {item}. Masz {self.credits}, potrzeba {price}.")
            return False
            
        return False