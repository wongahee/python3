# 로또 당첨 게임
import random as r

# 사용자에게 로또 입력받음
# def readlotto():
#     magic = []
#     for i in range(6):
#         val = input(f'1부터 45사이의 정수를 하나 입력하세요. ({i+1}/6) : ')
#         magic.append(int(val))
#     return magic
#
# # 컴퓨터가 로또 생성함
# def makeLotto():
#     magic = []
#     for i in range(6):
#         magic.append(r.randint(1, 45))
#     return magic

def readlotto():
    magic = []
    i = 0
    while len(magic) < 6:
        val = int(input(f'1부터 45사이의 정수를 하나 입력하세요. ({i+1}/6) : '))
        if magic.count(val) == 0:   # 입력한 정수가 magic 리스트에 존재하는지 검사
            magic.append(val)
            i += 1

    return magic

# 컴퓨터가 로또 생성함
def makeLotto():
    magic = []
    while len(magic) < 6:
        val = r.randint(1, 45)
        if magic.count(val) == 0:
            magic.append(val)

    return magic

def Lotto645():
    magic = readlotto()
    lotto = makeLotto()
    wins = []

    for v in magic:
        if lotto.count(v) != 0: wins.append(v)
    print(f'이번주 로또 번호', magic)
    print(f'내가 선택한 번호', lotto)
    print(f'일치하는 숫자 : ', wins)

# a의 인덱스2값이 b에 존재하는지 알아보기
# a = [1, 2, 3]
# b = [4, 5, 3]
# b.count(a[2])