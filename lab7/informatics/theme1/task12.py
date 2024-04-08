n = int(input())

ss = n % 60
mm = (n % 3600) // 60
h = (n // 3600) % 24

print(f"{h}:{mm:02d}:{ss:02d}")