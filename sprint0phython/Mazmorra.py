from Tesoro import Tesoro
from Monstruo import Monstruo
import random

class Mazmorra:


    def __init__(self,hero):
        #inicializamos los atributos
        self.monster = None
        self.hero = hero
        self.treasure = Tesoro()

    def jugar(self):
        dead_monsters = 0
        print("Héroe entra en la mazmorra.")
        #creamos una variable con el número de enemigos en la mazmorra
        number_of_monsters = random.randint(1,5)
        #abrimos un bucle que va a durar mientras siga habiendo enemigos en la mazmorra
        while dead_monsters < number_of_monsters:
            #creamos un mostruo
            self.monster = Monstruo()
            print("Te has encontrado con un " + self.monster.nameMonster + ".")
            #la pelea continuará hasta que muera el enemigo o el heroe
            while self.hero.esta_vivo() and self.monster.esta_vivo():
                self.enfrentar_enemigo(self.monster)
            #comprobar quien murió
            #si muere el monstruo buscamos un tesoro y aumentamos en 1 el contador de enemigos muertos
            if not self.monster.esta_vivo():
                self.encontrar_tesoro()
                dead_monsters += 1
            else:
                #si muere el heroe mostramos mensaje y ponemos el contador de enemigos muertos en
                # un valor fuera del rango posible
                print("Héroe ha sido derrotado en la mazmorra.")
                dead_monsters = 10
        #comprobamos si el valor de enemigos muertos es un valor dentro del rango de enemigos posibles,
        #si no es asi es que el que murió fue el heroe
        if dead_monsters < 6:
            print("¡" + self.hero.nameHero + " ha derrotado a todos los monstruos y ha conquistado la mazmorra!")


    def enfrentar_enemigo(self,enemy):
        defended = False
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
            defended = True
        elif op ==3:
            self.hero.curarse()
        else:
            print("Opción no válida.")
        #ataca el enemigo
        if enemy.esta_vivo():
            enemy.atacar(self.hero)
            #si nos defendimos restauramos nuestra defensa
        if defended:
            self.hero.reset_defensa()
    def encontrar_tesoro(self):
        #recibir un tesoro
        print("Buscando tesoro...")
        self.treasure.encontrar_tesoro(self.hero)
