# 공간의 크기 입력 
n = int(input())
# 제시한 좌표
x, y = 1,1
# 이동할 플랜 받을 문자열
plans = input().split()

# L, R, U, D 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1 ,0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동계획 하나씩 확인 
for plan in plans:
# 이동 후 좌표 구하기 (move_types 대로 좌표이동)
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
# 공간이 벗어난다면 아무행동 하지 않기 
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
