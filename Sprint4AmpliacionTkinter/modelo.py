import threading
import random
import time
import datetime


from PIL import ImageTk

from recursos import download_image


class GameModel:

    def __init__(self, difficulty, player_name, cell_size=50):
        # crear el tablero según la dificultad
        if difficulty == "facil":
            self.board = [int(50) for _ in range(16)]
            self.board_size = 16
            self.board_large = 4
        elif difficulty == "normal":
            self.board = [int(50) for _ in range(36)]
            self.board_size = 36
            self.board_large = 6
        elif difficulty == "dificil":
            self.board = [int(50) for _ in range(64)]
            self.board_size = 64
            self.board_large = 8
        else:
            print("error")

        #inicializar variables necesarias
        self.start_time = None
        self.player_name = player_name
        self.cell_size = cell_size
        self.difficulty = difficulty
        self.images = {}
        self.images_loaded = False
        self.pairs_found = 0
        self.hidden_image = None

        #llamar a las funciones privadas
        self._generate_board()
        self._load_images()

    def _generate_board(self):
        cont = 0
        self.unique_image_ids =[]
        #cubrir el tablero con parejas de id
        while cont < self.board_size//2:
            #obtener un id aleatorio
            image_id = random.randint(1,32)
            #comprobar que el id no se repita
            if image_id not in self.unique_image_ids:
                self.unique_image_ids.append(image_id)
                contt = 0
                #grabar en dos espacios vacíos (los 50) el id
                while contt < 2:
                    x = random.randint(0, self.board_size -1)
                    if self.board[x] == 50:
                        self.board[x] = image_id
                        contt += 1
                cont += 1

    def _load_images(self):

        #abrir una subfunción para el hilo
        def load_images_thread():
            #inicializar variables necesarias
            url_base = "https://raw.githubusercontent.com/balevin11/DI/main/Sprint4AmpliacionTkinter/img/"

            #descargar la hidden image
            self.hidden_image = download_image((url_base + "hidden_image.jpg"), self.cell_size)

            #descargar y guardar cada imagen
            for image_id in self.unique_image_ids:
                self.images[image_id] = download_image((url_base +
                                        str(image_id) + ".jpg") ,self.cell_size)

            #confirmar que se descargaron las imagenes
            self.images_loaded = True

        #abrir el hilo llamando a la función anterior
        threading.Thread(target=load_images_thread,daemon=True).start()

    def adapt_images(self):
        for image_id in self.unique_image_ids:
            self.images[image_id] = ImageTk.PhotoImage(self.images[image_id])
        self.hidden_image = ImageTk.PhotoImage(self.hidden_image)

    #comprobar imagenes descargadas
    def images_are_loaded(self):
        return self.images_loaded

    #reinicio del temporizador
    def start_timer(self):
        self.start_time = time.time()

    #tiempo transcurrido desde el inicio del temporizador
    def get_time(self):
        return time.time() - self.start_time

    #comprobar la pareja seleccionada
    def check_match(self, pos1, pos2):
        if self.board[pos1] == self.board[pos2]:
            self.pairs_found += 1
            return False
        return True

    #comprobar si terminó el juego
    def is_game_complete(self):
        if self.pairs_found == self.board_size/2:
            return True
        return False

    #guardar el resultado(chatgpt)
    def save_score(self,moves):
        ranking = {
            'facil': [],
            'normal': [],
            'dificil': []
        }
        #abrir archivo controlando que exista, para recoger datos guardados anteriormente
        try:
            with open('ranking.txt', 'r') as f:
                #leer el archivo por lineas
                lineas = f.readlines()
                for linea in lineas:
                    #separar las lineas en sus elementos
                    partes = linea.strip().split(",")
                    if len(partes) == 4:#si hay 4 elementos
                        difficulty, name, move, date = partes #en orden iguala cada elemento
                        if difficulty in ranking:
                            #añadir al diccionario ranking
                            ranking[difficulty].append({'nombre': name, 'movimientos': int(move), 'fecha': date})
        except FileNotFoundError:
           pass #si no existe seguirá con ranking

        #crear el nuevo ranker
        new_ranker = {
            'nombre': self.player_name,
            'movimientos': moves,
            'fecha': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        #añadir el nuevo ranker a su dificultad
        if self.difficulty in ranking:
            ranking[self.difficulty].append(new_ranker)

        #ordenar por movimientos y filtrar los tres mejores
        for difficulty in ranking:
            ranking[difficulty] = sorted(ranking[difficulty], key=lambda x: x['movimientos'])[:3]

        #grabar diccionario ranking en archivo ranking
        with open('ranking.txt', 'w') as file:
            for difficulty in ranking:
                for ranker in ranking[difficulty]:
                    #f hace que sea texto literal, las variables van entre {}
                    file.write(f"{difficulty},{ranker['nombre']},{ranker['movimientos']},{ranker['fecha']}\n")

    #cargar ranking(chatgpt)
    @staticmethod
    def load_scores():
        ranking = {
            'facil': [],
            'normal': [],
            'dificil': []
        }

        #abrir archivo controlando que exista(mismo procedimiento que arriba)
        try:
            with open('ranking.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    part = line.strip().split(",")
                    if len(part) == 4:
                        difficulty, name, move, date = part
                        if difficulty in ranking:
                            ranking[difficulty].append({'nombre': name, 'movimientos': int(move), 'fecha': date})
        except FileNotFoundError:
            pass
        return ranking
