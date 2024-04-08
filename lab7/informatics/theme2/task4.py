import math as m
n = int(input())
ans = m.sin(n)
if ans > 0:
    print(1)
elif ans < 0:
    print(-1)
else:
    print(0)