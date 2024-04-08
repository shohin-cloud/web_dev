n = int(input())

l_t = 45 * n

b_t_5 = 5 * (n // 2)
b_t_15 = 10 * ((n+ 1) // 2 - 1)
b_t = b_t_5 + b_t_15

t_t = l_t + b_t

hours = 9 + t_t // 60
minutes = t_t % 60

print(f'{hours}:{minutes:02d}')