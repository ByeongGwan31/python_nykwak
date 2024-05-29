# LAB 11-1 수학 함수도 쉽게 그려보자, 286쪽
# import matplotlib.pyplot as plt
# import numpy as np

# np.random.seed(0)

# x = [x for x in range(1000)]
# y = np.random.rand(1000) * 3

# plt.title("Numbers")
# plt.plot(x, y, marker='o')

# plt.show()

# 도전문제 11-2 (Lab 11-2)

# import matplotlib.pyplot as plt

# x = [x / 10 for x in range(20)]
# y = [(x / 10) ** 2 for x in range(20)]
# z = [(x / 10) ** 3 for x in range(20)]
# i = [2 ** (x / 10) for x in range(20)]

# plt.plot(x, x, label = 'linear')
# plt.plot(x, y, label = 'quadratic')
# plt.plot(x, z, label = 'qubic')
# plt.plot(x, i, label = 'power')

# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title("My Plot")
# plt.legend()
# plt.show()

# # 11.7 막대형 차트도 손쉽게 그려보자, 290쪽
# from matplotlib import pyplot as plt 

# # 한글 지원하는 라이브러리 추가 
# from matplotlib import font_manager, rc 
# font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name() 
# rc('font', family=font_name) 

# # 차트 축 <- 음수 부호 지원 
# import matplotlib 
# matplotlib.rcParams['axes.unicode_minus'] = False 

 
# # 1인당 국민소득 
# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010] 
# gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 22105.3] 
 
# plt.bar(range(len(years)), gdp) 
 
# plt.title("GDP per capita")   # 제목을 설정한다. 
# plt.ylabel("dollars")         # y축에 레이블를 붙인다. 
 
# # y축에 틱을 붙인다. 
# plt.xticks(range(len(years)), years) 
# plt.show()

# 11.10 맛있는 피자가 생각나는 파이 차트, 293쪽
#
import matplotlib.pyplot as plt 
# 한글 지원하는 라이브러리 추가 
from matplotlib import font_manager, rc 
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name() 
rc('font', family=font_name) 

# 차트 축 <- 음수 부호 지원 
import matplotlib 
matplotlib.rcParams['axes.unicode_minus'] = False 

times = [8, 14, 2]
timelabels = ["Sleep", "Study", "Play"]

# autopct로 백분율을 표시할 때 소수점 2번째 자리까지 표시하게 한다.
# labels 매개 변수에 timelabels 리스트를 전달한다.
plt.pie(times, labels = timelabels, autopct = "%.2f") 
plt.show()