class Monstruo:
    # inicializar atributos del monstruo
    attack = int(15)
    defense = int(5)
    health = int(100)
    nameMonster = "Monstruo"

    def __init__(self):
         pass
    def atacar(self, hero):
        damage = self.attack - hero.defense
        print("El monstruo " + self.nameMonster + " ataca a " + hero.nameHero + ".")
        #control de si se inflingió daño
        if damage > 0:
            print("El héroe " + hero.nameHero + " ha recibido " + str(damage) +" puntos de daño.")
        else:
            print("El héroe ha bloqueado el ataque.")
            #le bajamos la vida al heroe
        hero.health -= damage

    def esta_vivo(self):
        # control de que el monstruo sigue vivo
        if self.health > 0:
            return True
        else:
            return False

