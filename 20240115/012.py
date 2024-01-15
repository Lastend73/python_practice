# 1~12까지 달을 입력받아서, 입력받은 달은 몇 일까지 있는지 출력하는 코드를 작성(윤년은 고려하지 않음)
# 2월: 28일
# 4월, 6월, 9월, 11월: 30일
# 1월, 3월, 5월, 7월, 8월, 10월, 12월: 31일

input_num = int(input("몇월? : "))

try :
    days = 0
    days_31 = [3,5,7,8,10,12]
    days_30 = [4,6,9,11]
    if input_num == 2:
        days = 28
    elif input_num in days_31 :
        days = 31
    elif input_num in days_30 :
        days = 30
    if days == 0:
        print("정확한 월을 입력해주세요")
    else :
        print(f"이번달은 {days}일까지 있습니다")
except :
    print("정확한 년도를 입력하세요")
      