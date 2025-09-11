import queue

 # 상태를나타내는클래스
class State:
    def __init__(self, board, goal, depth=0, parent = None):
        self.board = board
        self.depth = depth
        self.goal = goal
        self.parent = parent
    # i1과i2를교환하여서새로운상태를반환한다.
    def get_new_board(self, i1, i2, depth):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, depth, parent = self)

    # 자식노드를확장하여서리스트에저장하여서반환한다.
    def expand(self, depth):
        result = []
        #if depth > 5: return result  # 깊이가 5 이상이면 더 이상 확장을하지않는다.
        i = self.board.index(0) # 숫자 0(빈칸)의 위치를 찾는다.
        if not i in [0, 3, 6] : # LEFT 연산자
            result.append(self.get_new_board(i, i-1, depth))
        if not i in [0, 1, 2] : # UP 연산자
            result.append(self.get_new_board(i, i-3, depth))
        if not i in [2, 5, 8]:
        # RIGHT 연산자
            result.append(self.get_new_board(i, i+1, depth))
        if not i in [6, 7, 8]:
        # DOWN 연산자
            result.append(self.get_new_board(i, i+3, depth))
        return result
        # 객체를출력할때사용한다.
    #f(n)을 계산하여 반환한다.
    def f(self):
        return self.h()+self.g()

    # 휴리스틱함수값인h(n)을계산하여반환한다.
    # 현재제위치에있지않은타일의개수를리스트함축으로계산한다.
    def h(self):
        score = 0
        for i in range(9):
            if self.board[i] != 0 and self.board[i] != self.goal[i]:
                score += 1
        return score
    #def h2(self):

    # 시작노드로부터의깊이를반환한다.
    def g(self):
        return self.depth

    def __str__(self):
        return str(self.board[:3]) +"\n"+\
        str(self.board[3:6]) +"\n"+\
        str(self.board[6:]) +"\n"+\
        "------------------"
    def __eq__(self, other):
        # 이것을정의해야in 연산자가올바르게계산한다.
        return self.board == other.board
    def __ne__(self, other):
        # 이것을정의해야in 연산자가올바르게계산한다.
        return self.board != other.board

    # 상태와상태를비교하기위하여less than 연산자를정의한다.
    def __lt__(self, other):
        return self.f() < other.f()

    def __gt__(self, other):
        return self.f() > other.f()

# 초기상태
puzzle = [2, 8, 3,
1, 6, 4,
7, 0, 5]
 # 목표상태
goal = [1, 2, 3,
8, 0, 4,
7, 6, 5]

# 초기상태
puzzle = [2, 8, 3,
1, 6, 4,
7, 0, 5]
 # 목표상태
goal = [1, 2, 3,
8, 0, 4,
7, 6, 5]

# open 리스트는우선순위큐로생성한다.
open_queue = queue.PriorityQueue()
open_queue.put(State(puzzle, goal))
closed_queue = [ ]
depth = 0
count = 0
while not open_queue.empty():
    current = open_queue.get()
    count += 1
    print(count)
    print(current)
    if current.board == goal:
        print("탐색 성공")
        break
    depth = current.depth+1
    for state in current.expand(depth):
        if state not in closed_queue and state not in open_queue.queue :
            open_queue.put(state)
            closed_queue.append(current)
        else:
            print ('탐색 실패')