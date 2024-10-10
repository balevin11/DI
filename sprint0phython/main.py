from Heroe import Heroe

from Mazmorra import Mazmorra

def main():

    #creamos nuestro heroe con el nombre que queremos
    name_hero = input("Introduce el nombre de tu heroe: ")
    hero = Heroe(name_hero)
    
    #iniciamos el juego con nuestro heroe
    dungeon = Mazmorra(hero)
    dungeon.jugar()

if __name__ == '__main__':
      main()
