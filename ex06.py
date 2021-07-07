# 업무 컴퓨터 수량 파악
# 근무시간 * 컴퓨터 수
# 8 * 3 = hour * computer
# computer = 8 * 3 / hour

import math

hour = int(input('근무시간을 입력하세요. '))
computer = math.ceil(24 / hour)

print(f'필요한 컴퓨터 : {computer}')

# ------선생님 풀이----------
computer = 3 * 8 // hour                    # 몫
addCom = 1 if (3 * 8 % hour) > 0 else 0    # 나머지
print(f'필요한 컴퓨터 : {computer + addCom}')