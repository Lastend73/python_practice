# 숫자를 입력받아 음수면 양수로 바꿔 출력
num = int(input('숫자 입력:'))
if num<0:
    print(-num)

# 길이를 입력받아 센티미터면 인치로, 인치면 센티미터로 변경
# 1인치 = 2.54센티미터
길이 = 100
kind = input('길이의 종류입력(cm/inch)')
if kind=='inch':
    print(길이*2.54, 'cm')
elif kind=='cm':
    print(길이/2.54, '인치')
else:
    print('cm 또는 inch를 입력하세요')




