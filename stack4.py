# SIZE = 5
# queue = [None for _ in range(SIZE)]
# front = rear = -1
def enQueue(data):
    global SIZE, queue, front, rear
    if rear == SIZE-1 and front == -1:
        print('큐가 꽉 찼습니다')
        return
    rear += 1
    queue[rear] = data


def deQueue():
    global SIZE, queue, front, rear
    if front == rear:
        print('큐가 비었습니다')
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data


def peek():
    global SIZE, queue, front, rear
    return queue[front+1]


SIZE = int(input('큐 크기를 입력하세요 : '))
queue = [None for _ in range(SIZE)]
front = rear = -1

if __name__ == '__main__':
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나 선택 : ")

    while True:
        if select == 'x' or select == 'X':
            print('프로그램 종료')
            break
        elif select == 'I' or select == 'i':
            data = input('입력할 데이터 : ')
            enQueue(data)
            print('큐 상태 : ', queue)
        elif select == 'E' or select == 'e':
            data = deQueue()
            print('추출된 데이터 -> ', data)
            print('큐 상태 : ', queue)
        elif select == 'V' or select == 'v':
            data = peek()
            print('확인된 데이터 -> ', data)
            print('큐 상태 : ', queue)
        else:
            print('잘못된 입력')

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나 선택 : ")
