# 계산기 프로그램
def computer():
    num1 = int(input('첫번째 숫자를 입력하세요. '))
    op = int(input('연산자를 선택하세요. 1.덧셈, 2.뺄셈, 3.곱셉, 4.나눗셈'))
    num2 = int(input('두번째 숫자를 입력하세요. '))

    compute(op, num1, num2)

def compute(op, num1, num2):     # compute에 없는 변수들을 매개변수로 받음
    result = ''

    if op == 1: result = num1 + num2
    elif op == 2: result = num1 - num2
    elif op == 3: result = num1 * num2
    elif op == 4: result = num1 / num2
    else:
        print('다시 입력하세요')
    print(f'연산 결과 : {result}')

computer()
