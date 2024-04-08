def calculate_time_difference(h1, m1, s1, h2, m2, s2):
  t_s1 = (h1 * 3600) + (m1 * 60) + s1
  t_s2 = (h2 * 3600) + (m2 * 60) + s2
  t_d = t_s2 - t_s1

  return t_d

h1, m1, s1 = int(input()), int(input()), int(input())
h2, m2, s2 = int(input()), int(input()), int(input())


t_d = calculate_time_difference(h1, m1, s1, h2, m2, s2)

print(t_d)
