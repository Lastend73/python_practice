# 두 숫자를 인자로 받아 큰수를 리턴하는 함수를 정의하고 호출
def hamsu(a :int, b:int) :
    if a > b :
        return a
    else :
        return b
      
num1 = input("숫자 1? :")
num2 = input("숫자 2? :")

print(f"큰수는 : {hamsu(num1,num2)}입니다")