## 함수 선언 부분 ##
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


## 전역 변수 선언 부분 ##
G1 = None
stack = []
visitedAry = []
store = ['GS25', 'CU', 'SevenEleven', 'MiniStop', 'Emart24']
GS25, CU, SevenEleven, MiniStop, Emart24 = 0, 1, 2, 3, 4

## 메인 코드 부분 ##
G1 = Graph(6)
G1.graph[GS25][CU] = 1; G1.graph[GS25][SevenEleven] = 1
G1.graph[CU][GS25] = 1; G1.graph[CU][SevenEleven] = 1; G1.graph[CU][MiniStop] = 1
G1.graph[SevenEleven][GS25] = 1; G1.graph[SevenEleven][CU] = 1; G1.graph[SevenEleven][MiniStop] = 1
G1.graph[MiniStop][SevenEleven] = 1; G1.graph[MiniStop][CU] = 1; G1.graph[MiniStop][Emart24] = 1
G1.graph[Emart24][MiniStop] = 1


print('## G1 무방향 그래프 ##')
for row in range(6):
    for col in range(6):
        print(G1.graph[row][col], end=' ')
    print()

current = 0
stack.append(current)
visitedAry.append(current)

while len(stack) != 0:
    next = None
    for vertex in range(6):
        if G1.graph[current][vertex] == 1:
            if vertex in visitedAry:
                pass
            else:
                next = vertex
                break
    if next != None:
        current = next
        stack.append(current)
        visitedAry.append(current)
    else:
        current = stack.pop()

print('방문 순서 --> ', end=' ')
for i in visitedAry:
    # print(chr(ord('A') + i), end=' ')
    print(mamamoo[i], end=' ')