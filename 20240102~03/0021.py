# 몇일인지 입력받아 몇개월 며칠인지 출력
# 333일 -> 11개월 3일
DAYS_PER_MONTH = 30
days = 333
months = 333//DAYS_PER_MONTH
days = days%30
print(f'{months}개월 {days}일')
