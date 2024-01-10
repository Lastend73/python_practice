# for 문
# hello를 for 를 이용해 3번 출력하시오

for x in (1,2,3):
    print('hello')

# for를 이용해서 0~10 까지 짝수만 출력하시오
for x in range(11):
    if x%2==0 : 
        print(x)

# 1부터 5의 합계를 출력
result = 0
for x in range(1,6):
    result = result + x
print(result)