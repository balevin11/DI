class Heroe:
    MAX_HEALTH = int(100)
    #inicializar atributos del heroe
    def __init__(self,namehero):
        self.attack = int(10)
        self.defense = int(5)
        self.health = int(100)

        self.nameHero=namehero

    def atacar (self,enemy):
        damage = self.attack - enemy.defense
        print("Heroe ataca a " + enemy.nameMonster + ".")
        #control de si se inflingió daño
        if damage > 0:
            print("El enemigo" +  enemy.nameMonster + "ha recibido " + damage + "puntos de daño.")
        else:
            print("El enemigo a bloqueado el ataque.")

    def curarse (self):
        #control salud no vaya a ser mayor a la salud máxima
        if self.health > self.MAX_HEALTH - 5:
            #aumento de la salud en 5 puntos
            self.health = self.health + 5
        print("Heroe se ha curado. Salud actual: " + str(self.health) + ".")

    def defenderse (self):
        #aumento de la defensa en 5 puntos
        self.defense = self.defense + 5
        print("Héroe se defiende. Defensa aumentada temporalmente a " + str(self.defense) + ".")

    def reset_defensa(self):
        #la defensa baja 5 puntos (a su estado incial)
        self.defense = self.defense - 5
        print("La defensa de "+ self.nameHero + " vuelve a la normalidad.")

    def esta_vivo(self):
        #control de que el heroe sigue vivo
        if self.health > 0:
            return True
        else:
            return False