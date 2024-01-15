        # 년도를 입력받아 그 해에 월드컵이 열리는지 또는 올림픽이 열리는 지 아니면 월드컵도 올림픽도 열리지 않는지 출력
        # 잘못된 입력에 대해 예외처리하시이
try : 
    input_num = int(input("년도? ex)2004  : "))

    if input_num%4 == 2 :
        print("월드컵")
    elif input_num % 4 == 0:
        print("올림픽")
    else :
        print("아무것도 안열림니다")
except :
    print("정수를 입력하세요")