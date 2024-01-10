# 정수 변수를 2개만들어 나눗셈 결과 를 출력하시오
# 예외 처리가 필요하면 예외 처리 하시오
a,b= 20,0

def divide(a : int , b : int ) :
    return a/b

try :
    print(divide(a,b))
except :
    print("0으로 나눌 수 없습니다")