# 도전 문제 9.1

# t = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic\
# Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 (LG \
# U+ Mystic Pink 30%, SKT Mystic BLue not disclose)'

# low_t = t.lower()
# t =''


# for word in low_t.split(' '):
#     if word == 'kt' or word == 'samsung' or word == 'lg' or word == 'skt':
#         t += '* '
#     else:
#         t += word +''

# print(t)

# lab 9_2

# t = "There's a reason some people are working to make it harder to vote, especially for people of color. It’s because when we show up, things change."

# length = len(t.split(' '))
# print('word count:', length)

# 도전문제 9.2
# t = "It's Not The Right Time To Conduct Exams. MY DEMAND IN BOLD AND CAPITAL. NO EXAMS IN COVID!!!"

# count = 0

# print('느낌표 개수 :', t.count('!'))
# for ch in t:
#     if ch.isupper():
#         count += 1
# print('대문자 개수 :', count)


# 기말고사 예제문제
# import random
# import string

# src_str = string.ascii_letters + '0123456789'

# n_digits = int(input('몇 자리의 비밀번호를 원하십니까? : '))

# otp = ''
# for i in range(n_digits) :
#     idx = random.randrange(len(src_str))
#     otp += src_str[idx]

# print(otp)


# 9.7 정보를 한눈에 보여주는 워드 클라우드, 233쪽
# 이거를 하려면 인터프리터에서 3.10 버전으로 venv 한다음 실행해야 함.

import wikipedia
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# 위키백과 사전의 컨텐츠 제목을 명시해 준다
wiki = wikipedia.page('Python programming language')
# 이 페이지의 텍스트 컨텐츠를 추출하도록 한다
text = wiki.content

# 불용어(stopwords)를 설정하고 워드 클라우드 생성
s_words = STOPWORDS.union({'one', 'using', 'first', 'two', 'make', 'use', 'python'})
wordcloud = WordCloud(width=2000, height=1500, stopwords=s_words).generate(text)

# 워드 클라우드 출력
plt.figure(figsize=(40, 30))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# 9.10 정규식을 활용해서 멋지게 검색을 하자.

# import re

# f = open('C:\\Users\\bk200\\ByeongGwan Kang\\python_nykwak\\python_nykwak\\11주차\\UNDHR.txt')

# for line in f:
#     ine = line.rstrip()
#     if re.search('^\([0-9]+\)', line):
#         print(line)


# LAB 9-5

import re
text = '''101 COM PythonPrograming
102 MAT LinearAlgebra
103 ENG ComputerEnglish'''

s = re.findall('\d+', text)
print(s)

# 도전문제 9.5_1

import re

# 멀티라인 텍스트는 세 개의 따옴표를 사용하여 표현한다
text = '''101 COM PythonProgramming1
102 MAT LinearAlgebra
103 ENG ComputerEnglish'''

# Python Part1과 같이 숫자가 표함된 문자가 있을 경우
# 알파벳 문자나 줄바꿈문자(\n)이 아닌 순수하게 숫자로만 이루어진 단어를 추출하는 정규식
s = re.findall('[^a-zA-Z\\n]\d+', text)
print(s)

# 수강 코드가 반드시 세자리 정수일 경우 다음과 같은 방법도 가능함
s = re.findall('\d{3}', text)
print(s)




