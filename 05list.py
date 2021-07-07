# 파이썬 리스트
attendList = ['순철', '병헌', '민우', '찬호', '민태']
print(attendList)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

# 자료형이 다른 값 list
complex = [1, 2.0, 3.1415, 40, '5', "6"]
print(complex)

for data in numbers:    # iterable
    print(data)

for data in complex:    # iterable
    print(complex)

# len : 리스트의 길이 출력
len(numbers)
len(complex)

msg = 'Hello, World!!'
print(len(msg))

# 입력한 글자 수 확인하기
msg = input('메시지를 입력하세요. ')

print(f'입력한 문자열의 길이 : {len(msg)}')

print(len(['Hello, Python!!']))     # list에 요소1개
print(len('Hello, Python!!'))       # 글자 수 15개

# 리스트의 모든 항목 조회
print(complex[0])
print(complex[1])
print(complex[2])
print(complex[3])
print(complex[4])
print(complex[5])

# for문을 사용하여 간단하게 코딩하기
for i in range(len(complex)):
    print(complex[i])

for item in complex:
    print(item)

for idx, item in enumerate(complex):
    print(f'{idx} : {item}')

print(complex.index(3.1415))

# sports 리스트에서 마지막 인덱스 값을 출력하는 프로그램을 만드시오
sports = ['baseball', 'basketball', 'tennis', 'golf', 'soccer']
print(sports.index('soccer'))
print(sports[len(sports)-1])

languages = ['c/c++', 'c#', 'python', 'java']
print(languages.index('python'))

# 취미 추가하기
# .append()함수 : (맨 뒤에 추가)
hobby = ['독서', '등산', '요리']
hobby.append('배구')
print(hobby)
#
# 누락된 숫자 추가하기
# .insert()함수 : 지정한 인덱스값에 추가
numbers = [1, 2, 3, 4, 5, 7, 8, 9]
numbers.insert(5, 6)    # 5번째에 숫자 6추가
print(numbers)

weather = ['the', 'weather', 'very']

weather.insert(2, 'is')
weather.insert(4, 'cold')
print(weather)

# 성적처리 프로그램
names = []
kors = []
engs = []
mats = []

for i in range(3):
    name = input('이름은?')
    names.append(name)
    kor = int(input('국어는?'))
    kors.append(kor)
    eng = int(input('영어는?'))
    engs.append(eng)
    mat = int(input('수학은?'))
    mats.append(mat)

tots = []
avgs = []
grds = []

for i in range(3):
    tots.append(kors[i] + engs[i] + mats[i])
    avgs.append(tots[i] / 3)

    grds.append('가')
    if avgs[i] >= 90:
        grds[i] = '수'
    if 80 <= avgs[i] < 90:
        grds[i] = '우'
    if 70 <= avgs[i] < 80:
        grds[i] = '미'
    if 60 <= avgs[i] < 70:
        grds[i] = '양'

for i in range(3):
    print(f'{names[i]}, {kors[i]}, {engs[i]}, {mats[i]} \n'
          f'{tots[i]}, {avgs[i]:.1f}, {grds[i]} \n')

# 리스트 수정
# 리스트[인덱스값] = 수정할값
hobby
hobby[1] = '여행'
hobby

# 리스트 삭제
# pop() 함수 : 맨 뒤에 항목 삭제
# pop(인덱스값) : 해당 위치의 항목을 제거
# del 키워드 : 지정한 위치의 인덱스값에 있는 값 삭제
hobby
hobby.pop()

sports
sports.pop(2)

# remove : 항목값으로 제거
languages
languages.remove('java')
languages.remove('c/c++')

# toDoList 리스트에서 할 일 지우기
toDOs = ['cleaning', 'shopping', 'TOEIC study', 'exercise']
toDOs.pop(0)
toDOs

# 과일 리스트에서 야채를 찾아 삭제하기
fruits = ['사과', '망고', '당근', '수박', '포도', '참외', '토마토']

# 위치값으로 삭제
fruits.pop(2)
fruits.pop(5)
fruits  # 확인

# 값으로 삭제
fruits.remove('당근')
fruits.remove('토마토')
fruits

# 합격 여부 판정하기
scores = [55, 35, 40, 70, 65, 30]

cnt = len(scores)
sum = 0
fails = 0
result = '아쉽습니다. 불합격하셨습니다.'

for i in range(cnt):
    if scores[i] < 40:
        fails += 1       # 과락수 증가
    sum += int(scores[i])

avg = sum / cnt
if avg >= 60 or fails == 0:
    result = '축하합니다. 합격하셨습니다.'

print(f'평균점수 : {avg:.2f}')
print(result)

# 정렬하기
numbers = [5, 1, 3, 4, 2, 6]

numbers.sort()
numbers

numbers.sort(reverse=True)
numbers

scores = [90, 100, 88, 85, 95, 92, 70, 75, 100, 92, 78, 80, 75, 95, 90, 100, 84]
scores.sort()
scores.sort(reverse=True)
scores

# 문자 정렬(한글)
names = ['김길동', '박길동', '이길동', '정길동', '홍길동']
names.sort()
names
names.sort(reverse=True)
names

# 문자 정렬(영어)
units = ['scv', 'marine', 'firebat', 'ghost',
         'driopship', 'battlecruiser', 'valkyrie']
units.sort(reverse=True)
units

# 리스트 슬라이싱
char = 'alphabet'

char[2:6]     # 2~5까지 추출
char[5]         # 0~4까지 추출
char[3:8]       # 3~7까지 추출
char[6:]        # 5~끝까지 추출
char[3:9]       # 3~8까지 추출

char[6:]        # 6~끝까지 추출
char[-4]        # 오른쪽 시작기준으로 4번째 요소를 시작


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# 0 1 2 3 4 5
# -5 -4 -3 -2 -1
# d,c,b,a 추출
alphabet[3::-1]     # 3부터 역순 추출
alphabet[-7::-1]
alphabet[-7:-11:-1]
