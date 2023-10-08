class Player:
    def __init__(self, name, ap):
        print('我诞生了')
        self.name = name
        self.ap = ap
        self.hp = 100

    def attack(self, target):
        print(self.name, 'attacking', target.name)
        target.hp = target.hp - self.ap


p1 = Player('Player1', 5)
p2 = Player('Player2', 10)
p1.attack(p2)
print(p2.hp)
