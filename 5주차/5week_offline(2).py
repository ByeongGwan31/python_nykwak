sex = int(input('여성이면 1, 남성이면 0을 입력하시오 : '))
height = int(input('당신의 키는 얼마입니까? : '))
round = int(input('당신의 허리 둘레는 얼마입니까? : '))

rfm = 64 - (20 * (height / round) ) + 12 * sex

print(f'당신의 rfm은 {rfm}입니다.')