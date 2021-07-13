# str
# 문자열은 문자들의 리스트와 유사
# 따라서, 리스트 슬라이싱을 통해 문자열 내 개별문자를 추출할 수 있음

# '파이썬은완전재미있어요'라는 문자열에서 홀수 위치에 있는 문자를 #으로 바꿔 출력하는 코드 작성
str = '파이썬은완전재미있어요'
for i in range(len(str)):
    if i % 2 ==0 : print(str[i] ,end='')
    else: print('#',end='')
print()

# 문자열 함수
# 대소문자 변환
str = 'Python is Easy. 그래서 programming이 재미있어요'

print(str.lower())
print(str.upper())
print(str.swapcase())
print(str.title())

# 문자열 찾기
str = '파이썬 공부는 즐겁습니다 물론 모든 공부가 다 재미있지는 않죠 ^^'

str.count('공부')     # 특정문자열 포함 개수

str.find('공부')      # 특정문자열 찾은 인덱스값
str.find('공부', 5)   # 인덱스를 시작으로 특정문자열 찾기
str.find('공부', str.find('공부')+1)
str.find('없다')      # 찾는 문자열이 없을 경우 : -1
str.rfind('공부')     # 오른쪽부터 찾은 인덱스값

str.index('공부')
str.index('공부', 5)
str.rindex('공부')
str.index('없다')     # 찾는 문자열이 없을 경우 오류 발생!!

str.startswith('파이썬')   # 시작문자열이 맞는지 T/F 여부
str.startswith('파이썬', 10)   # 10 index값 이후로 시작문자열이 맞는지 T/F 여부
str.startswith('물론', 14)
str.endswith('^^')        # 끝문자열이 맞는지 T/F 여부

# 문자열 공백 제거
# strip() 함수
# 매개변수로 제거할 문자 지정. 매개변수가 없다면 공백을 제거함
str = '  파  이  썬  '
str.strip()     # 양쪽 공백 제거
str.lstrip()    # 왼쪽
str.rstrip()    # 오른쪽

str = '--파--이--썬--'
str.strip('-')  # 양쪽 - 제거
str.lstrip('-')
str.rstrip('-')

str = '<<파 << 이 >> 썬>>'
str.strip('<>')     # 지정문자들 제거(<,>)
str.lstrip('<>')
str.rstrip('<>')

str = '열심히 파이썬 공부중~'
str.replace('파이썬','Python')   # 지정한 문자열을 새로운 문자열로 변경

str = '  파  이  썬  '
str.replace(' ', '')

str = '--파--이--썬--'
str.replace('-', '')

str = '<<파 << 이 >> 썬>>'
str = str.replace('<', '')
str = str.replace('>', '')
str.replace(' ','')

# 문자열 결합
str = '혜교,98,65,77'     # 구분기호로 문자열을 분리하고 리스트로 저장
str.split(',')

str = '혜교|98|65|77'
str.split('|')

str = '혜교\r\n98\r\n65\r\n77'
str.split('\r\n')   # 줄바꿈 기호 기준 문자열분리
str.splitlines()

str = ['혜교', '98', '65', '77']
','.join(str)   # 리스트의 각 항목을 구분기호로 합침

# join을 사용하기 않은 경우
result = ''
for s in str:
    result += s + ','

# 객체를 특정함수에 일괄적으로 적용하기
# map(적용할 함수명, 대상객체)
str = ['123', '456', '789']     # 문자열을 숫자로 변경

nums = []           # map을 사용하지 않는 경우
for s in str:
    nums.append(int(s))

nums = list(map(int, str))  # str에 모든항목들을 int로 적용시켜 list에 담음

# 문자열 정렬하기
str = '파이썬'
str.center(10)      # 가운데 정렬
str.ljust(10)       # 좌측 정렬
str.rjust(10)       # 우측 정렬

# 특정 문자로 채우기
str = '파이썬'
str.center(10, '-') # 가운데 정렬 & 공백은 -로 채우기
str.zfill(10)       # 0으로 채우기

# 문자열 구성 파악하기
'1234'.isdigit()
'abcd'.isalpha()
'abc123'.isalnum()
'abcd'.islower()
'abcd'.isupper()    # F
' '.isspace()

# 입력한 값이 영어/한글이면 '글자', 숫자면 '숫자', 섞여있으면 '글자+숫자'
# 그 외 나머지 문자면 '모르겠습니다'라고 출력하는 프로그램
str = input('문자열 입력 : ')

if str.isalpha() == True: print('글자')
elif str.isdigit() == True: print('숫자')
elif str.isalnum() == True: print('글자+숫자')
else: print('모르겠습니다')
