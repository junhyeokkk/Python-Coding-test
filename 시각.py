# 시간 입력받기
n = int(input())

reuslt = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
# 문자열 합쳐서 3이 들어간다면 카운트 증가 
            if '3' in str(i) + str(j) + str(k):
                reuslt += 1
print(reuslt)
