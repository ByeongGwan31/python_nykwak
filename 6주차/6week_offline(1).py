# ## 윤년 계산기

# year = int(input('연도를 입력하시오 : '))

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(f'{year}은 윤년입니다.')
# else:
#     print(f'{year}은 윤년이 아닙니다.')


## 랜덤 함수로 동전 던지기 게임 만들기

# import random

# print('동전 던지기 게임을 시작합니다.')
# coin = random.randrange(2)

# if coin == 0:
#     print('앞면입니다!')
# else :
#     print('뒷면입니다!')
# print("게임이 종료되었습니다.")

## 원의 내부에 있는 점일까 외부에 있는 점일까
x, y = map(float, input('점의 좌표 x, y를 입력하시오 : ').split())

if (x-3) ** 2 + (y-4) ** 2 > 10 ** 2:
    print('원의 외부에 있음')
else:
    print('원의 내부에 있음')