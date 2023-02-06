class Node:
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()


def insertNode(findData, insertData):
    global memory, head, current, pre

    if head.data == findData:  # 첫 번째 노드 삽입
        node = Node()
        node.data = insertData
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return
    current = head
    while current.link != head:  # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = pre.link
            pre.link = node
            return

    node = Node()
    node.data = insertData
    current.link = node
    node.link = head


def deleteNode(deleteData):
    global memory, head, current, pre

    if head.data == deleteData:
        current = head  # head 노드(첫 번째 노드)를 current 노드에 저장
        head = head.link  # head를 head 다음 노드로 변경
        last = head
        while last.link != current:  # 마지막 노드까지 이동
            last = last.link
        last.link = head  # 마지막 노드를 head랑 연결
        del current
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del current
            return


def findNode(findData):
    global memory, head, current, pre

    current = head
    if current.data == findData:
        print('# 첫 노드에서 찾음 #')
        return current
    while current.link != head:
        current = current.link
        if current.data == findData:
            print('# 중간 노드에서 찾음 #')
            return current
    print('# 찾는 노드가 없음 #')
    return Node()


# 전역 변수
memory = []
head, current, node = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']
# 메인 코드 실행
if __name__ == "__main__":

    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node  # data 갯수가 몇 개인지 모르기 때문에, 같은 변수명(node)를 사용한다.
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    fNode = findNode('다현')
    print(fNode.data)
    fNode = findNode('쯔위')
    print(fNode.data)
    fNode = findNode('재남')
    print(fNode.data)