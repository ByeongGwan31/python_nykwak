# 6.3 - n1, n2, n3 라는 이름의 매개변수를 3개 입력 받아 이 값 중에서, 
# 가장 큰 값을 반환하는 max(n1, n2, n3) 함수와 가장 작은 값을 반환하는 mim(n1, n2, n3) 함수를 구현하시오. 

# def max_val(n1, n2, n3):
#     return max(n1, max(n2, n3))

# def min_val(n1, n2, n3):
#     return min(n1, min(n2, n3))

# input_numbers = input("3 수를 입력하시오 : ")
# n1, n2, n3 = map(int, input_numbers.split())

# print("가장 큰 수 : ", max_val(n1, n2, n3))
# print("가장 작은 수 : ", min_val(n1, n2, n3))

# 6.4 - 섭씨온도를(celsius)를 화씨온도(fahrenheit)로 변환하는 식은 다음과 같다.
# fahrenheit = (9/5) * cel + 32

# def cel2fah(temp):
#     return (9/5) * temp + 32

# for cel in range(0, 51, 10):
#     fah = cel2fah(cel)
#     print(f"섭씨{cel}도는 화씨{fah}도 입니다.")


# 6.7 n은 n・(n-1)・(n-2)・・・2・1의 식으로 표현되는 값이다. 
# 양의 정수 n을 매개변수로 받아서 팩토리얼 값을 반환하는 factorial(n) 함수를 구현하여라. 
# 이 함수를 재귀함수를 사용하지 말고, for 문을 사용하여 작성하여라. 
# 이 함수를 이용하여 factorial(5), factorial(7), factorial(10)의 값을 출력하는 출력문을 구현하여라. 

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# print(f'factorail(5) : {factorial(5)}')
# print(f'factorail(7) : {factorial(7)}')
# print(f'factorail(10) : {factorial(10)}')