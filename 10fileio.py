# 파일 다루기

# 입력한 성적데이터를 파일에 저장
fname = 'c:/java/sungjuk.dat'

name = input('이름은? ')
kor = int(input('국어는? '))
eng = int(input('영어는? '))
mat = int(input('수학은? '))

f = open(fname, 'w')    # 지정한 파일을 쓰기모드 엶

# data = 'Hello, World!!'
data = f'{name}, {kor}, {eng}, {mat}'
                # 파일에 기록할 내용을 문자열로 작성
f.write(data)
f.close()

# 기록한 성적데이터를 파일로부터 읽어오기
f = open(fname, 'r')    # r: 읽기모드
                        # f변수에 fname으로 파일을 엶
data = f.read()
print(data)
f.close()

# 일정관리 메모를 입력하여 텍스트 파일에 저장하기
def saveMemo(memo):
    fname = 'c:/java/myMemo.txt'
    f = open(fname, 'a')        # a = append, 추가모드로 파일 초기화
    f.write(memo + "\n")
    f.close()

def menoMain():
    memo = input('메모를 입력하세요. ')
    saveMemo(memo)

menoMain()

# py3 방식으로 파일 다루기
# 기존 파일입출력 코드에서 불편한 점은
# 파일 작업 후에는 반드시 close를 해야한다는 것
# with문을 사용하면 명시적으로 close를 사용하지 않아도 됨
with open(fname, 'w') as f:
    f.write('blah blah~')

# 파일에서 데이터 읽어오기
fname = 'c:/java/employees.csv'

with open(fname) as f:
    data = f.read()    # 모든 데이터를 한번에 다 읽어옴
    print(data)

with open(fname) as f:
    data = f.readline() # 데이터 한 줄씩 읽어오기
    print(data)

with open(fname) as f:
    data = f.readlines() # 모든 데이터를 한 줄 단위로 읽어와 리스트에 저장
    print(data)

# employees.csv에서 사번, 이름, 입사일, 급여를 출력하세요
with open(fname) as f:
    f.readline()        # 첫 줄은 읽기만 함, 처리x

    while True:
        line = f.readline()
        if not line: break     # 읽을 데이터가 없는 경우 작업중단
        data = line.split(',') # 문자열을 ,로 분리해서 리스트로 저장

        empno = data[0]
        name = data[1]
        hdate = data[5]
        sal = int(data[7])

        emp = f'{empno} {name} {hdate} {sal:,}'  # 사번 이름 입사일 급여
        print(emp)

# 타이타닉 데이터셋을 이용해서
# 승객이름_name, 성별_sex, 나이_age, 승선위치_embarked, 사망여부_survived
# 등을 추출해서 출력하세요
# 단, embarked가 S이면 'Southampton', C이면 'Cherbourg',
# Q이면 'Queenstown' 이라 출력함
# survived가 0이면 '사망', 1이면 '생존' 이라 출력함
fname = 'c:/java/titanic3b.csv'

with open(fname) as f:
    f.readline()

    while True:
        line = f.readline()
        if not line: break

        data = line.split(',')

        # name = data[2]
        sex = data[2]
        age = data[3]
        embarked = data[9]
        survived = data[1]

        if embarked == 'S': pos = 'Southampton'
        elif embarked == 'Q': pos = 'Queenstown'
        elif embarked == 'C': pos = 'Cherbourg'

        if survived == '0': '사망'
        elif survived == '1': '생존'

        if age == '': age = '0'

        titanic = f'{sex}\t {age}\t {embarked}\t {survived}'
        print(titanic)
