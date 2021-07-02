#  24줄
import keyword

myName = '길동'
myMajor = '데이터분석'

print(myName)
print(myMajor)

myName = 100
myName = True
myName = False
myName = 3.141519

intro = 'Hello'
print(intro)

intro = '안녕하세요.'
print(intro)

nickname = 'Ms.Won'
nickname #콘솔에서만 출력

# 변수명규칙 - 예약어 사용불가
# print(keyword.kwlist)
# print(keyword.softkwlist)  # v3.9 추가

# //3

bigint = 1234567801212345678012123456780121234567801212123456780121212345678012
print(bigint)

bigfloat = 1.234567801234567890
print(bigfloat)

a = 123
b = '456'
a = a + 1
# b = b + 1 오류발생

# 자료형 조회
print(type('안녕하세요'))
print(type(123))
print(type(True))

print(type(myName))

# 다중 선언
x = 1
y = 1
z = 1

x = y = z = 10

# 자릿수 구분
million = 1000000
million = 1_000_000 # ,대신 _로 자릿수 구분
# num = 1_2_3 # 콘솔에 그냥 123으로 찍힘

# 논리값 확인 : bool - 0빼고 모든 수 true
bool(True)
bool(1)
bool(100)
bool(-100)
bool(0)

str(123)
int('456')
float('3.14')

# input() 함수
# name = input('이름을 입력하세요 : \n')
# print(name)

# 성적처리프로그램
# 이름,국어,영어,수학을 입력받아 출력하는 프로그램을 작성하세요.
name = input('이름을 입력하세요 : ')
kor = input('국어 점수를 입력하세요 : ')
eng = input('영어 점수를 입력하세요 : ')
mat = input('수학 점수를 입력하세요 : ')
tot= int(kor)+int(eng)+int(mat)
print(name, tot)
