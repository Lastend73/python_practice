numbers = [1,3,5,7]

#숫자를 입력받아 그 숫자가 numbers 에 있는지 출력 실패는 numbers ,모든 값의 대해서 못ㅂ\찾았을때 한일 성공 결과 값의 조거닝 다르다

num = int(input("번호? : "))
print(num in numbers)

for item in numbers :
    if item == num :
        print(True)