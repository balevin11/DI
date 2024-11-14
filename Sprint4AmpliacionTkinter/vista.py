from tkinter import simpledialog, Toplevel
import tkinter as tk

class GameView:
    def __init__(self, on_card_click_callback, update_move_count_callback, update_time_callback):
        #inicializar labels y variables necesarias
        self.cards =[]
        self.timer = tk.Label()
        self.moves = tk.Label()
        self.on_card_click_callback = on_card_click_callback
        self.update_move_count_callback = update_move_count_callback
        self.update_time_callback = update_time_callback
        self.images = None
        self.hidden_image = None
        self.game = None

    def create_board(self, model):
        self.game = Toplevel()
        self.game.title = "Game"
        self.game.geometry(model.cell_size * (int(model.board_large) + 2))

        #guardar las imágenes en vista
        self.images = model.images
        self.hidden_image = model.hidden_image

        # crear un array de labels para las cartas
        self.cards = []
        for i in range(int(model.board_large)):
            for j in range(int(model.board_large)):
                card = tk.Label(self.game, text="", image=self.hidden_image)
                card.grid(column=i, row=j, padx=10, pady=10)
                #agregamos el bind a cada carta
                card.bind("<Button-1>",self.on_card_click_callback)
                self.cards.append(card)

        #label temporizador y movimientos
        self.timer = tk.Label(self.game, text="")
        self.timer.grid(column=0, row=9, padx=10, pady=10)

        self.moves = tk.Label(self.game, text="")
        self.moves.grid(column=0, row=9, padx=10, pady=10)

    def update_board(self, pos, image_id):
        self.cards[pos].config(image=self.images[image_id])

    def reset_cards(self, pos1, pos2):
        self.cards[pos1].config(image=self.hidden_image)
        self.cards[pos2].config(image=self.hidden_image)

    def update_move_count(self, moves):
        self.moves.config(text="Movimientos: " + moves)
        self.update_move_count_callback()

    def update_time(self, time):
        self.timer.config(text="Tiempo: " + time)
        self.update_time_callback()

    def destroy(self):
        self.timer.config(text="")
        self.moves.config(text="")
        for card in self.cards:
            card.config(image=None)
        self.game.destroy()

class MainMenu:
    def __init__(self, root, start_game_callback, show_stats_callback, quit_callback):
        #crear ventana principal
        self.root = root
        self.root.title = "GameView"


        #crear botones
        play_button = tk.Button(root, text="Jugar", command=start_game_callback)
        play_button.pack()

        stats_button = tk.Button(root, text="Estadísticas", command=show_stats_callback)
        stats_button.pack()

        quit_button = tk.Button(root, text="Salir", command=quit_callback)
        quit_button.pack()

    def ask_player_name(self):
        return simpledialog.askstring("Nombre", "¿Cual es tu nombre?")


    def show_stats(self, stats):
        stats_root = Toplevel()
        stats_root.title = "Stats"
        stats_root.geometry("500x600")
        i = 0
        for row in stats:
            label = tk.Label(stats, text=row)
            label.grid(column=i, pady=10)
            i += 1

