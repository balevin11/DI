
from tkinter import simpledialog, Toplevel
import tkinter as tk

class GameView:
    def __init__(self, on_card_click_callback, update_time_callback):
        #inicializar labels y variables necesarias
        self.cards =[]
        self.label_timer = tk.Label()
        self.label_moves = tk.Label()
        self.board_frame = tk.Frame()
        self.text_frame = tk.Frame()
        self.on_card_click_callback = on_card_click_callback
        self.update_time_callback = update_time_callback
        self.images = None
        self.hidden_image = None
        self.game = None
        self.timer_continue = True

    #crear el tablero
    def create_board(self, model):
        # #tamaño según la dificultad
        size = (model.cell_size + 30) * int(model.board_large)
        #crear ventana de juego
        self.game = Toplevel()
        self.game.title("Game")
        self.game.geometry(str(size) + "x" + str(size + 50))
        self.game.grab_set()

        # Crear un Frame para el tablero y otro para el texto
        self.board_frame = tk.Frame(self.game)
        self.board_frame.grid(row=0, column=0, padx=10, pady=10)

        self.text_frame = tk.Frame(self.game)
        self.text_frame.grid(row=1, column=0, padx=10, pady=10)

        #guardar las imágenes en vista
        self.images = model.images
        self.hidden_image = model.hidden_image

        #crear un array de labels para las cartas
        self.cards = []
        for i in range(int(model.board_large)):
            for j in range(int(model.board_large)):
                #crear un label por carta y posicionarlo
                card = tk.Label(self.board_frame, text="",
                                image=self.hidden_image)
                card.grid(column=i, row=j, padx=10, pady=10)
                self.cards.append(card)

        #volver a las cartas clicables
        self.enable_events()

        #label temporizador y movimientos
        self.label_timer = tk.Label(self.text_frame, text="")
        self.label_timer.grid(column=0, row=1, pady=10)

        self.label_moves = tk.Label(self.text_frame, text="")
        self.label_moves.grid(column=1, row=1, pady=10)

    #desactivar el bind de las cartas
    def disable_events(self):
        for card in self.cards:
            card.unbind("<Button-1>")

    #activar o crear el bind de las cartas
    def enable_events(self):
        for pos_card, card in enumerate(self.cards):
            #lambda es para poder enviar un valor en el callback,
            #"_" es para evitar enviar el evento, idx es la id de
            #la posición de la carta. Se asocia a cada carta
            #individualmente para que cuando se clique de un callback
            #con el id de posición
            card.bind("<Button-1>", lambda _, idx=pos_card:
                      self.on_card_click_callback( idx))

    #cambia variable controladora del temporizador
    def stop_timer(self):
        self.timer_continue = False

    #mostrar la imagen de la carta correspondiente
    def update_board(self, pos, image_id):
        self.cards[pos].config(image=self.images[image_id])

    #ocultar dos imagenes
    def reset_cards(self, pos1, pos2):
        self.cards[pos1].config(image=self.hidden_image)
        self.cards[pos2].config(image=self.hidden_image)

    #muestra contador de movimientos
    def update_move_count(self, moves):
        self.label_moves.config(text="Movimientos: " + str(moves))

    #muestra temporizador
    def update_time(self, time):
        #timer_continue controla su funcionamiento
        if self.timer_continue:
            #convertir el time a segundos y minutos
            m = int(time) //60
            s = int(time) % 60
            self.label_timer.config(text="Tiempo: " + str(m) + ":" + str(s))
            #convoca al callback cada 0.1 segundos
            self.game.after(100, self.update_time_callback)

    #destruir la ventana de juego
    def destroy(self):
        #vaciar todos los label
        self.label_timer.config(text="")
        self.label_moves.config(text="")
        for card in self.cards:
            card.config(image=None)

        #cerrar la ventana de juego
        self.game.destroy()


class MainMenu:
    def __init__(self, root, start_game_callback, show_stats_callback,
                 quit_callback):
        #titular ventana principal
        root.title("GameView")

        #crear botones con sus respectivos callback
        play_button = tk.Button(root, text="Jugar",
                                command=start_game_callback)
        play_button.pack()

        stats_button = tk.Button(root, text="Estadísticas",
                                 command=show_stats_callback)
        stats_button.pack()

        quit_button = tk.Button(root, text="Salir",
                                command=quit_callback)
        quit_button.pack()

    #solicitud de nombre del jugador
    @staticmethod
    def ask_player_name():
        name = ""
        while name == "":
            #simpledialog crea una ventana en la que aparece la
            #pregunta y se puede escribir y contiene dos botones
            #ok" y "cancel". *Importante cancelar devuelve None,
            #ok vacío devuelve ""
            name = simpledialog.askstring("Nombre", "¿Cual es tu nombre?")
            if name != "":
                return name

    #Mostrar el ranking
    @staticmethod
    def show_stats(stats):
        #crear la ventana del ranking
        stats_root = Toplevel()
        stats_root.title("Stats")
        stats_root.geometry("500x600")
        stats_root.grab_set()

        #juntar stats por dificultad y almacenar en un texto
        text = ""
        #filtrado por dificultad
        for difficulty in ['facil', 'normal', 'dificil']:
            if difficulty in stats:
                text += f"\nDificultad: {difficulty.capitalize()}\n"
                #grabado de rankers
                for ranker in stats[difficulty]:
                    text += (f"Jugador: {ranker['nombre']}, "
                             f"Movimientos: {ranker['movimientos']}, "
                             f"Fecha: {ranker['fecha']}\n")

        #crear un label del ranking completo
        label_ranking = tk.Label(stats_root, text=text)
        label_ranking.pack(pady=10)
