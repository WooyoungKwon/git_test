guess_me = 5
number = 1
for i in range(number, 10):
    if i < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break