# # 함수와 모듈
# # 함수는 일정한 작업을 수행하는 코드집합체
# # 보통 반복적으로 사용되는 코드들을 함수로 정의해서 사용
#
# # 즉, 반복적으로 사용할 가치가 있는 코드를 한 뭉치로 묶고
# # 어떤 입력값을 주면 결과가 반환되도록 사용
#
# # 또한, 여러 코드들을 함수화하면 프로그램의 흐름을
# # 일목요연하게 파악하기 쉬움
#
# # 다른 사람과의 협업시 코드가 섞이지 않게
# # 하기 위한 목적도 있음 - 모듈
#
# def startSensor():
#     print('온도 센서 작동을 시작합니다.')
#
# def stopSensor():
#     print('온도 센서 작동을 중지한다.')
#
# startSensor()
# stopSensor()
#
# # 내 노트북은 몇 인치일까?
# def cm2inch(cm):
#     inch = cm * 0.03937
#     print(f'{cm} cm = {inch:.4f} inch')
#
# cm = int(input('길이를 입력하세요.(cm) '))
# cm2inch(cm)
#
# # 이동 거리를 계산하는 함수
# def movedis(time, speed):
#     print(f'이동 거리는 {time * speed} km 입니다.')
#
# time = float(input('이동 시간을 입력하세요. '))
# speed = float(input('이동 속도를 입력하세요. '))
# movedis(time, speed)
#
# # 추가
# def add():
#     print(a + b)
#
# a = input('a는? ')
# b = input('b는? ')
#
# add()
#
# # 전역변수와 지역변수 (global n local)
# # 지역변수 : 선언된 함수 안에서만 작동
# # 전역변수 : 함수 밖 전역에서 작동
# num = 10
#
# print('전역변수 num', num)       # 10
#
# def local():
#     num = 20
#     print(f'지역변수 num', num)  # 20
#
# local()
# print('전역변수 num', num)       # 10
#
# # 함수 내에서 전역변수 사용하기 : global
# num = 10                       # 10
# print('전역변수 num', num)
#
# def local():                   # 전역변수를 함수 내에서 사용할 수 있도록함
#     global num                 # 선언 시 모든 num변수가 같은 값이 됨
#                                # 함수 내에서 전역변수를 수정할 수 있도록 함
#     num = 20
#     print(f'지역변수 num', num)  # 20
#
# print('전역변수 num', num)       # 10이 아닌 20으로 출력하고 싶을 때
#
# # 웹사이트의 누적 방문 횟수 프로그램
# count = 0
#
# def countVisitor():
#     global count
#     # global count = 0    # 전역변수는 초기화 불가
#
#     while True:
#         menu = input('1.웹사이트 방문, 2.종료 ')
#         if menu == '1':
#             count += 1
#             print(f'누적 방문 횟수 : {count}')
#         elif menu == '2':
#             print(f'누적 방문 횟수 : {count}')
#             break
#         else:
#             print('다시 입력하세요.')
#
# print(f'전체 방문횟수 : {count}')
#
# countVisitor()
#
# x = 10
# y = 10
#
# def add():
#     print(x + y)
#
# add()
# add(10, 10)
#
# # 함수의 매개변수 개수를 동적으로 정의
# # 매개변수명 앞에 *로 정의해서 함수를 만들면 됨
#
# # ex) 기존에 만든 add함수는 2개의 매개변수만 받음
# # 2개 이상의 매개변수를 받아 결과로 출력하고 싶다면?
# def add(x, y, z):
#     print(x + y + z)
#
# def add2(*num):
#     sum = 0
#     for v in num:
#         sum += v
#     print(sum)
#
# add2(10, 10)
# add2(10, 10, 10, 10)
# add2(10, 10, 10, 10, 10, 10, 10)
#
# # SMS와 MMS 구별하기
# def computeMSG(msg):
#     print(f'입력한 문자열 길이 : {len(msg)}')
#
#     if len(msg) > 100:
#         print('장문 메시지로 100원이 부과됩니다.')
#     else:
#         print('단문 메시지로 50원이 부과됩니다.')
#
# msg = input('문자열을 입력하세요. ')
# computeMSG(msg)
#
# # 함수 정의 시 매개변수를 선언했지만
# # 함수 호출 시 인수를 순서대로 입력하지 않을 경우
# # => 인수값 앞에 매개변수명을 지정
#
# def computeSungJuk(name, kor, eng, mat):
#     tot = kor + eng + mat
#     avg = tot / 3
#
#     print(tot, avg)
#
# computeSungJuk('혜교', 98, 78, 85)
# computeSungJuk(98, 78, 85, '수지')    # 잘못된 순서로 오류 발생!!
#
# computeSungJuk(kor=98, eng=78, mat=85, name='수지')
# computeSungJuk(name='수지', kor=98, eng=78, mat=85)
#
# # 매개변수를 정의했지만
# # 매개변수 없이 함수 호출하고 싶다면?
# # -> 매개변수 선언시 초기값을 지정함
#
# def add3(x=10, y=10):
#     print(x + y)
#
# add3()      # 함수에 매개변수 지정해줌
#
# 사칙연산 프로그램 만들기
def calculator(x, y):
    add = x + y
    min = x - y
    mul = x * y
    div = x / y

    return add, min, mul, div

x = int(input('정수를 입력하세요. '))
y = int(input('정수를 입력하세요. '))
p, m, c, d = calculator(x, y)

print(f'사칙연산 결과 : {p}, {m}, {c}, {d:.2f}')
