# 구구단 출력 프로그램
# 사용자로부터 숫자(1 - 9)를 하나 입력 받아,
# 구구단을 출력하는 프로그램을 작성해보세요
dan = int(input('조회할 단을 입력하세요(1-9)'))

for i in list(range(1, 10)): print(dan*i)

# -------선생님풀이---------
print(f'{dan} x 1 = {dan*1}\n'
      f'{dan} x 2 = {dan*2}\n') # 이 문장을 9번 입력

# 키보드로 정수를 하나 입력받아 그 값이 양수, 음수, 0인지 구분하는 프로그램을 작성하시오.
# 각각의 경우에 따라 “양수입니다”, “음수입니다”, “0입니다”라고 출력하도록 한다.
num = int(input('수를 입력하세요 : '))

result = '양수입니다' if (num > 0) else \
         '음수입니다' if (num < 0) else '0 입니다'
print(result)

# 지금 현재 수지의 통장잔액이 25,000원이다.
# 은행이자가 연 6%라 가정할 때, 몇 년이 지나야 통장잔액이 지금의 2배를 넘는지
# 알아보는 프로그램을 작성하세요 => 답 : 12년
balance = 25_000
binter = 0.06
cnt = 0

# 밑 4줄 5만원이 넘어갈때까지 복사
cnt += 1
inter = balance * 0.06
balance = balance + inter
print(f'{cnt}, {balance:.2f}, {inter:.2f}')
