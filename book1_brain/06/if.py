import sys

a = int(input('수를 입력하세요: '))

if a == 0:
    print('0은 나눗셈에 이용할 수 없습니다.')
    sys.exit(0)

print('3 /', a, '=', 3/a)

