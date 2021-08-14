# int(): 괄호안의 내용을 정수로 만들어줌
# input(): 사용자에게 입력 받을 수 있음
a = int(input())
b = int(input())
c = int(input())

# [] : 리스트 생성
# list.append(): 리스트의 맨 뒤에 괄호안의 내용 추가
lst = []
lst.append(a)
lst.append(b)
lst.append(c)

# max(): 괄호안의 숫자 중 최대값 반환
# min(): 괄호안의 숫자 중 최솟값 
# print(): 괄호 내용을 출력함
print(f'max : {max(lst)}')
print(f'min : {min(lst)}')