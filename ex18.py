# 다국어 인사말 프로그램
def hiworld(nation):
    hello = ''

    if nation == 1: hello = '안녕'
    elif nation == 2: hello = 'Hello.'
    elif nation == 3: hello = 'こんにちは'
    else:
        print('다시 입력해주세요.')
    print(hello)

nation = int(input('where are you from? 1.한국, 2.USA, 3.JAPAN '))
hiworld(nation)
