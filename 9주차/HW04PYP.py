# 7-3 다음과 같이 문자열을 가진 두 개의 리스트 list1, list2가 있을 경우, list1과 list2의 모든 조합을 생성하여 다음과 같이 출력하시오.

# list1 = ['I like', 'I love']
# list2 = ['pancakes.', 'kiwi juice.', 'espresso.']

# comprehension = [f"{section1} {section2}" for section1 in list1 for section2 in list2]

# for x in comprehension:
#     print(x)

# 7-5 (‘A’, ‘B’, ‘C’) 튜플과 (‘1’, ‘2’)을 조합하여 다음과 같은 공연장의 좌석번호를 생성하는 프로그램을 작성하여라. 
# 이때 (‘1’, ‘2’) 대신 정수로 이루어진 튜플 (1, 2)가 있을 경우 동일한 결과가 나타나도록 다시 프로그램을 작성하여라.

# rows = ('A', 'B', 'C')
# cols = (1, 2)

# sets = [f"{row}{col}" for row in rows for col in cols]

# print(sets)

# 7-7 fruit_list = ['banana', 'orange', 'kiwi', 'apple', 'melon'] 에서 가장 길이가 긴 문자열을 찾아 출력하고 이 리스트에서 삭제 할 것.
# 이 때 동일한 길이의 문자열이 있을경우에도 삭제하라.
# 7-1)

# fruit_list = ['banana', 'orange', 'kiwi', 'apple', 'melon']

# max_length = max(len(fruit) for fruit in fruit_list)

# maximum = [fruit for fruit in fruit_list if len(fruit) == max_length]

# print(f"가장 길이가 긴 문자열 : {maximum}")

# fruit_list = [fruit for fruit in fruit_list if len(fruit) != max_length]

# print(f"fruit_list = {fruit_list}")


# 7-2)

# fruit_list = ['banana', 'orange', 'kiwi', 'apple', 'melon']

# for fruit in fruit_list:
#     print(f"{fruit} : 문자열의 길이 {len(fruit)}")

# 8-5

# print("사전 프로그램 시작... 종료는 q를 입력")
# dictionary = {}

# while True:
#     st = input('$ ')
#     command = st[0]

#     if command == "<":
#         st = st[1:]
#         inputStr = st.split(':')
#         if len(inputStr) < 2:
#             print('입력 오류가 발생했습니다.')

#         else:
#             dictionary[inputStr[0].strip()] = inputStr[1].strip()
#     elif command == '>':
#         st = st[1:]
#         inputStr = st.strip()
#         if inputStr in dictionary:
#             print(dictionary[inputStr])
#         else :
#             print('{}가 사전에 없습니다'.format(inputStr))
#     elif command == 'v':
#         print('영어 사전에 있는 단어와 뜻을 출력합니다.')
#         for word, meaning in dictionary.items():
#             print(f"{word} : {meaning}")
#     elif command == 'q':
#         break
#     else :
#         print('입력 오류가 발생했습니다')
# print('사전 프로그램을 종료합니다.')

student_tuple = [
    ('211101', '강이안', '010-123-1111'),
    ('211102', '박동민', '010-123-2222'),
    ('211103', '김수정', '010-123-3333')
]

student_dict = {student[0]: student[1] for student in student_tuple}

for student_id, student_name in student_dict.items():
    print(f'{student_id} : {student_name}')

input_student_id = input("학번을 입력하시오 : ")

for student in student_tuple:
    if student[0] == input_student_id:
        print(f'{student[0]} 학생은 {student[1]}이며, 전화번호는 {student[2]}입니다.')
