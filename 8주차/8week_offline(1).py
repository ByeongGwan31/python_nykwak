# 도전문제 6.3

# def get_square(a, b, c):
#     return a ** 2, b ** 2, c ** 2

# a, b, c = 1, 2, 3
# a_sq, b_sq, c_sq = get_square(a, b, c)

# print(a, '제곱 : ', a_sq, ', ', b, '제곱 : ', b_sq, ', ', c, '제곱 : ', c_sq)


# n-각형을 그리는 함수 만들기
# import turtle
# t = turtle.Turtle()

# # n-각형을 그리는 함수를 정의한다.
# def n_polygon(n, length):
#     for i in range(n):
#         t.forward(length)
#         t.left(360 // n)            # 정수 나눗셈은 //으로 한다.

# # for i in range(10):
# #     t.left(20)
# #     n_polygon(6, 100)

# for i in range(20):
#     t.left(30)
#     n_polygon()

# default argument
# def order(num, pickle = True, onion = True) :
#     print('햄버거 {0} 개 - 피클 {1}, 양파 {2}'.format(num, pickle, onion))

# order(1, pickle = False, onion = True)
# order(2)

# 주급 계산 프로그램
# def weeklyPay(rate, hour):
#     if (hour > 30):
#         money = rate * 30 + 1.5 * rate * (hour - 30)
#     else:
#         money = rate * hour
#     return money

# r = int(input("시급을 입력하시오 : "))      # 시급입력받기
# h = int(input("근무 시간을 입력하시오 : "))        # 근무시간 입력받기

# print("주급은 " + str(weeklyPay(rate = r, hour = h)))

# import turtle

# def drawBar(height):
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.write(str(height), font = ('Times New Roman', 16, 'bold'))
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()

# data = [120, 56, 309, 220, 156, 23, 98]

# t = turtle.Turtle()
# t.color("blue")
# t.fillcolor("red")
# t.pensize(3)

# for d in data:
#     drawBar(d)

# turtle.done()

# Lab 6-6 거북이에게 이차함수를 그리게 하자
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(0)  # 터틀 그래픽의 그리기 속도를 가장 빠르게 한다

# def f(x):  # 2차 함수를 만든다
#     return x ** 2 + 1

# t.goto(200, 0)
# t.goto(0, 0)
# t.goto(0, 200)
# t.goto(0, 0)

# for x in range(150):
#     t.goto(x, int(0.01 * f(x)))
    
# turtle.done()

# 6.12 자신을 호출하는 재귀 함수

# def fibonacci(n):
#     if n < 0:
#         print("잘못된 입력입니다.")
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# i = int(input("몇 번째 항 : "))
# print(fibonacci(i))


# 6.13 모듈 이용 -> 함수를 재사용
import datetime

datetime.datetime.now()
today = datetime.date.today()
print(today)