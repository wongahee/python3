# Dictionary 딕셔너리
ages = {'박찬호':48, '박지성':40, '박세리':50, '이승엽':43}
type(ages)
print(ages) # 위와 똑같이 출력됨

person = {'이름':'홍길동', '나이':25, '주소':'서울 종로구 삼일대로', '몸무게':88.8, '취미':['게임', '운동', '영화 감상']}    # 값이 많을 경우 리스트형태로 선언

print(person)

grade = {'c/c++':'a', 'java':'b+', '네트워킹':'c',
         '보안':'a+', '해킹':'f', '시스템':'c+'}
print(grade)

# 홍길동의 나이와 취미 조회
person['나이']
person['취미']

# 홍길동의 혈액형 추가
person['혈액형'] = 'A'
person

# dict에 기존 키와 값으로 구성한 항목을 추가하려하면 기존키에 저장된 값이 적용됨
person['혈액형'] = 'O'

# dict에서 항목 삭제 : pop
person.pop('몸무게')
person

# person.pop('나이')
# person.pop('취미')

dellist = ['나이', '취미']
for key in dellist:
    person.pop(key)

# dict 모든 항목 출력
for key in person.keys():
    print(person[key])

# dict의 키와 값 모두 가져오기 : items
person.items()

for k, v in person.items():
    print(k, v)

# 중간고사 성적 관리 프로그램 만들기
sungjuk = {'c/c++':'a', 'java':'b+', '모바일':'c', '보안':'a+', '해킹':'f', '시스템':'c+'}

sungjuk['java']
sungjuk['시스템']

sungjuk['파이썬'] = 'a'
sungjuk['OS'] = 'a+'

sungjuk['java'] = 'f'
sungjuk['시스템'] = 'a'

for k, v in sungjuk.items():
    print(k, '\t:', v)

# 딕셔너리 for 축약문
# { 키/값 표현식 for 키,값 in zip(반복가능객체1, 반복가능객체2) }

# 이름과 성적 리스트를 dict 객체로 재생성하세요
name = ['혜교', '지현', '수지'] # 키
grd = ['수', '양', '미']       # 값
sj = {}

# 반복문 사용x
sj[name[0]] = grd[0]
sj[name[1]] = grd[1]
sj[name[2]] = grd[2]

# 반복문을 사용해서 축약
for i in range(3):
    sj[name[i]] = grd[i]
print(sj)

# dict comprehension
# { 키/값 표현식 for 키,값 in zip(반복가능객체1, 반복가능객체2) }
sj2 = {key: val for key, val in zip(name, grd)}

# zip : 여러 개의 데이터를 하나로 합쳐서 iterable한 객체로 생성해줌
# 개별 객체는 튜플로 반환
for pair in zip(name, grd):
    print(pair)
