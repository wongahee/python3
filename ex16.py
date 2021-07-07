# 수학시험 프로그램
quiz = ['3+2', '5%2의 몫', '10-2', '10²x2', '1-(10%4의 나머지)', '2⁴', '4%2']
answer = [5, 2, 8, 200, -1, 16, 2]
point = [3, 5, 3, 5, 5, 3, 3]

# asw = []    # 사용자가 입력한 정답
#
# cnt = len(quiz)
# for i in range(cnt):
#     print(f'문제 {i+1} {quiz[i]}')
#     asw.append(input(f'정답을 입력하세요.'))
#
# good = 0
# jumsu = 0
# for i in range(cnt):
#     if int(asw) == answer[i]:
#         good += 1
#         jumsu += point[i]   # 점수변수에 point리스트에 해당하는 인덱스값 넣음
#
# asw = []    # 사용자가 입력한 정답
# cnt = len(quiz)
# good = 0
# jumsu = 0
#
# for i in range(cnt):
#     print(f'문제 {i+1}) {quiz[i]}의 값을 계산하시오.')
#     asw.append(input(f'정답을 입력하세요. '))
#
#     if int(asw) == answer[i]:
#         good += 1
#         jumsu += point[i]   # 점수변수에 point리스트에 해당하는 인덱스값 넣음
#
# print('-'*30)
# print(f'정답 개수 : {good}개 \n'
#       f'오답 개수 : {cnt - good}개 \n'
#       f'총 점수 : {jumsu}점')
# print('-'*30)

# 풀이2
quiz = [['3+2', 5, 3], ['5%2의 몫', 2, 5], ['10-2', 8, 3], ['10²x2', 200, 5],
        ['1-(10%4의 나머지)', -1, 5], ['2⁴', 16, 3], ['4%2', 2, 3]]
cnt = len(quiz)
good = 0
jumsu = 0

for q in quiz:
    print(f'{q[0]}의 값을 계산하시오.')
    asw = input(f'정답을 입력하세요. ')

    if int(asw) == q[1]:
        good += 1
        jumsu += q[2]
print('-'*30)
print(f'정답 개수 : {good}개 \n'
      f'오답 개수 : {cnt - good}개 \n'
      f'총 점수 : {jumsu}점')
print('-'*30)
