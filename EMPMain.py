from EMP import EMP
from EMPService import EMPService

emp = EMP(123, 'Steven', 'King', 'SKING', '01020002000', '2021-03-15',
          'AD_PRES', 24000, '', '', 90)
print(emp)

# 객체생성 후 메서드 호출
# empsrv = EMPService()
# emp = empsrv.readEmp()
# print(emp)

# 객체생성없이 바로 메서드 호출 - EMPService에 @staticmethod
emp = EMPService.readEmp()
print(emp)

EMPService.computeDuty(emp)