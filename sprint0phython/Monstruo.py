class Monstruo:
    def __init__(self):
        self.nameMonster = "Montruo"
        self.attack = int(10)
        self.defense = int(5)
        self.health = int(100)

    def atacar(self, hero):
        damage = self.attack - hero.defense
        print("El monstruo " + self.nameMonster + "ataca a " + hero.nameHero + ".")
        if damage > 0:
            print("El héroe " + hero.nameHero + " ha recibido " + damage +" puntos de daño.")
        else:
            print("El héroe ha bloqueado el ataque.")