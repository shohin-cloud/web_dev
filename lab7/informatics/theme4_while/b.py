n = int(input())

if n % 2 == 0:
  print(2)
else:
  i = 3
  while i * i <= n:
    if n % i == 0:
      print(i)
      break
    i += 2
  else:
    print(n)
