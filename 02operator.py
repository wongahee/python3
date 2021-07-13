num1 = 10
num2 = 20
num3 = num1 + num2  # 정수 + 정수 = 정수

num1 = 30.5
num2 = 50.5
num3 = num1 + num2 # 실수 + 실수 = 실수

num1 = 10
num2 = 30.5
num3 = num1 + num2 # 정수 + 실수 = 실수

month1 = input('1월 매출을 입력하세요 : ')
month2 = input('2월 매출을 입력하세요 : ')
month3 = input('3월 매출을 입력하세요 : ')

quater1 = int(month1) + int(month2) + int(month3)
print('1분기 전체 매출 : ', quater1)

quater1 = int(month1) + int(month2) + int(month3)
print('1분기 전체 매출 : {0}'.format(quater1))

num1 = 3.14
num2 = 0.25
num3 = num1 + num2
float(num3)
int(num3)

# 총매출 구하기
sales = input('1분기 매출액을 입력하세요 : ')
purchase = input('1분기 매입액을 입력하세요 : ')
profit = int(sales) - int(purchase)

print('1분기 총수익은 ', profit)
print('1분기 총수익은 {0} 원'.format(profit))

# 방 너비 구하기
width = input('방 가로길이는? ')
height = input('방 세로길이는? ')
room = int(width) * int(height)

print('방 넓이는', room ,'㎠ 입니다.')
print('방 넓이는 {0}㎠ 입니다.'.format(room))

str1 = 'Hello, world!!'
str1 * 3
3 * str1
3 * str1 * 2
str1 * -1
# str1 * 0.1 실수는 오류발생

# BMI 구하기
# < 18.5 : 저체중
# < 23 : 정상
# < 25 : 평균
# < 30 : 비만
# > 30 : 고도비만
weight = int(input('몸무게를 입력하세요 : '))
height = int(input('키를 입력하세요 : '))

height = height / 100

BMI = weight / (height * height)
# print('신체질량지수(BMI)는 {0}'.format(BMI))
print('신체질량지수(BMI)는 {0:.2f}'.format(BMI))
print(f'신체질량지수(BMI)는 {BMI:.2f}')   # f-string : py 3.6부터 지원

# print 출력속도
# .format < % < f-string

#'hello' / 2 -> 문자계산 오류발생

# 동전개수 알아보기
coin = int(input('손 안에 동전 수를 입력하세요.'))
even = '0, 짝수입니다' # 짝수일때
odd = '1, 홀수입니다'  # 홀수일때

if coin % 2 == 0 : print(even)
else : print(odd)

# -----------------------
even = coin % 2
print(f'동전의 홀짝여부 (0:짝) {even}')

10 / 3
10 // 3

# 빵 배분
bread = int(input('빵의 전체개수를 입력하세요 : '))
num = int(input('나눌 빵의 개수를 입력하세요 : '))

std = bread // num
divmod = bread % num
print(f'{bread}개의 빵은 {num}개씩')
print(f'나눠먹을 사람 수 : {std}, 나머지 빵의 개수는 : {divmod}')

# 전염병 예상 감염자 수 구하기
day = int(input('며칠 뒤 감염자 예상 수를 구할까요? '))
result = 2 ** day
print(f'{result}명의 감염자가 예상됩니다.')

# 복리 계산기 만들기
# 원금, 유치기간, 연이율을 입력받아 복리계산 후 총수령액 출력
# 1년차 : 원금 * 이율
# 2년차 : 1년차원금 * 이율
# ...
# n년차 : (n-1)년차 원금 * 이율
money = 5_000_000
duration = 5
interest = 5.0

takes = money + (money * 0.05) # 1년차 : 원금 + 이자
takes = takes + (takes * 0.05) # 2년차
takes = takes + (takes * 0.05) # 3년차
takes = takes + (takes * 0.05) # 4년차
takes = takes + (takes * 0.05) # 5년차
# takes += takes * 0.05 와 같음

# 범퍼카 탑승 가능 여부
height = int(input('어린이의 신장을 입력하세요.'))
isRide = height > 120

print(f'탑승 가능여부 : {isRide}(True: 탑승가능)')

'a' == 'b'
'a' > 'b'   # 아스키코드로 변환 후 비교

# 범퍼카 탑승 가능 여부
height = int(input('어린이의 신장을 입력하세요.'))
#isRide = height >= 120 and height < 170
isRide = 120 <= height < 170
print(f'탑승 가능여부 : {isRide}(True: 탑승가능)')

temp = input('온도를 입력하세요')
temp < 16 or temp > 28

# short circuit evaluation
num1 = 17
num2 = 20
(num1 < 15) and (num2 > 15)    # False and True

num1 = 10
num2 = 20
(num1 < 15) or (num2 > 15)    # True

(num1 < 5) and xyz      # py38만 지원

# 삼항 연산자
# 참일때 값 if 조건식 else 거짓일때값
num = 10
'짝수' if (num % 2 == 0) else '홀수'

# 적자/흑자 판단하기
income = int(input('수입은?'))
expense = int(input('지출은?'))
result = '흑자' if(income > expense) else '적자'
print(result)

# 윤년 여부 알아보기
# 4로 나눠떨어지고 100으로 나눠떨어지지 않음
# 400으로 나눠떨어짐
year = int(input('년도는?'))
isLeap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
result = '윤년' if(isLeap) else '평년'
print(result)

# operator 모듈을 이용하면 대량의 데이터 처리 시 속도향상이 존재함
import operator as op

op.add(10, 20)
op.sub(10, 20)
op.mul(10, 20)       # 곱
op.floordiv(10, 20)  # 정수 몫 : //
op.truediv(10, 20)   # 실수 몫 : /
op.mod(10, 3)        # 나머지
op.pow(2, 30)         # 2 * 2 ...* 2 (30번), 2 **30

op.eq(10, 20)
op.ne(10, 20)
op.gt(10, 20)        # 10 greater than 20
op.lt(10, 20)
op.ge(10, 20)
op.le(10, 20)

x = op.eq(10, 20)
y = op.gt(10, 20)
op.and_(x, y)
op.or_(x, y)

# 긴급재난지원금 대상자 판별하기
incomes = input('월소득을 입력하세요')
another = input('다른 지원금을 받고 있습니까? 1번 받고있다. 2번 받고 있지 않다.')

a = op.le(incomes <= 4_000_000)
b = op.eq(2, another)
isTarget = op.and_(a, b)

result = '수급대상자 'if(isTarget) else '긴급 재난지원금 수급대상자가 아닙니다.'
print(result)
