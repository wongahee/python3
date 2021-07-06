# 369 게임 만들기
# 3의 배수에 박수 메세지 출력
for i in range(1, 99+1):
    clap = ''
    if i % 3 == 0 or i % 6 == 0 or i % 9 == 0:
        clap = '짝!'
    print(f'{i} {clap}')

# 두번째 방법
for i in range(1, 99+1):
    clap = ''
    if i < 10:              # 숫자가 한자리라면
        if i % 3 == 0:
            clap = '짝!'
    else:                   # 숫자가 두자리라면 - 34
        num1 = i // 10      # 숫자의 첫번째글자 추출(몫) - 3
        num2 = i % 10       # 숫자의 두번째글자 추출(나머지) - 4

        if num1 % 3 == 0:   # 첫번째 숫자가 3의 배수라면
            clap += '짝!'

        if num2 % 3 == 0 and num2 != 0: # 두번째 숫자가 3의 배수이고, 0이 아니라면
            clap += '짝!'

    print(f'{i} {clap}', end=',')
print()

# 미국판 369 게임 - buzz
# https://www.wikihow.com/Play-Buzz
