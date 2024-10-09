class Monstruo:
    # inicializar atributos del monstruo
    def __init__(self):
        self.nameMonster = "Montruo"
        self.attack = int(10)
        self.defense = int(5)
        self.health = int(100)

    def atacar(self, hero):
        damage = self.attack - hero.defense
        print("El monstruo " + self.nameMonster + "ataca a " + hero.nameHero + ".")
        #control de si se inflingió daño
        if damage > 0:
            print("El héroe " + hero.nameHero + " ha recibido " + damage +" puntos de daño.")
        else:
            print("El héroe ha bloqueado el ataque.")

    def esta_vivo(self):
        # control de que el monstruo sigue vivo
        if self.health > 0:
            return True
        else:
            return False