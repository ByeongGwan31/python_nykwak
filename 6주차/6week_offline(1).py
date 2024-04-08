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
#     print('앞면입니다!
# else :
#     print('뒷면입니다!')
# print("게임이 종료되었습니다.")

## 원의 내부에 있는 점일까 외부에 있는 점일까
# x, y = map(float, input('점의 좌표 x, y를 입력하시오 : ').split())

# if (x-3) ** 2 + (y-4) ** 2 > 10 ** 2:
#     print('원의 외부에 있음')
# else:
#     print('원의 내부에 있음')
    

# 사용자로부터 아이디를 받아서 프로그램에 저장된 아이디 'ilovepython'과 일치하는지 여부를 출력하는 프로그램을 작성하라.
# id = 'ilovepython'
# password = 'mypass1234'

# id_2 = input('아이디를 입력하시오 : ')
# pw_2 = input('패스워드를 입력하시오 : ')

# if id == id_2 and password == pw_2: 
#     print('환영합니다.')
# elif id != id_2:
#     print('아이디를 찾을 수 없습니다!')
# else:
#     print('비밀번호가 틀렸습니다.')

# 4-9. 입력을 받아서 도형 그리기를 해보자.

import turtle

t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("", "도형을 입력하시오 : ")
if s == '사각형':
    s = turtle.textinput("", "가로:")
    w = int(s)
    s = turtle.textinput("", "세로:")
    h = int(s)
    t.forward(w) 
    t.left(90) 
    t.forward(h) 
    t.left(90) 
    t.forward(w) 
    t.left(90) 
    t.forward(h)
elif s == "삼각형":
     s = turtle.textinput("", "밑변: ") 
     w = int(s) 
     t.forward(w) 
     t.left(120) 
     t.forward(w)
     t.left(120) 
     t.forward(w)
elif s == "원":
    s = turtle.textinput("", "반지름: ") 
    r = int(s)
    t.circle(r)

turtle.done()





