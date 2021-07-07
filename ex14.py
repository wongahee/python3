# 출석부 관리 시스템
students = ['정우람', '박으뜸', '배힘찬', '천영웅', '신석기', '배민규', '전민수', '박건우', '박찬호', '이승엽']

#1 가나다 순 정렬
students.sort()
students

#2 박찬호 전학감
students.remove('박찬호')
students
print(len(students))

#3 앞에서 3명 선발
students[:3]

# 이병규 전학옴
students.insert(5,'이병규')
students

# 역순
students.reverse()
students

# 정우람->정잘남 개명
students.pop(1)
students.insert(1, '정잘남')
students
