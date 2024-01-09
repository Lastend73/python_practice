# 할일 관리
todos = [
    {"tno" : 1 , "title":"할일 1","reg_day" : "2024-01-09", "finsh" : False},
    {"tno" : 2 , "title":"할일 2","reg_day" : "2024-01-09", "finsh" : False}
]

# 할일 번호를 입력받아 찾아서 출력

choice = int(input("할일번호 출력 ? :"))
찾았니 = False
for todo in todos :
    if choice == todo["tno"] :
        print(todo)
        찾았니 = True
        break
if 찾았니 == False :
    print("할일을 찾을 수 없습니다")