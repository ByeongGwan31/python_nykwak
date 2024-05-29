# 11.4 - numpy의 난수생성기를 이용하여 각각 1000개의 난수를 가지는 3가지 종류의 (x, y) 분포를 생성하고 matplotlib의 산포도 그래프로 나타내어라. 

# import numpy as np
# import matplotlib.pyplot as plt
# np.random.seed(0)

# x1 = np.random.normal(25, 6, 1000)
# y1 = np.random.normal(25, 6, 1000)

# x2 = np.random.normal(25, 6, 1000)
# y2 = np.random.normal(25, 3, 1000)

# x3 = np.random.normal(25, 6, 1000)
# y3 = x3 + np.random.normal(0, 1, 1000)

# fig, axs = plt.subplots(1, 3, figsize = (15, 5))

# axs[0].scatter(x1, y1, color = 'blue')
# axs[1].scatter(x2, y2, color = 'red')
# axs[2].scatter(x3, y3, color = 'green')

# for ax in axs :
#     ax.set_xlim(0, 50)
#     ax.set_ylim(0, 50)

# plt.tight_layout()
# plt.show()

# 11.5 - 다음은 동민이네 동물병원에 치료를 받은 개의 종류와 그 크기 데이터이다. 몸통 길이와 높이는 다음과 같이 cm 단위로 기록하였다.
# import matplotlib.pyplot as plt

# dacs_length = [77, 78, 85, 83, 73, 77, 73, 80]
# dacs_height = [25, 28, 29, 30, 21, 22, 17, 35]

# samo_length = [75, 77, 86, 86, 79, 83, 83, 88]
# samo_height = [56, 57, 50, 53, 60, 53, 49, 61]

# malt_length = [34, 38, 38, 41, 30, 37, 41, 35]
# malt_heigth = [22, 25, 19, 30, 21, 24, 28, 18]

# figure, axes = plt.subplots(1, 3, figsize=(15, 5))

# axes[0].scatter(dacs_length, dacs_height, color = 'red', marker = 'o')
# axes[0].set_title('Dachshund size')
# axes[0].set_xlabel('Length')
# axes[0].set_ylabel('Height')

# axes[1].scatter(samo_length, samo_height, color = 'blue', marker = 's')
# axes[1].set_title('Samoyed size')
# axes[1].set_xlabel('Length')
# axes[1].set_ylabel('Height')

# axes[2].scatter(malt_length, malt_heigth, color = 'green', marker = '^')
# axes[2].set_title('Maltese size')
# axes[2].set_xlabel('Length')
# axes[2].set_ylabel('Height')

# plt.tight_layout()
# plt.show()

# 11.5 - 2.  세 종류의 개들이 한 화면에 나타나도록 하여라. 이때 다음과 같이 범례가 함께 나타나도록 하여라.

# import matplotlib.pyplot as plt

# dacs_length = [77, 78, 85, 83, 73, 77, 73, 80]
# dacs_height = [25, 28, 29, 30, 21, 22, 17, 35]

# samo_length = [75, 77, 86, 86, 79, 83, 83, 88]
# samo_height = [56, 57, 50, 53, 60, 53, 49, 61]

# malt_length = [34, 38, 38, 41, 30, 37, 41, 35]
# malt_heigth = [22, 25, 19, 30, 21, 24, 28, 18]

# plt.figure(figsize = (10, 8))

# plt.scatter(dacs_length, dacs_height, color = 'red', marker = 'o', label='Dachshund')
# plt.scatter(samo_length, samo_height, color = 'blue', marker = '^', label = 'Samoyed')
# plt.scatter(malt_length, malt_heigth, color = 'green', marker = 's', label = 'Matlese')

# plt.title('Dog size')
# plt.xlabel('Length')
# plt.ylabel('Height')

# plt.legend()

# plt.show()

# # 12.1

# import pandas as pd
# df = pd.read_csv('13주차/weather.csv', encoding='euc-kr')

# print(df.head(3).to_string(index = False))
# print(df.tail(3).to_string(index = False))

# 12. 2 - 2015년 6월 6일의 울릉도 평균 기온과 풍속 정보를 다음과 같이 확인하라.

# import pandas as pd

# df = pd.read_csv("13주차/weather.csv", encoding = 'euc-kr')

# df['일시'] = pd.to_datetime(df['일시'])
# df.set_index('일시', inplace = True)
# date150606 = df.loc['2015-06-06']
# print(date150606)

# 12.3 - 이 데이터에 기록된 날들 중에서 가장 무더웠던 날의 평균 기온은 얼마였는지 찾아보라. (weather['평균기온'].max() 활용)

# import pandas as pd

# weather = pd.read_csv('13주차/weather.csv', encoding = 'euc-kr')

# weather['일시'] = pd.to_datetime(weather['일시'])
# weather.set_index('일시', inplace = True)

# max_temp = weather['평균기온'].max()
# print(max_temp)

# 12.4 - 가장 무더웠던 날이 언제이고, 이 날의 평균 기온, 평균 풍속, 최대 풍속을 알아보라

# import pandas as pd
# weather = pd.read_csv('13주차/weather.csv', encoding = 'euc-kr')

# weather['일시'] = pd.to_datetime(weather['일시'])
# weather.set_index('일시', inplace = True)

# max_temp = weather[weather['평균기온'].max() == weather['평균기온']]

# print(max_temp)

# 12.5 - 울릉도의 평균기온 30도를 넘는 날들을 찾아, 이 날의 기상 데이터를 나열하기

import pandas as pd
weather = pd.read_csv('13주차/weather.csv', encoding = 'euc-kr')

weather['일시'] = pd.to_datetime(weather['일시'])
weather.set_index('일시', inplace = True)

avg30 = weather[weather['평균기온'] > 30]

print(avg30)
