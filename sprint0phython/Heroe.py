class Heroe:
    def __init__(self,nombreHeroe):
        self.ataque = int(10)
        self.defensa = int(5)
        self.salud = int(100)
        self.SALUD_MAX = int(100)
        self.nombreHeroe=nombreHeroe

    def atacar (self,enemigo):
        daño = self.ataque - enemigo.defensaEnemigo
        print("Heroe ataca a " + enemigo.nombreEnemigo + ".")
        if daño > 0:
            print("El enemigo" +  enemigo.nombreEnemigo + "ha recibido " + daño + "puntos de daño.")
        else:
            print("El enemigo a bloqueado el ataque.")


    def curarse (self):
        self.salud
        if self.salud > self.SALUD_MAX:
            self.salud = self.SALUD_MAX
        print("Heroe se ha curado. Salud actual: " + str(self.salud) + ".")

    def defenderse (self):
        self.defensa = self.defensa + 5
        print("Héroe se defiende. Defensa aumentada temporalmente a " + self.defensa + ".")
    def reset_defensa(self):
        self.defensa = self.defensa - 5
        print("La defensa de "+ self.nombreHeroe + " vuelve a la normalidad.")
    def esta_vivo(self):
        if self.salud > 0:
            return True
        else:
            return False