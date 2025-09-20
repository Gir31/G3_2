# 2021184002 길준형
import queue

class State:
    def __init__(self, board, depth=0, N=0, positions=None, h_score=None):
        self.board = board
        self.depth = depth
        self.N = N

        self.positions = positions if positions is not None else []

        self.h_score = h_score if h_score is not None else self.h()

    def get_new_board(self, row):
        new_board = self.board[:]
        new_board[self.depth] = row
        new_positions = self.positions + [(row, self.depth)]
        new_h = self.h(new_positions)
        return State(new_board, self.depth + 1, self.N, new_positions, new_h)

    def expand(self):
        result = []
        used_rows = [False]*self.N
        for r, _ in self.positions:
            used_rows[r] = True
        for row in range(self.N):
            if not used_rows[row]:
                result.append(self.get_new_board(row))
        return result

    def g(self):
        return self.depth

    def h(self, positions=None):
        positions = positions if positions is not None else self.positions
        score = 0
        for i in range(len(positions)):
            r1, c1 = positions[i]
            for j in range(i+1, len(positions)):
                r2, c2 = positions[j]
                if abs(r1 - r2) == abs(c1 - c2):
                    score += 1
        return score

    def f(self):
        return self.g() + self.h_score

    def __lt__(self, other):
        return self.f() < other.f()

    def __hash__(self):
        return hash(tuple(self.board))

    def __eq__(self, other):
        return self.board == other.board

N = int(input("배치할 퀸의 개수 : "))
puzzle = [-1]*N

open_queue = queue.PriorityQueue()
start = State(puzzle, 0, N)
open_queue.put(start)
closed_set = set()
count = 0

while not open_queue.empty():
    current = open_queue.get()
    count += 1

    if current.depth == N and current.h_score == 0:
        print(f"탐색 성공! 시도 횟수: {count}")
        for r in range(N):
            line = ['.']*N
            line[current.board[r]] = 'Q'
            print(" ".join(line))
        break

    closed_set.add(tuple(current.board))

    for state in current.expand():
        if tuple(state.board) not in closed_set:
            open_queue.put(state)

print("2021184002 길준형")
