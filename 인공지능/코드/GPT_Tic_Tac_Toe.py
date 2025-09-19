# 보드는 1차원 리스트
game_board = [' '] * 25  # 5x5

# 비어있는 칸을 찾는다.
def empty_cells(board):
    return [i for i, cell in enumerate(board) if cell == ' ']

# 비어있는 칸에만 둘 수 있다.
def valid_move(x):
    return x in empty_cells(game_board)

# 위치 x에 플레이어 돌을 놓는다.
def move(x, player):
    if valid_move(x):
        game_board[x] = player
        return True
    return False

# 현재 게임 보드를 출력한다.
def draw(board):
    for i, cell in enumerate(board):
        if i % 5 == 0:
            print('\n-------------------------')
        print('|', cell, '|', end='')
    print('\n-------------------------')

# 승리 조건 검사
def check_win(board, player, N=5, K=4):
    grid = [board[i * N:(i + 1) * N] for i in range(N)]

    # 가로/세로
    for i in range(N):
        for j in range(N - K + 1):
            if all(grid[i][j + x] == player for x in range(K)):
                return True
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

# 게임 종료 여부
def game_over(board):
    return check_win(board, 'X') or check_win(board, 'O')

# -----------------------
# 개선된 평가 함수
# -----------------------
def evaluate(board, N=5, K=4):
    def score_line(line, player):
        opp = 'O' if player == 'X' else 'X'
        score = 0
        for i in range(len(line) - K + 1):
            window = line[i:i+K]
            if opp not in window:  # 상대 돌이 없을 때만
                count = window.count(player)
                if count > 0:
                    # 연속 개수에 따라 점수 크게 부여
                    score += (10 ** count) if player == 'X' else -(10 ** count)
        return score

    grid = [board[i*N:(i+1)*N] for i in range(N)]
    total_score = 0

    # 가로, 세로
    for i in range(N):
        total_score += score_line(grid[i], 'X')
        total_score += score_line(grid[i], 'O')

        col = [grid[r][i] for r in range(N)]
        total_score += score_line(col, 'X')
        total_score += score_line(col, 'O')

    # 대각선 ↘
    for r in range(N-K+1):
        for c in range(N-K+1):
            diag = [grid[r+k][c+k] for k in range(K)]
            total_score += score_line(diag, 'X')
            total_score += score_line(diag, 'O')

    # 대각선 ↙
    for r in range(N-K+1):
        for c in range(K-1, N):
            diag = [grid[r+k][c-k] for k in range(K)]
            total_score += score_line(diag, 'X')
            total_score += score_line(diag, 'O')

    return total_score

# 미니맥스 + 알파베타 가지치기
def minimax_a_b(board, depth, maxPlayer, alpha=-10000, beta=10000):
    pos = -1
    if depth == 0 or len(empty_cells(board)) == 0 or game_over(board):
        return -1, evaluate(board)

    if maxPlayer:  # X (AI)
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
                break
    else:  # O (사람)
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
                break

    return pos, value

# -----------------------
# 메인 루프
# -----------------------
player = 'O'  # 사람은 O, AI는 X
player_turn = True

while True:
    draw(game_board)
    if len(empty_cells(game_board)) == 0 or game_over(game_board):
        break

    if player_turn:
        i = int(input("당신의 수 (0~24): "))
        if move(i, 'O'):
            player_turn = False
    else:
        i, _ = minimax_a_b(game_board, 5, True)  # depth=5
        move(i, 'X')
        player_turn = True

draw(game_board)

if check_win(game_board, 'X'):
    print('X 승리!')
elif check_win(game_board, 'O'):
    print('O 승리!')
else:
    print('비겼습니다!')
