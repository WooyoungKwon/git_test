def isQueueFull():
    global SIZE, queue, front, rear
    if (rear + 1 % SIZE) == front:
        return True
    else:
        return False


def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False


def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('통화 대기가 꽉 찼습니다.')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data


def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('줄이 없습니다')
        return
    data = queue[front + 1]
    queue[front + 1] = None
    return data


def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐가 비었음')
        return None
    return queue[front + 1]


def calcTime():
    global SIZE, queue, front, rear
    TSum = 0
    for i in range(front+1, rear + 1):
        TSum += queue[i][1]
    return TSum


SIZE = 6
queue = [None for _ in range(SIZE)]
front = rear = 0

if __name__ == '__main__':
    waitCall = [('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4), ('고장', 3)]
    for i in waitCall:
        print("귀하의 현재 사용 대기시간은 ", calcTime(), '분 입니다.')
        print('현재 대기 콜 -> ', queue)
        enQueue(i)
        print()

    print('최종 대기콜 : ', queue)
    print('프로그램 종료')