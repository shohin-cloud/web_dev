n = int(input())
m = int(input())

min_n = int(n**0.5) +1
max_m = int(m**0.5)

for i in range(min_n, max_m+1):
    if i ** 2 <= m:
        print(i**2)