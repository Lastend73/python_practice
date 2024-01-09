# 초를 입력받아 몇분 몇초인지 출력
# 예) 210초라고 입력하면 3분 30초
input_seconds = 210
# 3 = 210 
minutes = input_seconds//60
# 30 = 210
seconds = input_seconds%60; 
#print(f'{minutes}분 {seconds}초')

# 분과 초를 입력하면 초를 출력
# 코드에 값이 직접 나타나는 것 : literal
minutes = 5
seconds = 10
# 상수는 대문자로
SECONDS_PER_MINUTE = 60
result = minutes * SECONDS_PER_MINUTE + seconds
print(result)