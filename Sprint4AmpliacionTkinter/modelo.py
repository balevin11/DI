import os
import threading
import random
import time
import datetime
from xmlrpc.client import MAXINT

from recursos import download_image


class GameModel:

    def __init__(self, difficulty, player_name, cell_size=100):
        #crear el tablero según la dificultad
        if difficulty == "facil":
            self.board= [int(50) for _ in range(16)]
            self.board_size = 16
        elif difficulty == "normal":
            self.board = [int(50)  for _ in range(36)]
            self.board_size = 36
        elif difficulty == "dificil":
            self.board = [int(50)  for _ in range(64)]
            self.board_size = 64
        else:
            print("error")

        #llamar a las funciones privadas
        self._generate_board()
        self._load_images()

        #inicializar variables necesarias
        self.start_time = None
        self.moves = None
        if player_name != "":
            self.player_name = player_name
        else:
            print("error")
        self.cell_size = cell_size
        self.difficulty = difficulty
        self.images = {}
        self.images_loaded = False
        self.pairs_found = 0
        self.ranking = None

    def _generate_board(self):
        cont = 0
        self.unique_image_ids =[]
        #cubrir el tablero con parejas de id
        while cont < self.board_size/2:
            #obtener un id aleatorio
            image_id = random.randint(0,31)
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
            url_base=""

            #descargar la hidden image
            self.hidden_image = download_image(url_base + "hidden.jpg",
                                               self.cell_size)

            #descargar y guardar cada imagen
            for image_id in self.unique_image_ids:
                self.images[image_id] = download_image(url_base +
                                        str(image_id) + ".jpg" ,self.cell_size)

            #confirmar que se descargaron las imagenes
            self.images_loaded = True

        #abrir el hilo llamando a la función anterior
        threading.Thread(target=load_images_thread,daemon=True).start()

    #comprobar imagenes descargadas
    def images_are_loaded(self):
        return self.images_loaded

    #reinicio del temporizador
    def start_timer(self):
        self.start_time = time.time()

    #tiempo transcurrido desde el inicio del temporizador
    def get_time(self):
        return time.time() - self.start_time

    #comprobar la pareja selccionada
    def check_match(self, pos1, pos2):
        if self.board[pos1] == self.board[pos2]:
            self.pairs_found += 1

    #comprobar si terminó el juego
    def is_game_complete(self):
        if self.pairs_found == self.board_size/2:
            return True
        return False

    #guardar el resultado
    def save_score(self):
        #inicializamos las variables
        aux = MAXINT
        registered = False
        aux_ranking = None
        if self.ranking is None:
            self.ranking = [["Nombre", "Dificultad", "nº movimientos", "Fecha"],
                            ["-","facil","-","-"], ["-","facil","-","-"],
                            ["-","facil","-","-"], ["-","normal","-","-"],
                            ["-","normal","-","-"], ["-","normal","-","-"],
                            ["-","dificil","-","-"], ["-","dificil","-","-"],
                            ["-","dificil","-","-"]]

        #leer el ranking filtrar por dificultad y comparar
        #cantidad de movimientos
        for i in range(1,9):
            if (self.difficulty == self.ranking[i][1] and
                    self.ranking[i][2] > self.moves):
                #grabar el nuevo resultado solo la primera
                #vez y guardar ranking anterior
                if not registered:
                    if self.ranking[i][2] == "-":
                        aux = MAXINT
                    else:
                        aux = self.ranking[i][2]
                    aux_ranking = self.ranking[i]
                    self.ranking[i] = [self.player_name, self.difficulty,
                                       self.moves, datetime.datetime.now()]
                    registered = True
                #desplazar el ranking borrado por su inferior
                #(excepto si ya era el peor o igual)
                elif registered and self.ranking[i][2] > aux:
                    aux_ranking1 = aux_ranking
                    aux = self.ranking[i][2]
                    aux_ranking = self.ranking[i]
                    self.ranking[i] = aux_ranking1

        #grabar el ranking en ek archivo
        with open("ranking.txt","w") as file:
            for row in self.ranking:
                if row[1] != "-":
                    file.write(row)

    #cargar ranking
    def load_scores(self):
        self.ranking = [["Nombre", "Dificultad", "nº movimientos", "Fecha"],
                        ["-", "facil", "-", "-"], ["-", "facil", "-", "-"],
                        ["-", "facil", "-", "-"], ["-", "normal", "-", "-"],
                        ["-", "normal", "-", "-"], ["-", "normal", "-", "-"],
                        ["-", "dificil", "-", "-"], ["-", "dificil", "-", "-"],
                        ["-", "dificil", "-", "-"]]
        #comprobar que existe el archivo
        if os.path.exists("ranking.txt"):
            with open("ranking.txt", "r") as file:
                text = file.read()
                i = 0
                #leer cada línea y comprobar su dificultad para
                #grabarlos en orden
                for row in text:
                    out = False
                    while not out:
                        if i == 0:
                            self.ranking[i] = row
                            out = True
                        elif i > 0  < 4 and row.__contains__("facil"):
                            self.ranking[i] = row
                            out = True
                        elif i > 3 < 7 and row.__contains__("normal"):
                            self.ranking[i] = row
                            out = True
                        elif i > 6 < 10 and row.__contains__("dificil"):
                            self.ranking[i] = row
                            out = True
                        elif i > 9:
                            out = True
                            i = 0
                        i += 1
        return self.ranking
