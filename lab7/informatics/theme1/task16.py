def calculate_cost(a, b, n):
  total_cost_in_kopecks = a * 100 + b
  total_cost_in_kopecks *= n
  rubles = total_cost_in_kopecks // 100
  kopecks = total_cost_in_kopecks % 100

  return rubles, kopecks


a = int(input())
b = int(input())
n = int(input())

rubles, kopecks = calculate_cost(a, b, n)

print(rubles, kopecks)
