# 사각형의 너비와 높이를 입력받아 면적을 출력하는 함수
# 너비와 높이는 실수로 처리
# 면적은 round 함수를 이용해 소수점 첫째자리까지 출력

width = float(input("길이 :"))
heigth = float(input("높이? :"))

result = round(width*heigth,0)
print(f"넓이 : {result}")