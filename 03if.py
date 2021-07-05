# if문
num = int(input('숫자를 하나 입력하세요 '))

if num > 10:
    print('num은 10보다 크다')

# 속도위반 경고하기 : 50km/h
speed = int(input('자동차의 현재 속도는 : '))

# if speed > 50:
#     print('속도 위반!!')
# or
if speed > 50: print('속도 위반!!')

else:
    print('>>>')

# 합격/불합격 출력 : if ~ else
score = int(input('점수를 입력하세요 : '))

if score >= 80:
    print('합격입니다')
else:
    print('불합격입니다ㅜㅜ 다시 도전해주세요~')

# pass
# 실행문이 정해지지 않을 경우 대체 작성하여 사용하는 키워드
if score >= 80:
    pass
else:
    pass

# 자동 온도조절장치 만들기
temp = int(input('기계 온도를 입력하세요. '))

if temp >= 40:
    print('팬(Fan) 가동')
else:
    print('팬(Fan) 중지')

# 입력받은 정수를 3으로 나눠 소수점 첫자리에서 반올림하여 출력하는 프로그램
num = int(input('양의 정수 입력 : '))

result = num / 3

if (result - int(result) >= 0.5):
    result = int(result) + 1    # 올림
else:
    result = int(result)        # 내림

print(f'결과 : {result}')

# 다이어그램 조건문만들기
mileage = int(input('마일리지를 입력하세요 : '))

if mileage >= 1000:
    print('마일리지 사용가능')
else:
    print('마일리지 사용불가')

# 성적처리
jumsu = int(input('점수를 입력하세요'))

if 60 <= jumsu < 70:
    print('양')
elif 70 <= jumsu < 80:
    print('미')
elif 80 <= jumsu < 90:
    print('우')
elif 90 <= jumsu <= 100:
    print('수')
else:
    print('가')

# 자동 주문 시스템 만들기
print('Good morning. Nice to meet you.\n'
      'Where are you from?\n'
      'Please select a number\n'
      '1. 대한민국 2. USA 3. 中國')
nation = input('')

if nation == '1':
    intro = '주문 하시겠어요?'
elif nation == '3':
    intro = '您要点菜吗?'
else:
    intro = 'Would you like to order?'

print(intro)

# 국가재난지원금 수령액 조회하기
pnum = int(input('인원수를 입력하세요. '))

if pnum == 1:
    print('400,000원 지원')
elif pnum == 2:
    print('600,000원 지원')
elif pnum == 3:
    print('800,000원 지원')
elif pnum >= 4:
    print('1,000,000원 지원')

# ------선생님 풀이---------
if pnum == 1:
    money = '400_000원 지원'
elif pnum == 2:
    money = '600_000원 지원'
elif pnum == 3:
    money = '800_000원 지원'
elif pnum >= 4:
    money = '1_000_000원 지원'

print(f'{money:,.1f}원 지원')

# BMI 지수 확인하기
weight = int(input('몸무게를 입력하세요.'))
height = int(input('신장을 입력하세요.'))

height = height / 100
bmi = weight / (height * height)

if bmi > 30: print('고도 비만')
elif bmi > 25: print('비만')
elif bmi > 23: print('과체중')
elif bmi > 18.5: print('정상 체중')
else: print('저체중')

# 중첩 조건문
# 버스 전용차로 단속 프로그램
print('1.월~금 2.토요일 3. 공휴일')

day = int(input('요일을 선택하세요. '))

if day == 1:
    print('버스 전용차로 단속 중입니다.')
    trans = int(input('1.버스 2.승용차 '))
    if trans == 1:
        print('버스입니다.')
    elif trans == 2:
        print('버스 전용차로 위반!!')
    else:
        print('다시 입력해주세요')
elif day == 2 or day == 3:
    print('토요일 및 공휴일은 단속하지 않습니다.')
else:
    print('다시 입력해주세요~!')

# --------선생님풀이----------
msg = '1.월~금 2.토요일 3. 공휴일 \n' \
      '요일을 선택하세요. '
day = input(msg)

if day == 1:
    msg = '버스 전용차로 단속 중입니다.'
else:
    msg = '토요일 및 공휴일은 단속하지 않습니다.'
print(msg)

msg = '1.버스 2.승용차\n' \
      '차종을 선택하세요'
car = input(msg)

if car == 1:
    msg = '버스입니다 - 단속대상x'
elif car == 2:
    if day == 1:
        msg = '버스 전용차로 위반!!'
    else:
        msg = '승용차입니다 - 단속대상x'

print(msg)

# 마스크 구매가능요일 출력 프로그램
endBirthYear = int(input('출생연도 끝자리 입력 : '))
age = int(input('만 나이 입력 : '))

if age < 65:
    if endBirthYear == 1 or endBirthYear == 6:
        print('월요일 구매 가능합니다.')
    elif endBirthYear == 2 or endBirthYear == 7:
        print('화요일 구매 가능합니다.')
    elif endBirthYear == 3 or endBirthYear == 8:
        print('수요일 구매 가능합니다.')
    elif endBirthYear == 4 or endBirthYear == 9:
        print('목요일 구매 가능합니다.')
    elif endBirthYear == 5 or endBirthYear == 0:
        print('금요일 구매 가능합니다.')
else:
    print('언제든지 구매 가능합니다.')

# --------선생님풀이----------
if age < 65:
    if endBirthYear == 1 or endBirthYear == 6: day = '월'
    elif endBirthYear == 2 or endBirthYear == 7: day = '화'
    elif endBirthYear == 3 or endBirthYear == 8: day = '수'
    elif endBirthYear == 4 or endBirthYear == 9: day = '목'
    elif endBirthYear == 5 or endBirthYear == 0: day = '금'
    print(f'{day}요일에 구매 가능합니다')
else:
    print('언제든지 구매 가능합니다.')