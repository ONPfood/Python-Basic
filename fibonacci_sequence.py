# n 보다 작은 피보나치 수열을 인쇄합니다."""
n = 10000

a, b = 0, 1
while a < n:
    print(a, end=' ')
    a, b = b, a+b
