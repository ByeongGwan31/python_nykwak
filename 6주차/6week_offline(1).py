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

# import turtle

# t = turtle.Turtle()
# t.shape("turtle")

# s = turtle.textinput("", "도형을 입력하시오 : ")
# if s == '사각형':
#     s = turtle.textinput("", "가로:")
#     w = int(s)
#     s = turtle.textinput("", "세로:")
#     h = int(s)
#     t.forward(w) 
#     t.left(90) 
#     t.forward(h) 
#     t.left(90) 
#     t.forward(w) 
#     t.left(90) 
#     t.forward(h)
# elif s == "삼각형":
#      s = turtle.textinput("", "밑변: ") 
#      w = int(s) 
#      t.forward(w) 
#      t.left(120) 
#      t.forward(w)
#      t.left(120) 
#      t.forward(w)
# elif s == "원":
#     s = turtle.textinput("", "반지름: ") 
#     r = int(s)
#     t.circle(r)

# turtle.done()

# for i in "Hello":
#     print("i =", i)


# 5-4.

# for i in [1,2,3,4,5,6,7,8,9]:
#     print("9 *", i, "=", 9 * i)

# for i in range(9):
#     print('9 * ', i, '=', 9 * i)

# 5-6.

# for i in range(1, 6, 1):
#     print(i, end = " ")

# for i in range(10, 0, -1):
#     print(i, end = " ")

# # lab 5-1
# import turtle
# t = turtle.Turtle()

# for count in range(6):
#     t.circle(100)
#     t.left(360/6)

# lab 5-2
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# # 정삼각형
# for i in range(3):
#     t.forward(100)
#     t.left(360 / 3)

# # 정사각형 그리기 위한 터틀 이동
# t.penup()
# t.goto(200, 0)
# t.pendown()

# # 정사각형 그리기
# for i in range(4):
#     t.forward(100)
#     t.left(360 / 4)

# Lab 5-4

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# for i in range(6):
#     t.forward(100)
#     t.left(360 / 6)     # 360 / 4를 통해 90도 왼쪽으로 틀기

# turtle.done()

# # 도전문제 5-5.

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# s = turtle.textinput("", "몇각형을 원하시나요? :")
# n = int(s)

# width = turtle.textinput("", "한 변의 길이는 얼마인가요? :")
# w = int(width)

# for i in range(n):
#     t.forward(w)
#     t.left(360 / n)

# turtle.done()

# # Lab 5-4. 술에 취한 거북이

# import turtle
# import random
# t = turtle.Turtle()
# t.shape("turtle")

# for i in range(30):
#     length = random.randint(1, 100)
#     t.forward(length)

#     angle = random.randint(-180, 180)
#     t.right(angle)

# Lab 5 - 8. 별그리기
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# i = 0

# while i < 5:
#     t.forward(200)
#     t.right(144)
#     i = i + 1

# turtle.done()

# Lab 5-9. 나선형 도형 그리기
# import turtle
# t = turtle.Turtle()
# t.speed(0)
# t.width(3)

# length = 10
# while length < 500:
#     t.forward(length)
#     t.right(89)
#     length += 5

# turtle.done()

# Chanllenge 5-9.

# import turtle

# t = turtle.Turtle()
# # 거북이의 속도는 0으로 설정하면 최대가 된다. 
# t.speed(0)
# t.width(3)

# length = 10	  # 초기 선의 길이는 10으로 한다. 
# # while 반복문이다. 선의 길이가 500보다 작으면 반복한다.  
# while length < 500:	
#     t.forward(length)             # length만큼 전진한다. 
#     t.right(111)                       # 111도 오른쪽으로 회전한다. 
#     length += 5	        # 선의 길이를 5만큼 증가시킨다.
# turtle.done()

# lab 5-11.

# import random

# tries = 0
# guess = 0
# answer = random.randint(1, 100)

# print('1부터 100까지의 숫자를 맞추시오!')

# while guess != answer:
#     guess = int(input("숫자를 입력하시오 : "))
#     tries = tries + 1
#     if guess < answer:
#         print("숫자가 낮습니다!")
#     elif guess > answer:
#         print("숫자가 높습니다!")

# print(f'축하드립니다! 총 시도횟수 : {tries}')

# 5-10.

st = 'I love Python Programing'

for ch in st:
    if ch in ['a', 'e', 'i', 'o' , 'u', 'A', 'E', 'I', 'O', 'U']:
        continue            # 모음일 경우 아래 출력을 건너 뛴다.
    print(ch, end="")