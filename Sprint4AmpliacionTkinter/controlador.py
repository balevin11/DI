from tkinter import Toplevel, Label, messagebox, simpledialog, Tk
from modelo import GameModel
from vista import MainMenu, GameView
import time

class GameController:
    def __init__(self, root):
        self.root = root
        self.model = GameModel
        self.selected = []
        self.timer_started = False
        self.main_menu = MainMenu(self.root, self.start_game, show_stats_callback, quit_callback)
        self.loading = None
        self.player_name = None

    def show_difficulty_selection(self):
        difficulty = None
        while difficulty != "fácil" and difficulty != "normal" and difficulty != "difícil":
            difficulty = simpledialog.askstring("Dificultad", "Elige modo de dificultad(fácil, normal, difícil)")

        self.player_name = self.main_menu.ask_player_name()
        self.start_game(difficulty)

    def start_game(self,difficulty):
        self.show_loading_window(self.player_name + " por favor espere")
        self.model(difficulty,self.player_name)
        self.check_images_loaded()

    def show_loading_window(self, message):
        self.loading = Toplevel()
        self.loading.title = "Cargando"
        self.loading.geometry = "300x200"
        self.loading.grab_set()
        label = Label(self.loading, text=message)
        label.pack()

    def check_images_loaded(self):
        while self.model.images_are_loaded:
            time.sleep(1)
        self.loading.destroy()

    def on_card_click(self, pos):

