n = input()
f_num = ''

for i in range(len(n)-1, -1, -1):
    f_num += n[i]

print(int(f_num))