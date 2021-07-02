# 성적처리프로그램
# 이름,국어,영어,수학을 입력받아 총점, 평균, 학점을 출력하는 프로그램
name= input('이름을 입력하세요 ')
kor = int(input('국어 점수를 입력하세요 '))
eng = int(input('영어 점수를 입력하세요 '))
mat = int(input('수학 점수를 입력하세요 '))

tot = kor + eng + mat
avg = tot / 3
grd = '수' if (avg >= 90) else \
      '우' if(avg >= 80) else \
      '미' if(avg >= 70) else \
      '양' if(avg >= 60) else '가'

print(f'이름: {name}, 총점은 {tot}, 평균은 {avg:.1f}, 학점은 {grd}입니다.')
