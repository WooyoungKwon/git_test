#6.1
def push(data):
    global SIZE, stack, top
    if top >= size-1:
        print('스택이 꽉 찼습니다')
        return
    top += 1
    stack[top] = data


def isStackEmpty():
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False


def pop():
    global SIZE, stack, top
    if isStackEmpty():
        print('스택이 비었습니다')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


def peek():
    global SIZE, stack, top
    if isStackEmpty():
        print("스택이 비었습니다")
        return None
    return stack[top]


SIZE = 5
stack = ['커피', None, None, None, None]
top = 0

print(stack)
retData = peek()
print('데이터 ---> ', retData)
print(stack)
retData = pop()