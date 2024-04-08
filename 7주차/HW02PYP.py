# 4.4 하나의 정수를 입력으로 받아서 이 정수가 2로 나누어지는지, 
# 3으로 나누어지는지, 혹은 두 정수 모두로도 나누어지는지 알려주는 프로그램을 다음과 같이 작성하시오. 
# 예를 들어 15와 같은 수가 입력되면 다음 출력 결과와 같은 화면이 나타나면 된다.

number = int(input('정수를 입력하시오 : '))

if number % 2 == 0:
    print(f'{number}는 2(으)로 나누어집니다.')
else:
    print(f'{number}는 2(으)로 나누어지지 않습니다')

if number % 3 == 0:
    print(f'{number}은 3(으)로 나누어집니다.')
else:
    print(f'{number}은 3(으)로 나누어지지 않습니다.')

if number % 2 == 0 and number % 3 == 0:
    print(f'{number}은 2와 3(으)로 나누어집니다.')
else:
    print(f'{number}은 2와 3(으)로 나누어지지 않습니다.')

