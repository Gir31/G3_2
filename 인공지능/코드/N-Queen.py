import queue

class State:
    def __init__(self, board, depth = 0, N = 0):
        self.board = board
        self.depth = depth
        self.N = N

    def get_new_board(self, row):
        new_board = self.board[:]
        new_board[self.depth] = row
        return State(new_board, self.depth + 1, self.N)

    def expand(self):
        result = []
        used_rows = set(self.board[:self.depth])  # 이미 배치된 행 번호
        for row in range(self.N):
            if row not in used_rows:  # 이미 사용된 행은 제외
                result.append(self.get_new_board(row))
        return result

    def f(self):
        return self.h() + self.g()

    def h(self):
        score = 0
        positions = [(self.board[col], col) for col in range(self.depth)]

        for i in range(len(positions)):
            r1, c1 = positions[i]
            for j in range(i + 1, len(positions)):
                r2, c2 = positions[j]
                # 같은 행
                if r1 == r2:
                    score += 1
                # 같은 대각선
                if abs(r1 - r2) == abs(c1 - c2):
                    score += 1

        return score

    def g(self):
        return self.depth

    def __str__(self):
        lines = []
        for r in range(self.N):
            line = []
            for c in range(self.N):
                if c < self.depth and self.board[c] == r:
                    line.append('Q')
                else:
                    line.append('.')
            lines.append(" ".join(line))
        return "\n".join(lines) + "\n" + "-" * 20

    def __eq__(self, other):
        return self.board == other.board

    def __ne__(self, other):
        return self.board != other.board

    def __lt__(self, other):
        return self.f() < other.f()

    def __gt__(self, other):
        return self.f() > other.f()

N = int(input("배치할 퀸의 개수 : "))

puzzle = [-1] * N

open_queue = queue.PriorityQueue()
open_queue.put(State(puzzle, 0, N))
closed_queue = [ ]
depth = 0
count = 0

while not open_queue.empty():
    current = open_queue.get()
    count += 1
    print(f"상태 {count}:")
    print(current)

    if current.depth == N and current.h() == 0:
        print("탐색 성공! 최종 해:")
        print(current)
        break

    depth = current.depth + 1
    for state in current.expand():
        if state not in closed_queue and state not in open_queue.queue:
            open_queue.put(state)
            closed_queue.append(current)