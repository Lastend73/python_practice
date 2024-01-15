# 아래와 같은 내용을 저장하는 파이썬 변수 s로 만드시오
# 사는 곳 : 서울
# 성별 : 여자
# 이름 : 시은

# 나이와 혈액형을 입력받아 저장 후 출력하시오
      
people_list = {"사는 곳":"서울","성별" :"여자","이름" : "시은"}

age = input("나이? :")
blood = input("혈액형? : ")

people_list['나이'] = age
people_list['혈액형'] = blood

print(people_list)