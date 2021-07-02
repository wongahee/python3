# 수온 계산기
depth = int(input('수심을 입력하세요.'))

temp = 20
temp = temp - (depth // 10 * 0.7)

print(f'수온은 {temp}')
