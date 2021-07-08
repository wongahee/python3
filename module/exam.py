# 시험 통과 여부 출력하기
def passExam(kor, eng, mat):
    tot = kor + eng + mat
    avg = tot / 3

    isPass = 'Fail'

    isAll60 = avg >= 60
    is40 = kor < 40 or eng < 40 or mat < 40

    if isAll60 and not is40:
        isPass = 'Pass'

    # 파이썬에서는 함수의 리턴값으로 2개 이상 지정가능
    return tot, avg, isPass

def printPass(scores):
    for k, v in scores.items():
        print(f'{k} : {v}')
