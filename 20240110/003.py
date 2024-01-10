# 숫자를 입력받아 절대값을 계산하는 함수

def 절대값(num : int) :
    if num < 0 :
        return -num
    else :
        return num

input_num = int(input("절대값? : "))

print(절대값(input_num))