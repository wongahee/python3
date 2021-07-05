# 전기 요금 계산기
elec = float(input('전기 사용량을 입력하세요. '))

elecfee1 = elec * 99.3 + 910
elecfee2 = elec * 187.9 + 1600
elecfee3 = elec * 280.6 + 7300

if elec <= 200:
    print(f'사용량 : {elec} kwh \n'
          f'기본요금 : 910 원 \n'
          f'단가 : 99.3 원 \n'
          f'전기 요금 : {elecfee1} 원')
elif 201 <= elec <= 400:
    print(f'사용량 : {elec} kwh \n'
          f'기본요금 : 1600 원 \n'
          f'단가 : 187.9 원 \n'
          f'전기 요금 : {elecfee2} 원')
elif 400 < elec:
    print(f'사용량 : {elec} kwh \n'
          f'기본요금 : 7300 원 \n'
          f'단가 : 280.6 원 \n'
          f'전기 요금 : {elecfee3} 원')

# -----------선생님풀이----------
elec = float(input('전기 사용량을 입력하세요 '))
rate = 0 # 기본요금
price = 0 # 단가

if elec > 400:
    rate = 7300
    price = 280.6
elif elec >= 201:
    rate = 1600
    price = 187.9
elif elec <= 200:
    rate = 910
    price = 99.3

fare = rate + (elec * price)

print(f'사용량 : {elec:.1f} kwh \n'
      f'기본요금 : {rate:,} 원 \n'
      f'단가 : {price} 원 \n'
      f'전기 요금 : {fare:,} 원')