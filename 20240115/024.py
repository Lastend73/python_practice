# 문자열 리스트을 입력받아 가장 긴 문자열의 길이를 리턴하는 함수

def str_len(str_list : list) : 
    len_max = 0
    for str_value in str_list :
        if len(str_value) > len_max :
            len_max = len(str_value)
    return len_max

string_list = ['a','ab','abdfd']

print(f"가장 긴 문자열 길이는? : {str_len(string_list)}" )

      