class Heroe:
    def __init__(self,nameHero):
        self.attack = int(10)
        self.defense = int(5)
        self.health = int(100)
        self.MAX_HEALTH = int(100)
        self.nameHero=nameHero

    def atacar (self,enemy):
        damage = self.attack - enemy.defense
        print("Heroe ataca a " + enemy.nameMonster + ".")
        if damage > 0:
            print("El enemigo" +  enemy.nameMonster + "ha recibido " + damage + "puntos de daño.")
        else:
            print("El enemigo a bloqueado el ataque.")


    def curarse (self):
        self.health = self.health + self.MAX_HEALTH
        if self.health > self.MAX_HEALTH:
            self.health = self.MAX_HEALTH
        print("Heroe se ha curado. Salud actual: " + str(self.health) + ".")

    def defenderse (self):
        self.defense = self.defense + 5
        print("Héroe se defiende. Defensa aumentada temporalmente a " + self.defense + ".")
    def reset_defensa(self):
        self.defense = self.defense - 5
        print("La defensa de "+ self.nameHero + " vuelve a la normalidad.")
    def esta_vivo(self):
        if self.health > 0:
            return True
        else:
            return False