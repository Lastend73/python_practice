# bmi 지수를 계산하는 함수를 작성
# bmi는 체중 / 키의제곱인데 이때 키는 m단위이다(175cm이면 1.75)
# 체중은 kg 단위, 키는 cm 단위로 전달받는다
# bmi는 소수점 첫째자리까지 
      
weight = int(input("체중(kg)? : "))
height = float(input("키(cm)? : "))

height = height/100

bmi = round(weight/(height*height),1)

print(f"bmi : {bmi}")