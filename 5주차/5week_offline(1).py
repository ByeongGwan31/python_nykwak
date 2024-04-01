import turtle
t = turtle.Turtle()
t.shape("turtle")
n = int(input("몇각형을 그리는지 입력하시오 : "))

for i in range(n):      #n회만큼 아래의 두 문장을 반복수행 한다

    t.forward(100)
    t.left(360 // n)

turtle.done()