from EMP import EMP
from datetime import datetime

class EMPService:
    # 객체생성 없이 바로 사용가능한 static method로 선언 - @staticmethod
    @staticmethod
    def readEmp():  # 사원번호, 이름, 성, 이메일, 전화번호, 입사일 등 입력
        empno = input('사원번호는? ')
        fname = input('이름은? ')
        lname = input('성은? ')
        email = input('이메일은? ')
        phone = input('전화번호는? ')
        hdate = input('입사일은? ')

        return EMP(empno, fname, lname, email, phone, hdate)

    @staticmethod
    def computeDuty(emp):  # 입사일 기준 근무일수 계산
        # yyyy-mm-dd 형식의 입사일 입력값 자르기
        hdate = emp.hdate.split('-')

        now = datetime.now()
        hire = datetime(int(hdate[0]), int(hdate[1]), int(hdate[2]))
        days = now - hire  # 근무일 수

        print(f'str(days).split(' ')[0]일')
        # '6600 days, 12;47:53.715744'에서 맨 앞 6600만 출력

    def printEmp(self, e):
        print(e.empno, e.lname, e.fname, e.email, e.phone, e.hdate, e.jobid,
              e.salary, e.commission, e.mgr, e.deptid)