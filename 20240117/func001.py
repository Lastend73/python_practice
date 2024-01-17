def sample1() : 
    return 10

# 나이를 입력받아 생년/미성년 판단
def get_major(nai : int) -> bool :
    return nai > 18

# 나이를 입력받아 입장료를 리턴하는 함수
# 25~64세면 3000원, 기타는 무료
def price_age(nai : int)  :
    price = 0
    if nai > 24 and nai <65  :
        price = 3000
    return price

# 입장료를 3000원이다 10명이상이면 1인당 2400원
# 인원수를 입력받아 요금을 출력
def price_people(people : int) :
    price = 3000
    if people >= 10 :
        price = 2400
    return people * price