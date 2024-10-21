import tkinter as tk
import random


class Application:
    def __init__(self):
        #crear la ventana principal
        root = tk.Tk()
        root.title('Piedra, papel, tijera')
        root.geometry('350x300')

        #inicializamoc variables
        self.num_jugadores = 0
        self.win_j1= 0
        self.win_j2 = 0

        #crear menu
        menu = tk.Menu(root)
        root.config(menu=menu)

        menu.add_command(label='Salir', command=root.destroy)
        menu.add_separator()
        menu.add_command(label='1 Jugador', command=self.un_jugador)
        menu.add_separator()
        menu.add_command(label="2 Jugadores", command=self.dos_jugadores)

        #crear etiquetas
        self.label_mode = tk.Label(root, text='Bienvenido al juego del '
                                              'piedra, papel, tijeras.\n'
                                              'El ganador es el primero '
                                              'en llegar a 3 rondas '
                                              'ganadas.\n Hay dos modos '
                                              '"Un jugador" tu contra un '
                                              'bot y  \n"Dos jugadores" '
                                              'para que juegues con un amigo'
                                              ', una vez \nhayas elegido '
                                              'un modo no se podrá cambiar '
                                              'al otro.')
        self.label_mode.grid(column=1, row=0)

        self.label_result = tk.Label(root, text='', font=("arial",24, "bold"))
        self.label_result.grid(column=1, row=1)

        self.label_j1 = tk.Label(root, text='', font=("arial", 10, "bold"))
        self.label_j1.grid(column=0, row=2)

        self.label_j2 = tk.Label(root, text='', font=("arial", 10, "bold"))
        self.label_j2.grid(column=2, row=2)

        #crear las variables para elegir que sacar
        self.var_option_j1 = tk.StringVar()
        self.var_option_j1.set("Null")

        self.var_option_j2 = tk.StringVar()
        self.var_option_j2.set("Null")

        #crear los botones(no los posicionamos hasta elegir modo)
        self.stone_j1 = tk.Radiobutton(root, text='Piedra',
                                       variable=self.var_option_j1,
                                       value="piedra")
        self.paper_j1 = tk.Radiobutton(root, text='Papel',
                                       variable=self.var_option_j1,
                                       value="papel")
        self.scissors_j1 = tk.Radiobutton(root, text='Tijeras',
                                          variable=self.var_option_j1,
                                          value="tijeras")
        self.stone_j2 = tk.Radiobutton(root, text='Piedra',
                                       variable=self.var_option_j2,
                                       value="piedra")
        self.paper_j2 = tk.Radiobutton(root, text='Papel',
                                       variable=self.var_option_j2,
                                       value="papel")
        self.scissors_j2 = tk.Radiobutton(root, text='Tijeras',
                                          variable=self.var_option_j2,
                                          value="tijeras")

        #crear el botón (tampoco se posiciona aún)
        self.pelear = tk.Button(root, text='Iniciar pelea',
                                command=self.pelea)

        #crear más etiquetas
        self.label_message = tk.Label(root, text='')
        self.label_message.place(x=35, y=200)

        self.label_victory = tk.Label(root, text='',
                                      font=("arial",20, "bold"))
        self.label_victory.place(x=20, y=240)

        #ejecutar el bucle principal
        root.mainloop()

    #crear las funciones segun el numero de jugadores
    def un_jugador(self):
        if self.num_jugadores != 2:
            self.num_jugadores = 1
            self.interfaz()

    def dos_jugadores(self):
        if self.num_jugadores != 1:
            self.num_jugadores = 2
            self.interfaz()

    def interfaz(self):
        #mostrar toda la interfaz segun el modo
        if self.num_jugadores==1:
            self.label_mode.config(text="Modo de juego: Un jugador" )
        elif self.num_jugadores==2:
            self.label_mode.config(text="Modo de juego: Dos jugadores")

        self.label_result.config(text= str(self.win_j1) + "-" +
                                       str(self.win_j2))
        self.label_j1.config(text="Jugador 1")
        self.stone_j1.grid(column=0, row=3)
        self.paper_j1.grid(column=0, row=4)
        self.scissors_j1.grid(column=0, row=5)

        #si hay dos jugadores mostrar acciones para dos
        if self.num_jugadores == 2:
            self.label_j2.config(text="Jugador 2")
            self.stone_j2.grid(column=2, row=3)
            self.paper_j2.grid(column=2, row=4)
            self.scissors_j2.grid(column=2, row=5)

        self.pelear.grid(column=1, row=6)

    def pelea(self):
        #inicializar variables
        j1 = str(self.var_option_j1.get())
        j2 = None

        #si solo hay un jugador crear la respuesta del bot
        if self.num_jugadores == 1:
            j2 = ['piedra', 'papel', 'tijeras'][random.randint(0,2)]
        elif self.num_jugadores == 2:
            j2 = str(self.var_option_j2.get())

        #controlar el resultado anidando ifs y dar mensaje de acción
        #si algún jugador ya salimos
        if self.win_j1 < 3 and self.win_j2 < 3:
            if j1 == j2 and j1 != "Null" and j2 != "Null":
                self.label_message.config(text="Empate. Los dos jugadores"
                                               " lanzaron " + j1 + ".")
            elif (j1 == "piedra" and j2 == "tijeras") or (j1 == "tijeras"
                  and j2 == "papel") or (j1 == "papel" and j2 == "piedra"):
                self.label_message.config(text="Victoria del jugador 1. "
                                               "El jugador 1 lanzó " + j1 +
                                               "\n mientras que el jugador 2"
                                               " lanzó " + j2 + ".")
                self.victoria_j1()
            elif (j1 == "tijeras" and j2 == "piedra") or (j1 == "piedra"
                  and j2 == "papel") or (j1 == "papel" and j2 == "tijeras"):
                self.label_message.config(text="Victoria del jugador 2. "
                                               "El jugador 1 lanzó " + j1 +
                                               "\n mientras que el jugador 2"
                                               " lanzó " + j2 + ".")
                self.victoria_j2()

        #controlar si alguien gano con ifs
        if self.win_j1 >= 3:
            self.label_victory.config(text="Victoria del jugador 1")
        elif self.win_j2 >= 3 and self.num_jugadores == 2:
            self.label_victory.config(text="Victoria del jugador 2")
        elif self.win_j2 >= 3 and self.num_jugadores == 1:
            self.label_victory.config(text="    Victoria del Bot")

    #funciones para aumentar contadores
    def victoria_j1(self):
        self.win_j1 += 1
        self.interfaz()

    def victoria_j2(self):
        self.win_j2 += 1
        self.interfaz()
#ejecutador
if __name__ == "__main__":
    Application()