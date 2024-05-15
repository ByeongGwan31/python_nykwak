# 9.3 다음과 같이 대문자와 소문자, 특수문자, 숫자로 이루어진 문자열이 입력되면, 각각의 출현 횟수를 출력하는 코드를 작성하여라.

# input_string = input("문자열을 입력하시오: ")

# upper_case_count = 0
# lower_case_count = 0
# digit_count = 0
# special_char_count = 0


# for char in input_string:
#     if char.isupper(): # 대문자
#         upper_case_count += 1
#     elif char.islower(): #소문자
#         lower_case_count += 1
#     elif char.isdigit(): #숫자
#         digit_count += 1
#     else:
#         special_char_count += 1

# print("대문자, 소문자, 숫자, 특수문자의 개수")
# print(f"대문자 = {upper_case_count}")
# print(f"소문자 = {lower_case_count}")
# print(f"숫자 = {digit_count}")
# print(f"특수문자 = {special_char_count}")

# 9.4 다음과 같이 문자열 s가 있다. 이 문자열에는 Korea가 몇 번 나타나는가를 조사하여 출력하라. 
# 이때 KOREA, Korea와 korea는 같은 문자열로 간주한다.

# s = 'Korea is awesome! I REALLY LOVE KOREA.'

# s_lower = s.lower()
# word_length = len('korea')

# korea_count = 0

# for i in range(len(s_lower) - word_length + 1):
#     if s_lower[i:i+word_length] == 'korea':
#         korea_count += 1

# print(f"Korea의 출현 횟수 : {korea_count}")

# 9-8 사용자로부터 문장 입력받기
# import re

# input_string = input("문장을 입력하시오: ")

# alphabet = r'\b[a-zA-Z]+\b'
# number = r'\b\d+\b'
# alpha_number = r'\b(?=\w*\d)(?=\w*[a-zA-Z])[\w]+\b'

# english_words = re.findall(alphabet, input_string)
# number_words = re.findall(number, input_string)
# alphanumeric_words = re.findall(alpha_number, input_string)

# alphanumeric_words = [word for word in alphanumeric_words if not (word in english_words or word in number_words)]

# print(f"영문 단어: {' '.join(english_words)}")
# print(f"숫자: {' '.join(number_words)}")
# print(f"영문자+숫자: {' '.join(alphanumeric_words)}")


# 9.9 위키 백과사전 입력하기

import wikipedia
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

wiki = wikipedia.page('South Korea')
text = wiki.content

s_words = STOPWORDS.union({'south', 'north', 'korean', 'world', 'country'})
wordcloud = WordCloud(width=2000, height=1500, stopwords=s_words, background_color='black').generate(text)

plt.figure(figsize=(10, 8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()






