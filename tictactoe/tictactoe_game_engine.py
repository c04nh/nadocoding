class TictactoeGameEngine:
    def __init__(self):
        self.SIZE = 3
        self.board = list('.'  * self.SIZE * self.SIZE)
        self.turn = 'X'

    def show_board(self):
        for a in range(len(self.board)):
            print(self.board[a], end=' ')
            if a % self.SIZE == self.SIZE - 1:
                print()

    def set(self, row, col):
        self.board[self.SIZE * (row - 1) + (col - 1)] = self.turn

    def set_winner(self):
        # - 3줄
        # | 3줄
        # \
        # /
        return self.turn
        # 비기는 조건 : 다 채워졌는데 위에 해당 안 됐을 때 (self.board에 .이 없을 때)
        return 'd'

    def change_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'
        # self.turn = 'O' if self.turn == 'X' else 'X'


if __name__ == '__main__':
    game_engine = TictactoeGameEngine()
    game_engine.show_board()
    game_engine.set(3, 2)
    game_engine.show_board() # ['.', '.', '.', '.', '.', '.', '.', 'X', '.']
    game_engine.set(3, 1)
    game_engine.set(3, 3)
    # print(game_engine.set_winner()) # 'X'
    #
    game_engine.change_turn()
    print(game_engine.turn) # 'O'