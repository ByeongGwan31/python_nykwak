# x, y, z = map(int, input('세 정수를 입력하시오 : ').split())
# print(f'{x}, {y}, {z}')

import random
random.random()

random.random()

random.randint(1, 7)        # 1이상 7이하 임의의 정수를 반환

random.randrange(7)         # 0부터 출발해서 6까지만 n-1

random.randrange(0, 10, 2)          # 0, 2, 4, 8 중 하나를 반환

lst = [10, 20, 30, 40, 50]
random.shuffle(lst)
lst
random.choice(lst)