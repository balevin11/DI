import tkinter as tk

class Application:
    def __init__(self):
        #crear la ventana principal
        root = tk.Tk()
        root.title('Piedra, papel, tijera')
        root.geometry('700x500')

        self.win_j1= 0
        self.win_j2 = 0

        menu = tk.Menu(root)
        root.config(menu=menu)

        menu.add_command(label='Salir', command=root.destroy)
        menu.add_separator()
        menu.add_command(label='1 Jugador', command=self.un_jugador)
        menu.add_separator()
        menu.add_command(label="2 Jugadores", command=self.dos_jugadores)

        self.label_mode = tk.Label(root, text='')
        self.label_mode.grid(column=1, row=0)

        self.label_result = tk.Label(root, text='', font=("arial",24, "bold"))
        self.label_result.grid(column=1, row=1)

        #crear las variables para elegir que sacar
        self.var_option_j1 = tk.StringVar()
        self.var_option_j1.set("Null")

        self.var_option_j2 = tk.StringVar()
        self.var_option_j2.set("Null")

        #crear los botones
        self.stone_j1 = tk.Radiobutton(root, text='Piedra', variable=self.var_option_j1, value="piedra")
        self.paper_j1 = tk.Radiobutton(root, text='Papel', variable=self.var_option_j1, value="papel")
        self.scissors_j1 = tk.Radiobutton(root, text='Tijeras', variable=self.var_option_j1, value="tijeras")
        self.stone_j2 = tk.Radiobutton(root, text='Piedra', variable=self.var_option_j2, value="piedra")
        self.paper_j2 = tk.Radiobutton(root, text='Papel', variable=self.var_option_j2, value="papel")
        self.scissors_j2 = tk.Radiobutton(root, text='Tijeras', variable=self.var_option_j2, value="tijeras")

        self.pelear = tk.Button(root, text='Iniciar pelea', command=self.pelea)


        self.label_message = tk.Label(root, text='')
        self.label_message.grid(column=1, row=6)

        self.label_victory = tk.Label(root, text='', font=("arial",46, "bold"))
        self.label_victory.grid(column=1, row=7)

        #ejecutar el bucle principal
        root.mainloop()

    def dos_jugadores(self):
        #mostrar toda la interfaz
        self.label_mode.config(text="Modo de juego: Dos jugadores")
        self.label_result.config(text= str(self.win_j1) + "-" + str(self.win_j2))
        self.stone_j1.grid(column=0, row=2,)
        self.paper_j1.grid(column=0, row=3)
        self.scissors_j1.grid(column=0, row=4)
        self.stone_j2.grid(column=2, row=2)
        self.paper_j2.grid(column=2, row=3)
        self.scissors_j2.grid(column=2, row=4)
        self.pelear.grid(column=1, row=5)

    def un_jugador(self):
        self.label_mode.config(text="Modo de juego: Un jugador")

    def pelea(self):
        j1 = str(self.var_option_j1.get())
        j2 = str(self.var_option_j2.get())

        if self.win_j1 < 3 and self.win_j2 < 3:
            if j1 == j2 and j1 != "Null" and j2 != "Null":
                self.label_message.config(text="Empate. Los dos jugadores lanzaron " + j1 + ".")
            elif (j1 == "piedra" and j2 == "tijeras") or (j1 == "tijeras" and j2 == "papel") or (j1 == "papel" and j2 == "piedra"):
                self.label_message.config(text="Victoria del jugador 1. El jugador 1 lanzó " + j1 + " mientras que el jugador 2 lanzó " + j2 + ".")
                self.victoria_j1()
            elif (j1 == "tijeras" and j2 == "piedra") or (j1 == "piedra" and j2 == "papel") or (j1 == "papel" and j2 == "tijeras"):
                self.label_message.config(text="Victoria del jugador 2. El jugador 1 lanzó " + j1 + " mientras que el jugador 2 lanzó " + j2 + ".")
                self.victoria_j2()
        if self.win_j1 >= 3:
            self.label_victory.config(text="Victoria del jugador 1")
        elif self.win_j2 >= 3:
            self.label_victory.config(text="Victoria del jugador 2")


    def victoria_j1(self):
        self.win_j1 += 1
        self.dos_jugadores()

    def victoria_j2(self):
        self.win_j2 += 1
        self.dos_jugadores()

if __name__ == "__main__":
    Application()