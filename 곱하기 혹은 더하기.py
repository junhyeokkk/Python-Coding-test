# 문자열로 입력을 받아야함(공백 구분이 아님)
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
               num = int(data[i])
# 두 수중 하나라도 0이거나 1일때 더하기 아니면 곱하기(key)
               if num <= 1 or result <= 1:
                   result += num
               else:
                   result *= num
print(result)
