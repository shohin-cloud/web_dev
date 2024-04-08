n = int(input())
m = int(input())

days, remainder = divmod(m, n)
days_to_travel = days + (remainder != 0)


print(days_to_travel)
