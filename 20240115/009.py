        # 4의 배수면 윤년이다. 단 100의 배수이면 윤년이 아니다
        # 윤년여부를 출력
input_num = int(input("몇년? : "))

try :
    if input_num % 4 == 0 :
        print("윤년")
    else :
        print("윤년 아님")

except : 
    print("정확한 년도를 입력하세요")