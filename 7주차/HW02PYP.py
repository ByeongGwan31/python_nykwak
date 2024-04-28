# 4.4 하나의 정수를 입력으로 받아서 이 정수가 2로 나누어지는지, 
# 3으로 나누어지는지, 혹은 두 정수 모두로도 나누어지는지 알려주는 프로그램을 다음과 같이 작성하시오. 
# 예를 들어 15와 같은 수가 입력되면 다음 출력 결과와 같은 화면이 나타나면 된다.

# number = int(input('정수를 입력하시오 : '))

# if number % 2 == 0:
#     print(f'{number}는 2(으)로 나누어집니다.')
# else:
#     print(f'{number}는 2(으)로 나누어지지 않습니다')

# if number % 3 == 0:
#     print(f'{number}은 3(으)로 나누어집니다.')
# else:
#     print(f'{number}은 3(으)로 나누어지지 않습니다.')

# if number % 2 == 0 and number % 3 == 0:
#     print(f'{number}은 2와 3(으)로 나누어집니다.')
# else:
#     print(f'{number}은 2와 3(으)로 나누어지지 않습니다.')

# 4.5 random.randint(0, 9)를 사용하여 0에서 9사이의 복권번호 3개를 생성하도록 하자.
# 이들 중에서 3개의 숫자를 모두 맞치면 1억원, 2개를 맞히면 1천만원, 1개를 맞히면 1만원, 모두 틀리면 다음 기회에...
# 을 출력하는 복권 시스템, 사용자로부터 3개의 정수를 받은 다음 상금을 받는 시스템을 작성
# 랜덤하게 생성한 복권 당첨 번호가 2, 3, 9라고 가정

# import random

# winNumber = [2, 3, 9]

# userNumber = list(map(int, input("세 복권번호를 입력하시오: ").split()))

# matchCount = 0

# for num in userNumber:
#     if num in winNumber:
#         matchCount += 1

# if matchCount == 3:
#     print('상금 1억원')
# elif matchCount == 2:
#     print('상금 1천만원')
# elif matchCount == 1:
#     print('상금 1만원')
# else:
#     print('다음 기회에...')

# 5-6. 다음과 같이 자동차의 연료 탱크 프로그램을 시뮬레이션하여 보자.

# oil = 500

# while True:
#     user = input("충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오: ")

#     oil += int(user)

#     print(f'현재 탱크양은 {oil} 입니다.')

#     if oil < 50:
#         print("경고 : 연료가 10% 미만이니 충전하세요!")
#         break
# 500의 10%는 50이다.

# 5-8. 거꾸로 정수 121이나 3443와 같이 거꾸로 나열해도 그 값이 원래의 값과 같은 정수를 의미

# while True:
#     num = input("정수를 입력하시오 : ")

#     if num == "-99":
#         print("프로그램을 종료합니다.")
#         break

#     if num == num[::-1]:
#         print(f'{num}은(는) 거꾸로 정수입니다.')
#     else:
#         print(f'{num} 은(는) 거꾸로 정수가 아닙니다.')


# 5-9. 사용자로부터 임의의 양의 정수를 입력 받아, 다음과 같이 입력된 정수의 개수와, 가장 큰 값, 가장 작은 값을 출력하도록 하자.
# 입력을 받을 때, -99가 들어올 경우 더이상 입력을 받지 않는다.abs

max_num = None
min_num = None
count = 0

while True:
    num = int(input('정수를 입력하시오 : '))

    if num == -99:
        break

    if max_num is None or num > max_num:
        max_num = num
    if min_num is None or num < min_num:
        min_num = num

    count = count + 1

if count > 0:
    print(f'{count}개의 유효한 정수 중 가장 큰 정수는 {max_num} 이고, 가장 작은 정수는 {min_num} 입니다.')
else:
    print("정수를 입력해주세요.")