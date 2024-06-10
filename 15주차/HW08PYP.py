#1. 자동차의 연비에 영향을 미치는 요소 -> 선형 회귀 모델 구하기.abs

# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score

# data = {
#     '마력': [130, 250, 190, 300, 210, 220, 170],
#     '총중량': [1900, 2600, 2200, 2900, 2400, 2300, 2100],
#     '연비': [16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2]
# }

# df = pd.DataFrame(data)

# X = df[['마력', '총중량']]
# y = df['연비']

# model = LinearRegression()
# model.fit(X, y)

# coefficients = model.coef_
# intercept = model.intercept_

# y_pred = model.predict(X)
# r2 = r2_score(y, y_pred)

# print("계수 :", coefficients)
# print("절편 : ", intercept)
# print("예측 점수 : ", r2)

# 1-2. 
# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score

# data = {
#     '마력': [130, 250, 190, 300, 210, 220, 170],
#     '총중량': [1900, 2600, 2200, 2900, 2400, 2300, 2100],
#     '연비': [16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2]
# }

# df = pd.DataFrame(data)

# X = df[['마력', '총중량']]
# y = df['연비']

# model = LinearRegression()
# model.fit(X, y)

# coefficients = model.coef_
# intercept = model.intercept_

# new_data = np.array([[270, 2500]])
# predicted_fuel_efficiency = model.predict(new_data)[0]

# print(f"270 마력 2500kg 자동차의 예상 연비 : {predicted_fuel_efficiency:.2f} km/l")

# 1-3. 쌍플롯 그래프
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# data = {
#     'horse_power': [130, 250, 190, 300, 210, 220, 170],
#     'weight': [1900, 2600, 2200, 2900, 2400, 2300, 2100],
#     'efficiency': [16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2]
# }

# df = pd.DataFrame(data)

# sns.set(style = 'whitegrid')
# sns.pairplot(df)
# plt.show()

# 1-4. 히트맵 그래프
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# data = {
#     'horse_power': [130, 250, 190, 300, 210, 220, 170],
#     'weight': [1900, 2600, 2200, 2900, 2400, 2300, 2100],
#     'efficiency': [16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2]
# }

# df = pd.DataFrame(data)

# corr_matrix = df.corr()
# plt.figure(figsize = (8, 6))
# sns.heatmap(corr_matrix, annot = True, cmap = 'rocket', vmin = -1, vmax = 1)
# plt.show()

# 14.3 닥스훈트 

# import numpy as np

# data = np.array([
#     [77, 25], [78, 28], [85, 29], [83, 30], [73, 21], [77, 22], [73, 17], [80, 35],
#     [75, 56], [77, 57], [86, 50], [86, 53], [79, 60], [83, 53], [83, 49], [88, 61],
#     [34, 22], [38, 25], [38, 19], [41, 30], [30, 21], [37, 24], [41, 28], [35, 18]
# ])

# labels = np.array([
#     0, 0, 0, 0, 0, 0, 0, 0,
#     1, 1, 1, 1, 1, 1, 1, 1,
#     2, 2, 2, 2, 2, 2, 2, 2
# ])

# print("Data:", data)
# print("Labels:", labels)


# 14.3 2)
# import numpy as np
# from sklearn.neighbors import KNeighborsClassifier

# data = np.array([
#     [77, 25], [78, 28], [85, 29], [83, 30], [73, 21], [77, 22], [73, 17], [80, 35],
#     [75, 56], [77, 57], [86, 50], [86, 53], [79, 60], [83, 53], [83, 49], [88, 61],
#     [34, 22], [38, 25], [38, 19], [41, 30], [30, 21], [37, 24], [41, 28], [35, 18]
# ])

# labels = np.array([
#     0, 0, 0, 0, 0, 0, 0, 0,
#     1, 1, 1, 1, 1, 1, 1, 1,
#     2, 2, 2, 2, 2, 2, 2, 2
# ])

# new_data = np.array([
#     [45, 34],
#     [70, 59],
#     [49, 30],
#     [60, 56]
# ])

# knn = KNeighborsClassifier(n_neighbors=3)
# knn.fit(data, labels)
# predictions = knn.predict(new_data)

# print(f"A : 길이 {new_data[0][0]}, 높이 {new_data[0][1]} -> 클래스 {predictions[0]}")
# print(f"B : 길이 {new_data[1][0]}, 높이 {new_data[1][1]} -> 클래스 {predictions[1]}")
# print(f"C : 길이 {new_data[2][0]}, 높이 {new_data[2][1]} -> 클래스 {predictions[2]}")
# print(f"D : 길이 {new_data[3][0]}, 높이 {new_data[3][1]} -> 클래스 {predictions[3]}")

# 14.3 3) 산점도 나타내기
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = 'C:/Windows/Fonts/malgun.ttf'
fontprop = fm.FontProperties(fname = font_path, size = 12)
plt.rc('font', family = fontprop.get_name())

data = np.array([
    [77, 25], [78, 28], [85, 29], [83, 30], [73, 21], [77, 22], [73, 17], [80, 35],
    [75, 56], [77, 57], [86, 50], [86, 53], [79, 60], [83, 53], [83, 49], [88, 61],
    [34, 22], [38, 25], [38, 19], [41, 30], [30, 21], [37, 24], [41, 28], [35, 18]
])

labels = np.array([
    0, 0, 0, 0, 0, 0, 0, 0,  
    1, 1, 1, 1, 1, 1, 1, 1,
    2, 2, 2, 2, 2, 2, 2, 2 
])

new_data = np.array([
    [45, 34],
    [70, 59],
    [49, 30],
    [60, 56]
])

knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(data, labels)
predictions = knn.predict(new_data)

plt.figure(figsize=(10, 8))

colors = ['red', 'blue', 'green']
labels_names = ['닥스훈트', '사모예드', '말티즈']
for i in range(3):
    plt.scatter(data[labels == i][:, 0], data[labels == i][:, 1], c=colors[i], label = labels_names[i], edgecolor = 'k')

markers = ['o', 's', 'D', '^']
for i, point in enumerate(new_data):
    plt.scatter(point[0], point[1], c = 'none', edgecolor = 'k', s=100, marker = markers[i], label = f'새로운 포인트 {chr(65+i)}')

plt.xlabel('Length')
plt.ylabel('Height')
plt.title('개의 종류와 크기 산점도')
plt.legend()
plt.grid(True)
plt.show()

