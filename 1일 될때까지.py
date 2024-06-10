## n, k를 공백 기준 입력 받
n, k = map(int, input().split())
## 연산 수행 횟수 변수값 
result = 0

while True:
## k로 나누어 떨어지지 않은경우 가장 근접한 나누어 떨어지는수(target)
    target = (n // k) * k
## 나누어 떨어지지 않을때 1을 빼는 연산을 몇번해야하는지 한번에 구할수 있음
    result += (n - target)
## 연산횟수 구했으니 가장 나누어떨어지는 target으로 n을 변경
    n = target
##  n이 k보다 작다면 반복문 탈출
    if n < k:
        break
## 그렇지 않다면 n을 k로 나누기
    result += 1
    n //= k
## 탈출한 수가 1보다 크다면 1로 만들어주는데 필요한 연산개수 구하기
result += (n - 1)
print(result)
    
