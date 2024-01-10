# 두 숫자를 입력방다 큰 수를 가리는 숫자

def compare_num(a : int , b :int) :
    if a > b :
        return a
    elif a < b :
        return b
    elif a == b :
        return "same" 
    
input_num1 = int(input("첫번째 번호? : "))
input_num2 = int(input("두번째 번호? : "))

result = compare_num(input_num1,input_num2)

if result == "same":
    print("같은 숫자")
else :
    print(f"큰수 : {result}")