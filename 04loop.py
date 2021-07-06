# 반복문 loop
# 1 ~ 10까지 정수 출력
for i in range(1,10+1):
    print(i)

# 2 ~ 10까지 짝수 출력
for i in range(1, 6):
    print(i*2)

for i in range(2, 10+1, 2):
    #print(i)
    print(i, end=' ')

for i in range(1, 10+1):
    if i % 2 == 0: print(i)

# 사용자가 입력한 횟수만큼 '메일발송!' 문자열 출력하기
mail = int(input('메일 발송 횟수를 입력하세요. '))
msg = '메일 발송!'

for i in range(1, mail+1):
    print(msg)

# 1~10사이의 정수를 출력하되, 정수가 3의 배수이면 '3의 배수!'출력하기
for i in range(1, 10+1):
    if i % 3 == 0:
        print(f'num = {i}')
        print('3의 배수!')
    else:
        print(f'num = {i}')

# 구구단 5단 출력하기
for i in range(1, 9+1):
    print(f'5 * {i} = {5*i}')

# -----슨생님 풀이-------
dan = int(input('단을 하나 입력하세요(1-9)'))
for i in range(1, 9+1):
    print(f'{dan} x {i} = {dan * i}')

# 1~10까지 정수의 합 출력하기
sum = 0
for i in range(1, 10+1):
    sum += i
print(sum)

# for문을 이용해서 1~100까지 정수 중에서 3과 7의 공배수, 최소공배수를 출력하시오.
for i in range(1, 100+1):
    if i % 3 == 0 and i % 7 == 0:
        print(i)

min = 100
for i in range(100, 1, -1):
    if i % 3 == 0 and i % 7 == 0:
        if min >= i: min = i
        print(i, end=' ')
print(f'최소공배수 : {min}')

# -10 ~ 0 까지 1씩 증가하는 숫자들
for i in range(-10, 0+1, 1):
    print(i, end=' ')

# 1 ~ 10 까지 출력
for i in range(10):  # 0 ~ 9
    print(i + 1)     # 1 ~ 10

# 반복문에 range 대신 문자열 사용
for ch in 'Hello':
    print(ch, end=',')
print()

# 50보다 작은 7의 배수를 출력하는 프로그램을 만드시오.
for i in range(7, 50+1, 7):
    print(i)

for i in range(50):
    if i % 7 == 0:
        print(i, end=',')
print()

# 1~ 10까지 출력
num = 1
while num < 10+1:
    print(num)
    num += 1

# 1 ~ 30까지 정수 중 홀수와 짝수를 구분하여 출력하기
num = 1
while num < 30+1:
        print(f'홀수 : {num}')
        print(f'짝수 : {num}')
        num += 1

# -------선생님 풀이---------
num = 1
while num <= 30:
    if num % 2 == 0:
        print(f'짝수 : {num}')
    else:
        print(f'홀수 : {num}')
    num += 1

# 구구단 3단 출력하기
num = 1
dan = 3
while num < 9+1:
    print(f'{dan} * {num} = {dan * num}')
    num += 1

# 0 ~ 100까지 정수 중 3과 8의 공배수와 최소공배수 출력하기
num = 1
min = 100
while num < 100+1:
    if num % 3 == 0 and num % 8 == 0:
        print(f'공배수 : {num}')
        if min > num: min = num
    num += 1
print(f'최소공배수 : {min}')

# 게임 진행과 종료
flag = True
while flag:
    code = int(input('1:진행, 2:종료 '))
    if code == 1: print('게임 진행')
    else :
        flag = False
        print('게임 종료')

# 1 ~ 50까지 정수 중 3의 배수 더하기
sum = 0
for i in range(1, 50+1):
    if i % 3 != 0: continue
    sum += i
print(sum)

# 1 ~ 100까지 모든 정수 더하기
# 단, 정수의 합이 500이 넘었을때의 정수는 무엇인가?
sum = 0
for i in range(1, 100+1):
    sum += i
    if sum >= 500:
        print(i)
        break
print(sum, i)

# 1 ~ 10까지 정수의 총합을 구하고 반복이 끝나는 경우 완료메세지 출력
sum = 0
for i in range(1, 10+1):
    sum += i
else:
    print(f'총합 계산 끝! : {sum}')

# 두번째 풀이
sum = 0
for i in range(1, 10):
    sum += (i + 1)
else:
    print(f'총합 계산 끝! : {sum}')

# 삼각형의 넓이 구하기
width = 2
height = 3
area = 0
while area <= 150:
    area = (width * height) / 2
    print(area, width, height)
    width += 2
    height += 3
print('넓이 구하기 종료!')

# 1 ~ 100까지 정수 중 5 또는 7의 배수를 제외하고 출력
for i in range(1,100):
    if i % 5 == 0 or i % 7 == 0: continue
    print(i, end=',')
print()

# 구구단 출력
for i in range(2, 9+1):
    for j in range(1, 9+1):
        print(f'{j:2d} x {i:2d} = {i * j:2d} \t', end=' ')
    print()   # 1단마다 줄바꿈
# 트리 만들기
for num1 in range(1, 11+1, 2):
    for num2 in range(num1):
        print('*', end='')
    print()
