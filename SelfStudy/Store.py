## 함수 선언 부분 ##
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def printGraph(g):
    print(' ', end=' ')
    for v in range(g.SIZE):
        print('%9s' % nameAry[v][0], end=' ')
    print()
    for row in range(g.SIZE):
        print('%9s' % nameAry[row][0], end=' ')
        for col in range(g.SIZE):
            print("%8d" % g.graph[row][col], end=' ')
        print()
    print()



nameAry = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['MiniStop', 90], ['Emart24', 40]]
GS25, CU, Seven11, MiniStop, Emart24 = 0, 1, 2, 3, 4

## 메인 코드 부분 ##
G1 = Graph(5)
G1.graph[GS25][CU] = 1; G1.graph[GS25][Seven11] = 1
G1.graph[CU][GS25] = 1; G1.graph[CU][Seven11] = 1; G1.graph[CU][MiniStop] = 1
G1.graph[Seven11][GS25] = 1; G1.graph[Seven11][CU] = 1; G1.graph[Seven11][MiniStop] = 1
G1.graph[MiniStop][Seven11] = 1; G1.graph[MiniStop][CU] = 1; G1.graph[MiniStop][Emart24] = 1
G1.graph[Emart24][MiniStop] = 1

printGraph(G1)

stack = []
visitedAry = []
current = 0
stack.append(current)
visitedAry.append(current)

maxSnack = 0
maxName = current
while len(stack) != 0:
    next = None
    for vertex in range(5):
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
        if nameAry[current][1] > maxSnack:
            maxSnack = nameAry[current][1]
            maxName = current
    else:
        current = stack.pop()

print('최대 보유 편의점 -> ', nameAry[maxName][0], '(', nameAry[maxName][1], ')')
# while len(stack) != 0:
#     next = None
#     for vertex in range(5):
#         if G1.graph[current][vertex] == 1:
#             if vertex in visitedAry:
#                 pass
#             else:
#                 next = vertex
#                 break
#     if next != None:
#         current = next
#         stack.append(current)
#         visitedAry.append(current)
#     else:
#         current = stack.pop()
#
# print('방문 순서 --> ', end=' ')
# for i in visitedAry:
#     # print(chr(ord('A') + i), end=' ')
#     print(mamamoo[i], end=' ')