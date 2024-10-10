from Heroe import Heroe

from Mazmorra import Mazmorra

def main():
    name_hero = input("Introduce el nombre de tu heroe: ")
    hero = Heroe(name_hero)

    dungeon = Mazmorra(hero)
    dungeon.jugar()
if __name__ == '__main__':
      main()

