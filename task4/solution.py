class TicTacToeBoard:

    def __init__(self):
        self._board = {'A1': ' ', 'A2': ' ', 'A3': ' ',
                       'B1': ' ', 'B2': ' ', 'B3': ' ',
                       'C1': ' ', 'C2': ' ', 'C3': ' '}

    def __str__(self):
        line = '  -------------'
        return '\n' + line + '\n' +\
        + ('\n' + line + '\n').join([str(row) + ' | ' +
                    ' | '.join(
                        [self._board[column + str(row)]
                            for column in 'ABC']) + ' |'
                        for row in [3,2,1]]) + '\n' + line +\
                        '\n    A   B   C'

    def __setitem__(self, key, val):
        self._board[key] = val

    def first_exceptions(key, val):
        try:
            '''WAAAAAAAAAAAAA'''
        return

    def game_status():
            return 'Game in progress.'
            
