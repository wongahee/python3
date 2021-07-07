# 혈액 보관 시스템
A = []
B = []
AB = []
O = []

num = 0

for i in range(10):
    blood = input('헌혈해 주셔서 감사합니다. 혈액형을 선택하세요 \n'
                  'A, B, AB, O : ')
    if blood == 'A' or blood == 'a' : A.append(blood)
    elif blood == 'B' or blood == 'b' : B.append(blood)
    elif blood == 'AB' or blood == 'ab' :  AB.append(blood)
    elif blood == 'O' or blood == 'o' : O.append(blood)

print(f'혈액형별 수급 현황 :')
print('-------------')
print(f'A형 : {len(A)}명, B형 : {len(B)}명, AB형 : {len(AB)}명, O형 : {len(O)}명')

# 풀이 2
bloods = []

for i in range(10):
    blood = input('헌혈해 주셔서 감사합니다. 혈액형을 선택하세요 \n'
                   'A, B, AB, O : ')
    bloods.append(blood)

print('-'*30)
print('혈액형 수급 현황')
print('-'*30)
print(f'A형 : {bloods.count("A")}명, B형 : {bloods.count("B")}명 '
      f'AB형 : {bloods.count("AB")}명, O형 : {bloods.count("O")}명')
print('-'*30)
