from func001 import sample1
from func001 import get_major
from func001 import price_age
from func001 import price_people

# 테스트하는 함수를 작성
# unit test (단위테스ㅌ)
# 테스트하는 함수는 pytest로 실행이 가능

def test_sample() :          
    assert sample1() == 10

def test_is_amjor() :
    assert get_major(20) is True
    assert get_major(18) is False
    assert get_major(15) is False

def test_price_age() :
    assert price_age(20) == 0
    assert price_age(65) == 0
    assert price_age(25) == 3000
    
def test_price_people() :
    assert price_people(9) == 27000
    assert price_people(10) == 24000
    assert price_people(11) == 26400