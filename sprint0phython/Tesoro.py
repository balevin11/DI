import random


class Tesoro:
    #creamos un array con los nombres de los beneficios (en este caso usamos objetos)
    ITEMS = ["Poción", "Escudo", "Espada"]

    def encontrar_tesoro(self, hero):
        #creamos un numero a azar que será el objeto que se le otorgará al heroe
        item = random.randint(1,3)
        print("Héroe ha encontrado un tesoro: " + str(self.ITEMS[item]) + ".")
        #control del efecto del obejto encontrado segun el numero generado al azar
        if item == 1:
            #aumentamos el ataque del heroe
            hero.attack = hero.attack + 5
            print("El ataque de " + hero.nameHero + "aumenta a " + hero.attack + ".")
        elif item == 2:
            # aumentamos la defensa del heroe
            hero.defense = hero.defense + 5
            print("La defensa de " + hero.nameHero + " aumenta a " + hero.defense  + ".")
        else:
            #recuperamos la salud del heroe al maximo
            hero.health = hero.MAX_HEALTH
            print("La salud de {nombre del héroe} ha sido restaurada a" + hero.MAX_HEALTH+".")

