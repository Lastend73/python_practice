# 리스트를 인자로 받아 합계를 리턴하는 함수를 정의하고 호출
def sum_number(num_sum : list) :
    return sum(num_sum)

num_list = [1,2,3,4,5]

print(f"합계는 : {sum_number(num_list)}")


      