# 이 파일은 Main app 작업 중 짧은 테스트를 위한 공간임.


# 0x 이후의 문자를 인덱스 하려면 아래의 방법이 좋다

with open('Sensor Info.txt', 'r') as f:
    lines = f.readlines()

print(lines[4])

# '0x' 가 포함된 줄인지 확인
if '0x' in lines[4]:
    # '0x' 이후의 두 문자 추출
    start_index = lines[4].index('0x')
    d = lines[4][start_index+2:start_index + 6]
    print(d)
else :
    print('조건이 충족되지 않았습니다')

if '0x' in lines[9]:
    # '0x' 이후의 두 문자 추출
    start_index = lines[9].index('0x')
    e = lines[9][start_index+2:start_index + 6]
    print(e)
else :
    print('조건이 충족되지 않았습니다')

if '0x' in lines[15]:
    # '0x' 이후의 두 문자 추출
    start_index = lines[15].index('0x')
    e = lines[15][start_index+2:start_index + 6]
    print(e)
else :
    print('조건이 충족되지 않았습니다')
