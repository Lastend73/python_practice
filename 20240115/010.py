  # 년도를 입력받아 다음 올림픽이 열리는 해를 출력
input_num = int(input("몇년? : "))

try :
    year = input_num//4*4+4
    print(f"다음 올림픽년도는 {year}년도입니다") 
except : 
    print("정확한 년도를 입력하세요")