squares = {k: k**2 for k in range(10)}
odd = {num for num in squares if num % 2 == 1}
generator = (ge for ge in odd)
for i in generator:
    print(i)
