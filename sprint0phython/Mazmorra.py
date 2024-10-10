from Tesoro import Tesoro

from Monstruo import Monstruo
import random

class Mazmorra: #inicializamos los atributos

    def __init__(self,hero):
        self.monster = Monstruo()
        self.hero = hero
        self.treasure = Tesoro()

    def jugar(self):
        dead_monsters = 0

        print("Héroe entra en la mazmorra.")
        number_of_monsters = random.randint(1,5)
        while dead_monsters < number_of_monsters:
            print("Te has encontrado con un " + self.monster.nameMonster + ".")
            while self.hero.esta_vivo() and self.monster.esta_vivo():
                self.enfrentar_enemigo(self.monster)
            if not self.monster.esta_vivo():
                self.encontrar_tesoro()
                dead_monsters += 1
            else:
                print("Héroe ha sido derrotado en la mazmorra.")
                dead_monsters = 10

        if dead_monsters < 6:
            print("¡" + self.hero.nameHero + " ha derrotado a todos los monstruos y haconquistado la mazmorra!")


    def enfrentar_enemigo(self,enemy):
        #ataca el jugador
        #menu de acciones
        print("¿Qué deseas hacer?")
        print("1. Atacar")
        print("2. Defender")
        print("3. Curarse")
        op = int(input())
        #control de la acción
        if op == 1:
            self.hero.atacar(self.monster)
        elif op ==2:
            self.hero.defenderse()
        elif op ==3:
            self.hero.curarse()
        else:
            print("Opción no válida.")
        #ataca el enemigo
        if enemy.esta_vivo():
            enemy.atacar(self.hero)

    def encontrar_tesoro(self):
        #recibir un tesoro
        print("Buscando tesoro...")
        self.treasure.encontrar_tesoro(self.hero)
