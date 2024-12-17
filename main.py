class Android:
    def __init__(self):
        self.hp = 100
        self.attack = 10
        self.deviancy = 5
    
    def change_deviancy(self, deviancy):
        self.deviancy += deviancy

    def get_damage(self, damage):
        self.hp -= damage

    def attack(self, enemy):
        enemy.get_damage(self.attack)

    def __add__(self, value):
        new_attack = self.attack + value
        return new_attack


class Connor(Android):
    def __init__(self):
        super().__init__()
        self.attack = 70

    def change_deviancy(self, deviancy):
        if deviancy > 50:
            self.attack = 50
        return super().change_deviancy(deviancy)

    def die(self):
        self.deviancy = 0
    

class Kara(Android):
    def __init__(self):
        super().__init__()
        self.deviancy = 60

    def die_Alice(self):
        self.hp = 0

    def change_deviancy(self, deviancy):
        if deviancy > 50:
            self.attack = 70
        return super().change_deviancy(deviancy)