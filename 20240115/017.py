# 상품의 이름을 입력하면 가격을 알려주는 코드를 작성
# 단, 없는 상품을 입력하면 오류 메시지 출력

proudect_example = {"사과":3000 , "바나나":5000,"포도":4000}

fruit = input("과일? : ")

if fruit in list(proudect_example.keys()) : 
    print(f"가격 : {proudect_example[fruit]}원")
else :
    print('해당상품이 없습니다')