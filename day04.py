#8.13
ZipKey = ('optimist', 'pessimist', 'troll')
ZipValue = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')

aa = {k: v for k, v in zip(ZipKey, ZipValue)}
print(aa)

#8.14
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
print(movies)