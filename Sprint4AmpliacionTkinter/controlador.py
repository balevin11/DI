from tkinter import Toplevel, Label, messagebox, simpledialog
from modelo import GameModel
from vista import MainMenu, GameView
import time

class GameController:
    def __init__(self, root):
        self.root = root
        self.model = None
        self.selected = []
        self.timer_started = False
        self.main_menu = MainMenu(root, self.start_game, self.show_stats, root.destroy)
        self.game_view = GameView(self.on_card_click, self.update_move_count, self.update_time)
        self.loading = None
        self.player_name = None
        self.moves = 0
        self.time = None

    def show_difficulty_selection(self):
        difficulty = None
        while difficulty != "fácil" and difficulty != "normal" and difficulty != "difícil":
            difficulty = simpledialog.askstring("Dificultad", "Elige modo de dificultad(fácil, normal, difícil)")

        self.player_name = self.main_menu.ask_player_name()
        self.start_game(difficulty)

    def start_game(self,difficulty):
        self.show_loading_window(self.player_name + " por favor espere")
        self.model = GameModel(difficulty,self.player_name)
        self.check_images_loaded()

    def show_loading_window(self, message):
        self.loading = Toplevel()
        self.loading.title("Cargando")
        self.loading.geometry("300x200")
        self.loading.grab_set()
        label = Label(self.loading, text=message)
        label.pack()

    def check_images_loaded(self):
        while self.model.images_are_loaded:
            time.sleep(1)
        self.loading.destroy()

    def on_card_click(self, pos):
        if not self.timer_started:
            self.model.start_timer()
            self.timer_started = True
        self.time = self.model.get_time

        if self.selected [0] is None:
            self.selected[0] = pos
        else:
            self.selected[1] = pos
            self.handle_card_selection()

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
            self.return_to_main_menu()

    def return_to_main_menu(self):
        self.game_view.destroy()

    def show_stats(self):
        self.main_menu.show_stats(self.model.load_scores())

    def update_time(self):
        self.game_view.update_time(self.time)








