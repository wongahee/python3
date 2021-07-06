# # 로그인 기능 만들기
# # for문
# for i in range(1, 4+1):
#     userid = input('아이디를 입력하세요.')
#     passwd = input('관리자 암호를 입력하세요. ')
#
#     if userid == 'admin' and passwd == 'hanbitac':
#         print('로그인 되었습니다.')
#         break
#     else:
#         print('암호를 다시 확인하세요!')
# else:
#     print('로그인 실패!! 횟수 초과!!!')

# while문
cnt = 1

while True:
    if cnt > 5:
        print('로그인 실패!! 횟수 초과!!!')
        break

    userid = input('아이디를 입력하세요.')
    passwd = input('관리자 암호를 입력하세요. ')

    if userid == 'admin' and passwd == 'hanbitac':
        print('로그인 되었습니다.')
        break
    else:
        print('암호를 다시 확인하세요!')
    cnt += 1
print('로그인 실패!! 횟수 초과!!!')