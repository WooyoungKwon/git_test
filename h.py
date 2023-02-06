def insert_data(index, pokemon):
    if index < 0 or index > len(pokemons):
        print("Out of range!")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons) - 1, index, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[index] = pokemon
    #


# 함수 사이 줄바꿈 2개(권고 규정)
def delete_data(index):
    if index < 0 or index > len(pokemons):
        print("Out of range!")
        return

    len_pokemons = len(pokemons)  # python에서 kLen같은 표기는 지양
    pokemons[index] = None  # 데이터 삭제

    for i in range(index + 1, len_pokemons):
        pokemons[i - 1] = pokemons[i]
        pokemons[i] = None
    pokemons.pop()


# main 함수처럼 만들기
if __name__ == "__main__":
    pokemons = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]

    print(pokemons)
    delete_data(2)
    print(pokemons)x`