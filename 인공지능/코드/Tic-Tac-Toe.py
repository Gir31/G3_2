# 보드는1차원리스트로구현한다.
game_board = [' ', ' ', ' ', ' ', ' ',
 ' ', ' ', ' ', ' ', ' ',
 ' ', ' ', ' ', ' ', ' ',
 ' ', ' ', ' ', ' ', ' ',
 ' ', ' ', ' ', ' ', ' ',]
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
         if i%5 == 0:
            print('\n-------------------------')
         print('|', cell , '|', end='')
     print('\n-------------------------')
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
    N = 5
    K = 3
    # 1차원 → 2차원 변환
    grid = [board[i * N:(i + 1) * N] for i in range(N)]

    # 가로 & 세로
    for i in range(N):
        for j in range(N - K + 1):
            # 가로
            if all(grid[i][j + x] == player for x in range(K)):
                return True
            # 세로
            if all(grid[j + x][i] == player for x in range(K)):
                return True

    # 대각선 ↘
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            if all(grid[i + x][j + x] == player for x in range(K)):
                return True

    # 대각선 ↙
    for i in range(N - K + 1):
        for j in range(K - 1, N):
            if all(grid[i + x][j - x] == player for x in range(K)):
                return True

    return False

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

def minimax_a_b(board, depth, maxPlayer, alpha = -10000, beta = 10000):
    pos = -1

    if depth == 0 or len(empty_cells(board)) == 0 or game_over(board):
        return -1, evaluate(board)

    if maxPlayer:
        value = -10000
        for p in empty_cells(board):
            board[p] = 'X'
            _, score = minimax_a_b(board, depth-1, False, alpha, beta)
            board[p] = ' '
            if score > value:
                value = score
                pos = p
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # 가지치기
    else:
        value = 10000
        for p in empty_cells(board):
            board[p] = 'O'
            _, score = minimax_a_b(board, depth-1, True, alpha, beta)
            board[p] = ' '
            if score < value:
                value = score
                pos = p
            beta = min(beta, value)
            if alpha >= beta:
                break  # 가지치기

    return pos, value


player='O'
player_turn = True
# 메인프로그램
while True:
     draw(game_board)
     if len(empty_cells(game_board)) == 0 or game_over(game_board):
        break
     if player_turn:
         i = int(input())
         if move(i, 'X'):
            player_turn = False
     else:
         i, v = minimax_a_b(game_board, 7, player=='O')
         move(i, player)
         player_turn = True



if check_win(game_board, 'X'):
    print('X 승리!')
elif check_win(game_board, 'O'):
    print('O 승리!')
else:
    print('비겼습니다!')