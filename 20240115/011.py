# 년도를 입력받아 다음 윤년을 출력
# 2020입력 : 다음 윤년은 2000년입니다 오타일듯?
# 2021입력 : 다음 윤년은 2024년입니다

input_num = int(input("몇년? : "))

try :
    year = 0
    if input_num%4==0 :
        year = input_num
    else :
        year = input_num//4*4+4
    print(f"다음 윤년은 {year}년입니다")
except :
    print("정확한 년도를 입력하세요")