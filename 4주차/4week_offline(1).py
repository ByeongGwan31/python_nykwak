'''
string = "키 : {:^10}, 몸무게 : {:>10}".format(height, weight)
print(string)
string = "키 : {1:10}, 몸무게 : {0}".format(height, weight)
print(string)

string = "x좌표 : {x}, y좌표 : {y}".format(x=10, y=20)
print(string)
'''

'''
import turtle

t = turtle.Turtle()
t.shape('turtle')

radius = 100
t.circle(radius)

radius = 200
t.circle(radius)
'''

'''
import turtle

t = turtle.Turtle()
t.shape('turtle')

radius = 100
t.circle(radius)           # 반지름이 100인 원을 그린다.

radius = 200
t.circle(radius)           # 반지름이 200인 원을 그린다.

radius = 50
t.circle(radius)           # 반지름이 50인 원을 그린다.

turtle.done()
'''

'''
principal = 100000000
years = 30
interest_rate = 0.03
money = principal * (1.0 + interest_rate) ** years
print('원금 : ', principal)
print('이율 : ', interest_rate)
print('기간 : ', years)
print('수령금액 : ', money)
'''

'''
print(1/3)
'''


'''
x = int(input("첫 번째 정수를 입력하시오 : "))
y = int(input("두 번째 정수를 입력하시오 : "))

s = x + y
print(x, "과", y, "의 합은", s, "입니다.")
'''


# 사용자의 대답을 변수에 저장한다.
stadium = input("경기장을 입력하시오 : ")
winner = input("이긴팀을 입력하시오 : ")
loser = input("진 팀을 입력하시오 : ")
vip = input("우수선수를 입력하시오 : ")
score = input("스코어를 입력하시오 : ")

# 사용자의 입력을 바탕으로 기사를 작성
print("")
print("========================================")
print(f"오늘 {stadium} 에서 야구 경기가 열렸습니다. ")
print(f"{winner}과 {loser}은 치열한 공방전을 펼쳤습니다.")
print(f"{vip}의 맹활약으로, {winner}가, {loser}을 {score}로 이겼습니다.")
print("========================================")


## 핵심 정리
print()


