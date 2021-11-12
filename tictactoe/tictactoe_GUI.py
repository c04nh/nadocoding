import tkinter
from tkinter import messagebox

from tictactoe_game_engine import TictactoeGameEngine


class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        self.init_GUI()

    def init_GUI(self):
        self.CANVAS_SIZE = 300
        self.root = tkinter.Tk()
        self.root.title('틱택토')
        self.root.geometry(f'{self.CANVAS_SIZE}x{self.CANVAS_SIZE}')
        self.root.resizable(width=False, height=False)

        self.canvas = tkinter.Canvas(self.root, bg='white', width=self.CANVAS_SIZE, height=self.CANVAS_SIZE)
        self.canvas.pack()

        self.images = {}
        self.images['X'] = tkinter.PhotoImage(file='X.gif')
        self.images['O'] = tkinter.PhotoImage(file='O.gif')

        self.canvas.bind('<Button-1>', self.click_handler) # 괄호 안 씀


        self.root.mainloop()

    def click_handler(self, event):
        # input x, y -> row, col
        row, col = self.coordinate_to_position(event.x, event.y)
        # set row, col
        self.game_engine.set(row, col)
        # show board
        self.draw_board()
        # set winner
        winner = self.game_engine.set_winner()
        # 승자가 있거나 무승부일 때, 게임오버, 결과 출력
        if winner == 'X' or winner == 'O':
            messagebox.showinfo('Game Over', f'{winner} 승리')
            self.root.quit()
        elif winner == 'd':
            messagebox.showinfo('Game Over', '무승부')
            self.root.quit()
        # change turn
        self.game_engine.change_turn()

    def draw_board(self):
        TILE_SIZE = self.CANVAS_SIZE // self.game_engine.SIZE # 100
        # clear
        self.canvas.delete('all')

        x = 0
        y = 0
        for i, v in enumerate(self.game_engine.board):
            if v == '.':
                pass
            else:
                self.canvas.create_image(x, y, anchor='nw', image=self.images[v])
            x += TILE_SIZE
            if i % self.game_engine.SIZE == self.game_engine.SIZE - 1:
                x = 0
                y += TILE_SIZE

    def coordinate_to_position(self, x, y):
        return y // (self.CANVAS_SIZE // self.game_engine.SIZE) + 1, x // (self.CANVAS_SIZE // self.game_engine.SIZE) + 1


if __name__ == '__main__':
    ttt_GUI = TictactoeGUI()
