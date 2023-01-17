life = {
    'animals': {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'},
    'plants': ' ',
    'other': ' '
}
[print(key) for key in life]
[print(key) for key in life['animals'].keys()]
print(life['animals']['cats'])