def find_and_insert_data(pokemon_name, hp):
    pokemon_key = []
    pokemon_value = []
    for i, j in Pokemon.items():
        pokemon_key.append(i)
        pokemon_value.append(j)

    for i in range(len(pokemon_value)):
        if pokemon_value[i] < hp:
            pokemon_value.append(None)
            for j in range(-2, -(len(pokemon_value)), -1):
                pokemon_value[i+1] = pokemon_value[i]


def inset_data(idx, new_data):
    if idx < 0 or idx > len(KakaoTalk):
        print("범위 벗어남")
    KakaoTalk.append(None)
    for i in range((len(KakaoTalk))-1, idx, -1):
        KakaoTalk[i] = KakaoTalk[i-1]
        KakaoTalk[i-1] = None
    KakaoTalk[idx] = new_data
    print(KakaoTalk)


# Pokemon = {'피카츄': 800, '라이츄': 1000, '파이리': 100, '꼬부기': 70, '버터풀': 1, '야도란': 0}
Pokemon = [1, 2, 3, 4, 5]

Pokemon.append(None)
for j in range(-2, -7, -1):
    # pair = Pokemon[j+1]
    Pokemon[j+1] = Pokemon[j]
    print(Pokemon)

for i in range(len(pokemon_value)):
    if pokemon_value[i] < hp:
        pokemon_value.append(None)
        for j in range(-2, -(len(pokemon_value)), -1):
            pokemon_value[i+1] = pokemon_value[i]
#     print(i, j)
# print(Pokemon['피카츄']) # value 값 뽑는 방식
# name = input('이름')
# call = int(input('연락 횟수'))

# find_and_insert_data(name, call)


# KakaoTalk_sl = KakaoTalk[1:]
# print(KakaoTalk_sl)
# print(len(KakaoTalk[1:]))