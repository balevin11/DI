from tkinter import simpledialog, Toplevel
import tkinter as tk

class GameView:
    def __init__(self, on_card_click_callback, update_move_count_callback, update_time_callback):
        self.root = tk.Tk()
        self.root.title = "GameView"
        self.root.geometry('500x600')


        #crear un array de labels para las cartas
        self.cards =[]
        for i in range(8):
            for j in range(8):
                card = tk.Label(self.root, text="")
                card.grid(column=i, row=j, padx=10, pady=10)
                self.cards.append(card)

        self.timer = tk.Label(self.root, text="")
        self.timer.grid(column=0,row=9,padx=10, pady=10)

        self.moves = tk.Label(self.root, text="")
        self.moves.grid(column=0, row=9, padx=10, pady=10)

        self.on_card_click_callback = on_card_click_callback
        self.update_move_count_callback = update_move_count_callback
        self.update_time_callback = update_time_callback

    def create_board(self, model):
        game = Toplevel(self.root)
        game.title = "Game"
        game.geometry(model.cell_size * (int(model.board_large) + 2))

        # crear un array de labels para las cartas
        self.cards = []
        for i in range(int(model.board_large)):
            for j in range(int(model.board_large)):
                card = tk.Label(game, text="", image=model.hidden_image)
                card.grid(column=i, row=j, padx=10, pady=10)
                self.cards.append(card)

        #label temporizador y movimientos
        self.timer = tk.Label(game, text="")
        self.timer.grid(column=0, row=9, padx=10, pady=10)

        self.moves = tk.Label(game, text="")
        self.moves.grid(column=0, row=9, padx=10, pady=10)
