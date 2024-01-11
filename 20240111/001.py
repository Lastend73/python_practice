#할일은 할일번호, 할일, 완료여부로 구성

todos = []
todo1 = {"tno" : 1,"title" :"자바공부" , "finish" : False}
todo2 = {"tno" : 2,"title" :"스프링 공부" , "finish" : False}
todo3 = {"tno" : 3,"title" :"파이썬 공부" , "finish" : False}
tno = 4 
todos.append(todo1)
todos.append(todo2)
todos.append(todo3)

print(todos) 

def print_list():
    select_num = 1
    for todo in todos :
        print(f"[{select_num}] {todo["title"]} 상태 : {todo["finish"]}")
        select_num = select_num + 1

def add_todo():
    # 함수 밖에 있는 변수르 변경하려면 global 함수이름
    global tno
    title = input("할일 입력 : ")
    todos.append({"tno" : tno,"title" :title , "finish" : False})
    tno = tno +1

def toggle_finsh():
    select_num = 1
    for todo in todos :
        print(f"[{select_num}] {todo["title"]} 상태 : {todo["finish"]}")
        select_num = select_num + 1

    select_toggle = int(input("어떤 것을 변경할 것 입니까? : "))

    if select_toggle <= len(todos) :
        todos[select_toggle-1]["finish"] = not todos[select_toggle-1]["finish"]
        print("변경 완료 했습니다")
    else :
        print("잘못 입력했습니다")

def delete_todo():
    select_num = 1
    for todo in todos :
        print(f"[{select_num}] {todo["title"]} 상태 : {todo["finish"]}")
        select_num = select_num + 1

    select_toggle = int(input("어떤 것을 삭제할 것 입니까? : "))

    if select_toggle <= len(todos) :
        del todos[select_toggle-1]
    else :
        print("잘못 입력했습니다")    

while True :
    print("### 할일 관리 ####")
    print('1: 목록, 2: 추가, 3:변경, 4: 삭제 , 999: 종료')
    select = input("메뉴 선택? : ")
    if select == '1' :
        print_list()            #호출
    elif select == '2' : 
        add_todo()
    elif select == '3' : 
        toggle_finsh()
    elif select == '4' : 
        delete_todo()
    elif select == '999' : 
        print("이용해주셔서 감사합니다")
        break
    print()

