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



# 초기상태
puzzle = [2, 8, 3,
1, 6, 4,
7, 0, 5]
 # 목표상태
goal = [1, 2, 3,
8, 0, 4,
7, 6, 5]


# open 리스트
open_queue = [ ]
open_queue.append(State(puzzle, goal))
closed_queue = [ ]
optimal_route = [ ]
depth = 0
depth_depth = 0
ending = False
count=1
while True:
    open_queue = []
    open_queue.append(State(puzzle, goal))
    closed_queue = []
    optimal_route = []
    while len(open_queue) != 0:
        current = open_queue.pop(0)
        # OPEN 리스트의앞에서삭제
        #print(count)
        count += 1
        #print(current)
        if current.board == goal:
            print("탐색 성공")
            ending = True

            node = current
            while node is not None:
                optimal_route.append(node)
                node = node.parent
            break
        depth = current.depth+1
        closed_queue.append(current)
        if depth > depth_depth :
            continue
        for state in current.expand(depth):
            if (state in closed_queue) or (state in open_queue): # 이미 거쳐간 노드이면
                continue
            # 노드를버린다.
            else:
                open_queue.insert(0, state)
            # OPEN 리스트의끝에추가
    if ending:
        break
    depth_depth += 1

for route in reversed(optimal_route):
    print(route)
print("2021184002 길준형")
#2021184002 길준형