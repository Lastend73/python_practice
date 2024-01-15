# 급여를 인자로 받아 소득세, 국민연금, 건강보험를 제외한 실수령액을 계산하는 함수를 정의하고 호출
# 소득세율은 3.3%, 국민연금은 4.5%, 건강보험은 3.5%로 한다
# 소수점 이하 금액은 절사한다

pay = int(input("월급은? :"))

income_tax = int(pay * 3.3/100)
pension_tax = int(pay * 4.5/100)
helath_tax = int(pay * 3.5/100)

print(f"소득세 : {income_tax}원")
print(f"국민연금 : {pension_tax}원")
print(f"건강보험 : {helath_tax}원")

print(f"실수령액 : {int(pay-income_tax-pension_tax-helath_tax)}원")

