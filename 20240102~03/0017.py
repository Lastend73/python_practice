# 숫자를 2개 입력받아 큰수와 작은수를 출력하시오
# 예: 5와 8중 큰수는 8, 작은수는 5입니다
num1 = int(input('첫번째 숫자'))
num2 = int(input('두번째 숫자'))
large = max(num1, num2)
small = min(num2, num1)
print(f'{num1}와 {num2}중 큰수는 {large}, 작은수는 {small}')