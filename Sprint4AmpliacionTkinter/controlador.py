import threading
from tkinter import Toplevel, Label, messagebox, simpledialog
from modelo import GameModel
from vista import MainMenu, GameView
import time

class GameController:
    def __init__(self, root):
        self.root = root
        self.model = None
        self.selected = [None,None]
        self.timer_started = False
        self.loading = None
        self.difficulty ="normal"
        self.player_name = "jugador"
        self.moves = 0
        self.time = None
        self.main_menu = MainMenu(root, self.start_game, self.show_stats, root.destroy)
        self.game_view = GameView(self.on_card_click, self.update_time)

    def show_difficulty_selection(self):
        self.difficulty = simpledialog.askstring("Dificultad", "Elige modo de dificultad(fácil, normal, difícil)")
        while self.difficulty != "fácil" and self.difficulty != "normal" and self.difficulty != "difícil":
            self.difficulty = simpledialog.askstring("Dificultad", "Elige modo de dificultad(fácil, normal, difícil)")
        self.player_name = self.main_menu.ask_player_name()

    def start_game(self):
        self.show_difficulty_selection()
        self.show_loading_window(self.player_name + " por favor espere")
        self.model = GameModel(self.difficulty,self.player_name)
        threading.Timer(10.0, self.check_images_loaded).start()

    def show_loading_window(self, message):
        self.loading = Toplevel()
        self.loading.title("Cargando")
        self.loading.geometry("200x100")
        self.loading.grab_set()
        label = Label(self.loading, text=message)
        label.pack()

    def check_images_loaded(self):
        while not self.model.images_are_loaded():
            time.sleep(1)
        self.loading.destroy()
        self.model.adapt_images()
        self.game_view.create_board(self.model)

    def on_card_click(self, pos):
        if not self.timer_started:
            self.timer_started = True
            self.model.start_timer()
            self.update_time()

        # Calcular columna (col) y fila (row) donde ocurrió el clic
        col = pos.x // self.model.cell_size + 10  # tamaño de la carta más margen
        row = pos.y // self.model.cell_size + 10

        if self.selected [0] is None:
            self.selected[0] = (col * self.model.board_large) + row #esto calcula la posicion de la carta pasando el tablero de un 2d a 1d
        else:
            self.selected[1] = (col * self.model.board_large) + row
            self.handle_card_selection()
            self.selected = [None,None]

    def handle_card_selection(self):
        if self.model.check_match(self.selected[0], self.selected[1]):
            time.sleep(1)
            self.game_view.reset_cards(self.selected[0], self.selected[1])
        self.moves += 1
        self.update_move_count()
        self.check_game_complete()

    def update_move_count(self):
        self.game_view.update_move_count(self.moves)

    def check_game_complete(self):
        if self.model.is_game_complete():
            messagebox.showinfo("Victoria", "Enorabuena has ganado")
            self.timer_started = False
            self.return_to_main_menu()

    def return_to_main_menu(self):
        self.game_view.destroy()

    def show_stats(self):
        self.main_menu.show_stats(self.model.load_scores())

    def update_time(self):
        self.game_view.update_time(self.model.get_time())
