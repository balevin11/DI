from tkinter import simpledialog, Toplevel
import tkinter as tk

class GameView:
    def __init__(self, on_card_click_callback, update_time_callback):
        #inicializar labels y variables necesarias
        self.cards =[]
        self.timer = tk.Label()
        self.moves = tk.Label()
        self.board_frame = tk.Frame()
        self.text_frame = tk.Frame()
        self.on_card_click_callback = on_card_click_callback
        self.update_time_callback = update_time_callback
        self.images = None
        self.hidden_image = None
        self.game = None

    def create_board(self, model):
        size = (model.cell_size + 30) * int(model.board_large)
        self.game = Toplevel()
        self.game.title("Game")
        self.game.geometry(str(size) + "x" + str(size + 50))

        # Crear un Frame para el tablero y otro para el texto
        self.board_frame = tk.Frame(self.game)
        self.board_frame.grid(row=0, column=0, padx=10, pady=10)

        self.text_frame = tk.Frame(self.game)
        self.text_frame.grid(row=1, column=0, padx=10, pady=10)

        #guardar las imágenes en vista
        self.images = model.images
        self.hidden_image = model.hidden_image

        # crear un array de labels para las cartas
        self.cards = []
        for i in range(int(model.board_large)):
            for j in range(int(model.board_large)):
                card = tk.Label(self.board_frame, text="", image=self.hidden_image)
                card.grid(column=i, row=j, padx=10, pady=10)
                #agregamos el bind a cada carta
                self.cards.append(card)
        self.enable_events()
        #label temporizador y movimientos
        self.timer = tk.Label(self.text_frame, text="")
        self.timer.grid(column=0, row=1, pady=10)

        self.moves = tk.Label(self.text_frame, text="")
        self.moves.grid(column=1, row=1, pady=10)

    def disable_events(self):
        for card in self.cards:
            card.unbind("<Button-1>")

    def enable_events(self):
        for pos_card, card in enumerate(self.cards):
            card.bind("<Button-1>", lambda _, idx=pos_card: self.on_card_click_callback( idx))

    def update_board(self, pos, image_id):
        self.cards[pos].config(image=self.images[image_id])

    def reset_cards(self, pos1, pos2):
        self.cards[pos1].config(image=self.hidden_image)
        self.cards[pos2].config(image=self.hidden_image)

    def update_move_count(self, moves):
        self.moves.config(text="Movimientos: " + str(moves))

    def update_time(self, time):
        m = int(time) //60
        s = int(time) % 60
        self.timer.config(text="Tiempo: " + str(m) + ":" + str(s))
        self.game.after(100, self.update_time_callback)

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
        self.root.title("GameView")

        #crear botones
        play_button = tk.Button(root, text="Jugar", command=start_game_callback)
        play_button.pack()

        stats_button = tk.Button(root, text="Estadísticas", command=show_stats_callback)
        stats_button.pack()

        quit_button = tk.Button(root, text="Salir", command=quit_callback)
        quit_button.pack()

    def ask_player_name(self):
        name = ""
        while name == "":
            name = simpledialog.askstring("Nombre", "¿Cual es tu nombre?")
            if name != "":
                return name

    def show_stats(self, stats):
        stats_root = Toplevel()
        stats_root.title("Stats")
        stats_root.geometry("500x600")
        i = 0
        for row in stats:
            label = tk.Label(stats, text=row)
            label.grid(column=i, pady=10)
            i += 1
