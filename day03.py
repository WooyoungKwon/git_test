count = int(input())
j=1
score = 0
for i in range(count):
    arr = list(input())
    print(arr[0])
    if arr[i] == 'O':
        score += 1
        print('1')
        for j in range(count-1):
            print('1.5')
            if arr[i+j] == 'X':
                print('2')
                break
            elif arr[i+j] == 'O':
                print('3')
                score += j
print(score)
