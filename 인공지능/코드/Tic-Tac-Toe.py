# 보드는1차원리스트로구현한다.
game_board = [' ', ' ', ' ',
 ' ', ' ', ' ',
 ' ', ' ', ' ']
 # 비어있는칸을찾아서인덱스를리스트로반환한다.
def empty_cells(board):
     cells = []
     for x, cell in enumerate(board):
         if cell == ' ':
             cells.append(x)
     return cells

 # 비어있는칸에는놓을수있다.
def valid_move(x):
     return x in empty_cells(game_board)

# 위치x에놓는다.
def move(x, player):
    if valid_move(x):
        game_board[x] = player
        return True
    return False

 # 현재게임보드를그린다.
def draw(board):
     for i, cell in enumerate(board):
         if i%3 == 0:
            print('\n----------------')
         print('|', cell , '|', end='')
     print('\n----------------')
 # 보드의상태를평가한다.
def evaluate(board):
     if check_win(board, 'X'):
         score = 1
     elif check_win(board, 'O'):
         score = -1
     else:
         score = 0
     return score

# 1차원리스트에서동일한문자가수직선이나수평선, 대각선으로나타나면
# 승리한것으로한다.
def check_win(board, player):
     win_conf = [
     [board[0], board[1], board[2]],
     [board[3], board[4], board[5]],
     [board[6], board[7], board[8]],
     [board[0], board[3], board[6]],
     [board[1], board[4], board[7]],
     [board[2], board[5], board[8]],
     [board[0], board[4], board[8]],
     [board[2], board[4], board[6]],
     ]
     return [player, player, player] in win_conf

# 1차원리스트에서동일한문자가수직선이나수평선, 대각선으로나타나면
# 승리한것으로한다.
def game_over(board):
     return check_win(board, 'X') or check_win(board, 'O')

# 미니맥스알고리즘을구현한다.
# 이함수는순환적으로호출된다.
def minimax(board, depth, maxPlayer):
    pos = -1
     # 단말노드이면보드를평가하여위치와평가값을반환한다.
    if depth == 0 or len(empty_cells(board)) == 0 or game_over(board):
         return -1, evaluate(board)

    if maxPlayer:
        value = -10000
        for p in empty_cells(board):
            board[p] = 'X'
            x, score = minimax(board, depth-1, False)
            board[p] = ' '
            if score > value:
                value = score
                pos = p
    else:
        value = +10000
        for p in empty_cells(board):
            board[p] = 'O'
            x, score = minimax(board, depth-1, True)
            board[p] =  ' '
            if score < value:
                value = score
                pos = p
    return pos, value

player='X'
player_turn = False
# 메인프로그램
while True:
     draw(game_board)
     if len(empty_cells(game_board)) == 0 or game_over(game_board):
        break
     if player_turn:
         i = int(input())
         if move(i, 'O'):
            player_turn = False
     else:
         i, v = minimax(game_board, 9, player=='X')
         move(i, player)
         player_turn = True



if check_win(game_board, 'X'):
    print('X 승리!')
elif check_win(game_board, 'O'):
    print('O 승리!')
else:
    print('비겼습니다!')