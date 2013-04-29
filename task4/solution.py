class TicTacToeBoard:

    def __init__(self):
        self._board = {'A1': ' ', 'A2': ' ', 'A3': ' ',
                       'B1': ' ', 'B2': ' ', 'B3': ' ',
                       'C1': ' ', 'C2': ' ', 'C3': ' '}
        self.filled_cells = 0

    def __str__(self):
        line = '  ' + '-' * 13
        return '\n' + line + '\n' + ('\n' + line + '\n').join([str(row) + ' | ' +
                                                               ' | '.join(
                                                               [self._board[column + str(row)]
                                                                for column in 'ABC']) + ' |'
                                                               for row in [3, 2, 1]]) + '\n' + line +\
            '\n    A   B   C'

    def __setitem__(self, key, val):
        if self._board[key] == 'X' or self._board[key] == 'O':
            raise InvalidMove("Move not possible!")
        if key not in self._board.keys():
            raise InvalidKey("Invalid coords!")
        if val not in ['X', 'O']:
            raise InvalidValue("Use only X and O!")
        if last_move == val:
            raise InvalidValue("Not your turn!")
        if val in ['X', 'O']:
            last_move = val
        self._board[key] = val
        self.filled_cells += 1

    def game_status(self):
        if self.wins('X'):
            return 'X wins!'
        elif self.wins('O'):
            return 'O wins!'
        elif self.filled_cells == 9:
            return 'Draw!'
        else:
            return 'Game in progress.'

    def wins(self, gamer):
            winning_combinations = (('A1', 'A2', 'A3'), ('B1', 'B2', 'B3'),
                                   ('C1', 'C2', 'C3'), ('A1', 'B1', 'C1'),
                                   ('A2', 'B2', 'C2'), ('A3', 'B3', 'C3'),
                                   ('A1', 'B2', 'C3'), ('A3', 'B2', 'C1'))
            for comb in iter(winning_combinations):
                if self.board[comb[0]] == self.board[comb[1]] == \
                   self.board[comb[2]] == gamer:
                    return True
            return False

    class InvalidMove (Exception):
        pass

    class InvalidKey  (Exception):
        pass

    class InvalidValue (Exception):
        pass

    class NotYourTurn  (Exception):
        pass
