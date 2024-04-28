# 3.7 - 사용자로부터 세 자리 정수를 입력 받으시오.

# n = int(input('세 자리 정수를 입력하시오 : '))
#
# # 백의 자리 구하기
# hundreds = n // 100
#
# # 십의 자리 구하기
# tens = (n % 100) // 10
#
# # 일의 자리 구하기
# ones = n % 10
#
# print(f'백의 자리 : {hundreds}')
# print(f'십의 자리 : {tens}')
# print(f'일의 자리 : {ones}')

# 3-8. 이동거리 구하기 : 평균 시속과 이동 시간

# average_speed = float(input('평균 시속(km/h)을 입력하세요 : '))
# total_time = float(input('이동 시간(h)을 입력하세요 : '))

# hours = int(total_time)
# minutes = int((total_time - hours) * 60)
# seconds = int(((total_time - hours) * 60 - minutes) * 60)

# distance = average_speed * total_time

# print(f'평균 시속 : {average_speed} km/h')
# print(f'이동 시간 : {hours} 시간 {minutes} 분 {seconds} 초')
# print(f'이동 거리 : {distance} km')


# 3-10. 다음과 같이 사용자로부터 두 점의 좌표 (x1, y1), (x2, y2)를 입력받아 두 점 사이의 거리를 출력하시오.

# import math

# x1 = float(input('x1 좌표를 입력하시오 : '))
# y1 = float(input('y1 좌표를 입력하시오 : '))
# x2 = float(input('x2 좌표를 입력하시오 : '))
# y2 = float(input('y2 좌표를 입력하시오 : '))

# distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

# print(f'두 점 사이이 거리 : {distance}')


# 3-12. 다음과 같은 공식을 참고하여 입체도형의 부피를 구하는 함수를 만드시오.

def cone_volume(r, h): # 원뿔
    return (1/3)*3.14*r**2*h

def circle_volume(r): # 구
    return (4/3)*3.14*r**3

def cylinder_volume(r, h):  # 원기둥
    return 3.14*r**2*h

cone_r = float(input('원뿔의 반지름을 입력하시오 : '))
cone_h = float(input('원뿔의 높이를 입력하시오 : '))

circle_r = float(input('구의 반지름을 입력하시오 : '))

cylinder_r = float(input('원기둥의 반지름을 입력하시오 : '))
cylinder_h = float(input('원기둥의 높이를 입력하시오 : '))

print(f'원뿔의 부피 : {cone_volume(cone_r, cone_h):.2f}')
print(f'구의 부피 : {circle_volume(circle_r):.2f}')
print(f'원기둥의 부피 : {cylinder_volume(cylinder_r, cylinder_h):.2f}')



