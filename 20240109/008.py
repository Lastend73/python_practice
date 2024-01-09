def sample(a:int) :
    print(a)

sample(10)
sample("hello")

# 정수 2개를 인자로 받아 덧셈후 출려하는 함수를 정의학소 호출

def plus_num(a:int|float, b:int|float):
    print(a + b)

plus_num(5,10)

def hap2(a :int|float, b : int|float) :
    # return 결과 -> 함수를 종료하고 결과로 바꿔라
    return a + b


print(hap2(1,4))
result = hap2(1,4)