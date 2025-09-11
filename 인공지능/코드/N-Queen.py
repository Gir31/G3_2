import queue

# 상태를 나타내는 클래스
class State:
    def __init__(self, board, goal, depth=0, parent=None):
        self.board = board[:]       # 각 행(row)에 queen이 놓인 col (없으면 -1)
        self.goal = goal            # 목표: queen N개 배치
        self.depth = depth          # g(n)
        self.parent = parent

    # 현재 행(row)에 col에 배치 가능한지 검사
    def is_safe(self, row, col):
        for r in range(row):
            c = self.board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    # 자식 노드 확장
    def expand(self, depth):
        result = []
        row = self.depth  # 지금까지 놓은 queen 수 = 다음에 놓을 행
        if row < self.goal:
            for col in range(self.goal):
                if self.is_safe(row, col):
                    new_board = self.board[:]
                    new_board[row] = col
                    result.append(State(new_board, self.goal, depth, parent=self))
        return result

    # f(n) = g(n)+h(n)
    def f(self):
        return self.g() + self.h()

    def h(self):
        # 아직 배치해야 하는 queen 개수
        return self.goal - self.g()

    def g(self):
        return self.depth

    def __str__(self):
        out = ""
        for r in range(self.goal):
            row = ""
            for c in range(self.goal):
                if self.board[r] == c:
                    row += "Q "
                else:
                    row += ". "
            out += row + "\n"
        out += "------------------"
        return out

    def __eq__(self, other):
        return self.board == other.board

    def __lt__(self, other):
        return self.f() < other.f()


# 실행 부분
if __name__ == "__main__":
    N = int(input("N 입력: "))

    # 초기 상태: 모든 행을 -1로 (아직 queen 없음)
    puzzle = [-1] * N
    goal = N

    # open 리스트 = 우선순위 큐
    open_queue = queue.PriorityQueue()
    open_queue.put(State(puzzle, goal))
    closed_queue = []
    count = 0

    while not open_queue.empty():
        current = open_queue.get()
        count += 1
        print(f"{count}번째 상태 (f={current.f()}, g={current.g()}, h={current.h()})")
        print(current)

        if current.depth == goal:  # N개의 queen을 다 배치했으면 성공
            print("탐색 성공")
            break

        depth = current.depth + 1
        for state in current.expand(depth):
            if state not in closed_queue and state not in open_queue.queue:
                open_queue.put(state)
                closed_queue.append(current)
    else:
        print("탐색 실패")
