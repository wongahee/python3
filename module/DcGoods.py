# 할인율 적용 프로그램
# 1개 - 5%, 2개 - 10%,
# 3개 - 20%, 4개 이상 - 30%

def checkDiscount(goods):
    rate = 0.3  # 할인율 기본값
    sum = 0

    if len(goods) == 1:
        rate = 0.05
    elif len(goods) == 2:
        rate = 0.1
    elif len(goods) == 3:
        rate = 0.2

    for i in range(len(goods)):
        sum += goods[i]

    fare = sum - (sum * rate)  # 할인율이 적용된 총 합계금액

    print(f'할인율 : {rate * 100}%')
    print(f'총 구매금액 : {sum}원')
    print(f'할인적용 구매금액 : {fare}원')

def discountGoods():
    goods = []
    flag = True

    while flag:
        job = input('상품을 구매 하시겠습니까? 1.구매, 2.종료 ')
        if job == '1':
            price = int(input('구매한 상품의 금액을 입력하세요. '))
            goods.append(price)

        elif job == '2':
            flag = False
            checkDiscount(goods)

        else:
            print('잘못입력하셨습니다.')

