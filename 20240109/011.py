# 숫자 리스트 -> 추가, 목록, 합계, 변경, 삭제 함수Ver.

numbers = []

def print_memu():
    print('##### 숫자 CRUD #####')
    print("1:추가, 2:목록, 3:삭제, 999:종료")
    select=  input("선택? : ")
    return select

def num_add():
   val = int(input("추가할 숫자 입력? : "))
   numbers.append(val)

def list_num():
    for num in numbers :
      print(num, end=" ")
    print()
   

def del_num():
    for num in numbers :
      print(num, end=" ")
    print()
    
    if len(numbers) == 0 :
        print("삭제할 번호가 없습니다")
    else :
        select_num = int(input("삭제할 숫자는? :"))
        for num in numbers :
            if num == select_num :
                numbers.remove(num)
                break
        

while True : 
    select = print_memu()
    if select == '1' :
        num_add()
    elif select == '2' :
      list_num()
    elif select == '3' :
      del_num()
    elif select == '999' :
      print("감사합니다.")
      break
    else :
       print("번호를 잘못입력했습니다")
    print()
