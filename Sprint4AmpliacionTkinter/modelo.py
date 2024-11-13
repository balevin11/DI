import threading
import random
import time
import datetime
from recursos import download_image
class GameModel:
    board = None
    def __init__(self, difficulty, player_name, cell_size=100):
        if difficulty == "facil":
            self.board[4][4]= None
            self.board_size = 4
        elif difficulty == "normal":
            self.board[6][6] = None
            self.board_size = 6
        elif difficulty == "dificil":
            self.board[8][8]= None
            self.board_size = 8
        else:
            print("error")
        self._generate_board()
        self._load_images()
        self.start_time = None
        self.moves = None
        self.player_name = player_name
        self.cell_size = cell_size
        self.difficulty = difficulty


    def _generate_board(self):
        cont = 0
        while cont < (self.board_size * self.board_size)/2:
            ids = random.randint(0,31)
            contt = 0
            while contt < 2:
                x = random.randint(0, self.board_size)
                y = random.randint(0, self.board_size)
                if self.board[x][y] is None:
                    self.board[x][y] = ids
                else:
                    contt -= 1
                contt += 1
            cont += 1

    def _load_images(self):
        url=""
        hilo = threading.Thread(target=download_image,
                                args=(url,self.cell_size))
        hilo.start()

    def images_are_loaded(self):
        return True

    def start_timer(self):
        self.start_time = 0

    def get_time(self):
        pass
    def check_match(self, pos1, pos2):
        pass
    def is_game_complete(self):
        pass
    def save_score(self):
        pass
    def load_scores(self):
        pass