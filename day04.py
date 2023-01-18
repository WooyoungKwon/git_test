ox = input()
ox = list(ox)
moScore = 0
score = 0
print(ox)
for i in ox:
    if i == 'O':
        moScore += 1
        score += moScore
    else:
        moScore = 0
print(score)