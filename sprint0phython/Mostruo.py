class Mostruo:
    def __init__(self):
        self.nombreMonstruo = "Montruo"
        self.ataque = int(10)
        self.defensa = int(5)
        self.salud = int(100)

    def atacar(self, heroe):
        print("El monstruo " + self.nombreMonstruo + "ataca a " + heroe.nombreHeroe+ ".")