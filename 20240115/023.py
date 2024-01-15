# 리스트를 인자로 받아 최대값을 리턴하는 함수를 정의하고 호출
def max_num (num_max : list) :
    return max(num_max)

num_list = [1,2,3,4,5]

print(f"최대값은 : {max_num(num_list)}")