def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False


def isQueueFull():
    global SIZE, queue, front, rear
    if rear == SIZE-1:
        return True
    else:
        return False


def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('대기 마감')
        return
    rear += 1
    queue[rear] = data


def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('줄이 없습니다')
        return
    data = queue[front+1]
    queue[front+1] = None

    for i in range(front+2, rear+1):
        queue[i-1] = queue[i]
        queue[i] = None
    rear -= 1
    return data


SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1


if __name__ == '__main__':
    enQueue('정국')
    enQueue('뷔')
    enQueue('지민')
    enQueue('진')
    enQueue('슈가')
    print('대기줄 상태 : ', queue)

    for _ in range(rear+1):
        print(deQueue(), '님 식당에 들어감')
        print('대기줄 상태 : ', queue)

    print('영업 종료!')
