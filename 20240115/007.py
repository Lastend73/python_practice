        # 정수를 입력받아 짝수인지 홀수인지 출력하시오
        # 정수를 입력하지 않은 경우 예외처리하시오
try : 
    input_num = int(input("정수?  : "))

    if input_num%2 == 0 :
        print("짝수")
    else :
        print("홀수")
except :
    print("정수를 입력하세요")