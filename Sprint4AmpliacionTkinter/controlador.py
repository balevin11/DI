import threading
from tkinter import Toplevel, Label, messagebox, simpledialog
from modelo import GameModel
from vista import MainMenu, GameView
import time

class GameController:
    def __init__(self, root):
        #inicializar variables
        self.selected = [None,None]
        self.timer_started = False
        self.loading = None
        self.difficulty ="normal"
        self.player_name = "jugador"
        self.moves = 0
        self.time = None

        #inicializar clases
        self.model = GameModel(self.difficulty,self.player_name)
        self.main_menu = MainMenu(root, self.start_game, self.show_stats, root.destroy)
        self.game_view = GameView(self.on_card_click, self.update_time)

    def show_difficulty_selection(self):
        self.difficulty = simpledialog.askstring("Dificultad", "Elige modo de dificultad(facil, normal, dificil)")
        while self.difficulty != "facil" and self.difficulty != "normal" and self.difficulty != "dificil" and self.difficulty is not None:
            self.difficulty = simpledialog.askstring("Dificultad", "Elige modo de dificultad(facil, normal, dificil)")
        if self.difficulty is not None:
            self.player_name = self.main_menu.ask_player_name()

    def start_game(self):
        self.show_difficulty_selection()
        if self.difficulty is not None and self.player_name is not None:
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

    def on_card_click(self,i):
        if not self.timer_started:
            self.timer_started = True
            self.model.start_timer()
            self.game_view.timer_continue = True
            self.update_time()
        if self.selected [0] is None:
            self.selected[0] = i
            self.game_view.update_board(self.selected[0], self.model.board[self.selected[0]])
        elif i == self.selected[0]:
            pass
        else:
            self.selected[1] = i
            self.game_view.update_board(self.selected[1],self.model.board[self.selected[1]])
            threading.Thread(target=self.handle_card_selection,daemon=True).start()


    def handle_card_selection(self):
        self.game_view.disable_events()
        if self.model.check_match(self.selected[0], self.selected[1]):
            time.sleep(1)
            self.game_view.reset_cards(self.selected[0], self.selected[1])
        self.moves += 1
        self.update_move_count()
        self.check_game_complete()
        self.selected = [None,None]


    def update_move_count(self):
        self.game_view.update_move_count(self.moves)

    def check_game_complete(self):
        if self.model.is_game_complete():
            self.game_view.stop_timer()
            messagebox.showinfo("Victoria", "Enhorabuena has ganado")
            self.timer_started = False
            self.model.save_score(self.moves)
            self.moves = 0
            self.return_to_main_menu()
        else:
            self.game_view.enable_events()

    def return_to_main_menu(self):
        self.game_view.destroy()

    def show_stats(self):
        self.main_menu.show_stats(self.model.load_scores())

    def update_time(self):
        self.game_view.update_time(self.model.get_time())

