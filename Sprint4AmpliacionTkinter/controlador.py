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

    #preguntar por dificultad y nombre del jugador
    def show_difficulty_selection(self):
        #pregunta por dificultad
        self.difficulty = simpledialog.askstring("Dificultad",
                                                 "Elige modo de dificultad"
                                                 "(facil, normal, dificil)")
        #controlar respuesta dentro de los valores válidos
        while (self.difficulty != "facil" and self.difficulty != "normal"
               and self.difficulty != "dificil" and self.difficulty is not None):
            self.difficulty = simpledialog.askstring("Dificultad",
                                                     "Elige modo de dificultad"
                                                     "(facil, normal, dificil)")

        #si no se canceló en la dificultad preguntar nombre
        if self.difficulty is not None:
            self.player_name = self.main_menu.ask_player_name()

    #empezar el juego
    def start_game(self):
        #pregunta por dificultad y nombre
        self.show_difficulty_selection()
        #controlar que no se canceló
        if self.difficulty is not None and self.player_name is not None:
            #abrir ventana de espera
            self.show_loading_window(self.player_name + " por favor espere")
            #inicializar GameModel
            self.model = GameModel(self.difficulty,self.player_name)
            #revisar que las imagenes estén descargadas.
            #*hilo a parte para evitar bloqueos por el sleep
            threading.Timer(10.0, self.check_images_loaded).start()

    #abrir una ventana de con un mensaje
    def show_loading_window(self, message):
        #crear ventana
        self.loading = Toplevel()
        self.loading.title("Cargando")
        self.loading.geometry("200x100")
        self.loading.grab_set()

        #crear label con el mensaje
        label = Label(self.loading, text=message)
        label.pack()

    #revisar que las imagenes estén descargadas
    def check_images_loaded(self):
        #si no hay confirmacion esperar
        while not self.model.images_are_loaded():
            time.sleep(1)
        #destruir ventana espera
        self.loading.destroy()
        #adaptar las imagenes a tkinter y crear el tablero
        self.model.adapt_images()
        self.game_view.create_board(self.model)

    #interacciones al clicar una imagen
    def on_card_click(self,i):
        #si no se inició temporizador iniciarlo
        if not self.timer_started:
            self.timer_started = True
            self.model.start_timer()
            self.game_view.timer_continue = True
            self.update_time()

        #si no se seleccionó una carta antes guardar la
        #posición y mostrarla
        if self.selected [0] is None:
            self.selected[0] = i
            self.game_view.update_board(self.selected[0],
                                        self.model.board[self.selected[0]])
        #si se seleccionó dos veces la misma carta pasar
        elif i == self.selected[0]:
            pass
        #a la segunda selección diferente guardar posicion,
        #mostrar la carta y comprobar si es la misma. Uso de
        #hilo por posibles errores
        else:
            self.selected[1] = i
            self.game_view.update_board(self.selected[1],
                                        self.model.board[self.selected[1]])
            threading.Thread(target=self.handle_card_selection,
                             daemon=True).start()

    #acciones de movimientos
    def handle_card_selection(self):
        #desactivar el clic en las cartas
        self.game_view.disable_events()
        #si las cartas son distintas volver a esconderlas
        if self.model.check_match(self.selected[0], self.selected[1]):
            time.sleep(1)
            self.game_view.reset_cards(self.selected[0], self.selected[1])

        #actualizar movimientos
        self.moves += 1
        self.update_move_count()

        #revisar si se terminó el juego
        self.check_game_complete()

        #vaciar registro de cartas seleccionadas
        self.selected = [None,None]

    #actualizar contador de movimientos
    def update_move_count(self):
        self.game_view.update_move_count(self.moves)

    #acciones si termina el juego
    def check_game_complete(self):
        #si terminó el juego
        if self.model.is_game_complete():
            #parar temporizador
            self.game_view.stop_timer()
            #dar mensage de victoria
            messagebox.showinfo("Victoria", "Enhorabuena has ganado")
            self.timer_started = False
            #guardar resultado
            self.model.save_score(self.moves)
            #resetear movimientos
            self.moves = 0
            #volver al menú principal
            self.return_to_main_menu()
        else:
            #si no terminó la partida volver a activar las cartas
            self.game_view.enable_events()

    #cerrar la ventana de juego
    def return_to_main_menu(self):
        self.game_view.destroy()

    #mostrar ranking
    def show_stats(self):
        self.main_menu.show_stats(self.model.load_scores())

    #actualizar el temporizador
    def update_time(self):
        self.game_view.update_time(self.model.get_time())
