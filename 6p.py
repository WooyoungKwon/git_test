#6.1
def push(data):
    global size, stack, top
    if top >= size-1:
        print('스택이 꽉 찼습니다')
        return
    top += 1
    stack[top] = data


size = 5
# stack = [None for _ in range(size)
stack = ['커피', '녹차', '우유', '물', None]
top = 3

print(stack)
push('환타')
print(stack)
push('게토레이')