# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

def main():
    nombre_heroe = input("Introduce el nombre de tu heroe: ")
    heroe = Heroe(nombre_heroe)

    mazmorra = Mazmorra(heroe)
    mazmorra.jugar()
if __name__ == '__main__':
      main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
