# 숫자 리스트 -> 추가, 목록, 합계, 변경, 삭제 함수Ver.

numbers = [1,3,5]

def print_memu():
    print('##### 숫자 CRUD #####')
    print("1:추가, 2:목록, 3:삭제, 999:종료")

def input_select():
    select = input("메뉴선택 :")
    return select

def add_value():
    value = int(input("값 입력 : "))
    numbers.append(value)

def list_number():
    for num in numbers:
        print(num,end = " ")
    print()

def delete_number() :
    value = int(input("삭제할 값 입력 : "))
    index = 0
    for num in numbers:
        if num == value :
            del numbers[index]
        index = index +1
    
while True :
    print_memu()
    select = input_select()
    if select == '1':
        add_value()
    elif select == '2':
        list_number()
    elif select == '3':
        delete_number()
    elif select == '999':
        break
    print()
        