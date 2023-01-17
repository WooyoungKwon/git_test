start1 = ["fee", 'fie', 'foe']
rhymes = [
    ('flop', 'get a mop'),
    ('fope', 'turn the rope'),
    ('fa', 'get your ma'),
    ('fudge', 'call the judge'),
    ('fat', 'pet the cat'),
    ('fog', 'walk the dog'),
    ('fun', "say we're done"),
]
start2 = 'Someone better'
for i in range(3):
    start1[i] = start1[i].title()

start1 = '! '.join(start1)
print(start1 + '! ' + (rhymes[0][0].title() + '!'))
print(start2, rhymes[0][1] + '.')