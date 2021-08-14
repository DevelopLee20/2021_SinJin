# input(): 사용자에게 입력 받을 수 있음
N = input()
sum = 0

# for: 반복문
# for i in N: N의 요소 하나씩 사용함
for i in N:
    # sum += int(i) : sum = sum + int(i) 와 같은 역할
    sum += int(i)

print(sum)