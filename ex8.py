# 차량 2부제 프로그램
cnum = int(input('차량 번호 4자리를 입력하세요. '))
day = int(input('오늘 날짜 : '))

if day % 2 == 0:
    print(f'오늘 입차 : 번호가 짝수인 차량')
    if cnum % 2 == 0:
        print('귀하의 차량은 입차 가능합니다.')
    else:
        print('귀하의 차량은 입차 불가합니다.')
else:
    print(f'오늘 입차 : 번호가 홀수인 차량')
    if cnum % 2 == 1:
        print('귀하의 차량은 입차 가능합니다.')
    else:
        print('귀하의 차량은 입차 불가합니다.')

# ----선생님풀이--------
from datetime import datetime as dt
dt.now().day
dt.today().day

evenOrodd = '짝수'
if int(day) % 2 != 0: evenOrodd == '홀수'
print(f'오늘 입차 : 번호가 {evenOrodd}인 차량')

passOrNot = '입차 불가'
if int(cnum) % 2 != 0 and evenOrodd == '짝수':
    passOrNot = '입차 가능'
print(f'귀하의 차량은 {passOrNot}합니다')
