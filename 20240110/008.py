 # 1부터 5의 합계를 출력
result = 0
for x in range(1,11):
    result = result + x
print(result)

# 1 ~ 10 사이의 3의 배수의 합계 

result_b = 0
for x in range(1,11):
    if x%3 == 0  :
        result_b = result_b + x

for x in range(1,11):
    if x%3 != 0  :
        continue

print(result_b)
print()
# 1 ~ 100 사이의 5과 7의 공배수를 출력하시오
for x in range(1,101):
    if x%5 == 0  and x%7==0 :
        print(x)

# 1 ~ 100 사이의 5과 7의 배수를 출력하시오 e단 공배수는 제외
        
for x in range(1,101):
    if (x%5 == 0  or x%7==0) and not(x%5 == 0  and x%7==0):
        print(x,end=" ")