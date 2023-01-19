def selfNumber(n):
    all_number = {i for i in range(n)} # 1부터 n까지의 set 생성
    con_number = set() # 생성자가 존재하는 정수가 담길 set 생성

    for i in all_number: # all_number의 길이를 재서 돌아가게 하고 i에 all_number의 객체가 들어가는 부분은 따로 구현
        temp = []
        # 리스트로 변환해서 자릿수 별로 나누기
        for j in str(i):
            temp.append(j)
            # 계산을 위해 다시 정수로 변환
            for k in range(len(temp)):
                temp[k] = int(temp[k])
        print(temp)
        hap = i + int(temp[0]) + int(temp[1]) # 한 자릿 수는 계산이 불가능 하기 때문에 인덱스 에러 발생
        # print(f'temp{int(temp[0])}')

        con_number.add(hap)
    return print(f'이건가{all_number - con_number}')

selfNumber(100)
# aa = {1, 2, 3, 4}
# bb = {2, 3, 4, 6}
# print(aa & bb)