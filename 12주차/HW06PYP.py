# 10.3 -1) 다음과 같은 난수로 이루어진 3x3x3 형태의 배열 a를 생성하기

# import numpy as np
# a = np.random.rand(3, 3, 3)

# print(a)

# 10.3 -2 ) a배열에 가장 큰 값을 구하여 다음과 같이 출력하라. max()사용

# import numpy as np
# a = np.random.rand(3, 3, 3)

# max_value = a.max()
# print(f"a의 원소들 중 최댓값 : {max_value}")

# 10.3 -3 ) a배열에서 가장 큰 값이 몇 번째 있는지 구하여 출력하기 ndarray에서 제공하는 argmax() 함수 제공
# import numpy as np
# a = np.random.rand(3, 3, 3)

# max_index = a.argmax()
# print(f"a의 원소들 중 최댓값의 위치 : {max_index}")


# 10.4 1) 넘파이의 인덱싱 기능을 활용하여 5*5 크기의 행렬 생성하기 0과 1로 이루어지고 체크판 형태

# import numpy as np
# a = np.zeros((5, 5), dtype = int)

# a[::2, ::2] = 1 
# a[1::2, 1::2] = 1
# print(a)

# 10.4 2) 행방향 성분의 합
# import numpy as np
# a = np.zeros((5, 5), dtype = int)

# a[::2, ::2] = 1 
# a[1::2, 1::2] = 1

# row_sums = a.sum(axis = 1)

# print("행렬의 행 방향 성분의 합 :")
# print(row_sums)


# 10.6 ) 4개의 데이터 리스트 -> 상관관게를 구하여 표로 나타내기

import numpy as np
import pandas as pd

x1 = [ i for i in range(100) ]
x2 = [ i + np.random.randint(1, 10) for i in range(100) ]
x3 = [ i + np.random.randint(1, 50) for i in range(100) ]
x4 = [ np.random.randint(1, 100) for i in range(100) ]

data = pd.DataFrame({
    'x1': x1,
    'x2': x2,
    'x3': x3,
    'x4': x4
})

correlation_matrix = data.corr()
print(correlation_matrix.to_numpy())
