# 정수로 모험가 공포심(총 인원수) 입력받기
n = int(input())
# 총 모험가 공포심 리스트로 입력받기(공백 구분)
data = list(map(int, input().split()))
# 리스트 오름차순
data.sort()

result = 0
group = 0

# 공포심 낮은순부터 차근착느 확인
for i in data:
# 그룹에 포함시키기
    group += 1
# 현재 그룹공포보다 다음 인원공포가 이상이면 그룹결성
    if group >= i:
# 총 그룹수 추가 
        result += 1
# 현재 그룹인원 초기화
        group = 0

print(result)
