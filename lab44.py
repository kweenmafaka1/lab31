n = int(input())
b = 0
i: int
for i in range(1, n + 1):
    b += i
for i in range(n-1):
    b -= int(input())
print(b)