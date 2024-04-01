Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> bottom = float(input('직각삼각형의 변의 길이를 입력하시오 : '))
직각삼각형의 변의 길이를 입력하시오 : 3
>>> height = float(input('직각삼각형의 높이를 입력하시오 : '))
직각삼각형의 높이를 입력하시오 : 4
>>> hypotenuse = (botoon ** 2 + height ** 2) ** 0.5
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    hypotenuse = (botoon ** 2 + height ** 2) ** 0.5
NameError: name 'botoon' is not defined. Did you mean: 'bottom'?
>>> hypotenuse = (botton ** 2 + height ** 2) ** 0.5
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    hypotenuse = (botton ** 2 + height ** 2) ** 0.5
NameError: name 'botton' is not defined. Did you mean: 'bottom'?
>>> hypotenuse = (bottom ** 2 + height ** 2) ** 0.5
>>> print(f'빗변은 {hypotenuse} 입니다.')
빗변은 5.0 입니다.
