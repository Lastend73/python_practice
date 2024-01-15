 # 문자열 리스트을 입력받아 가장 긴 문자열을 리턴

def str_len(str_list : list) : 
    len_max = ''
    for str_value in str_list :
        if len(str_value) > len(len_max) :
            len_max = str_value
    return len_max

string_list = ['a','ab','abdfd']

print(f"가장 긴 문자열은? : {str_len(string_list)}" )

      