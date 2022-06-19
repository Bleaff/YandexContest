str = input().split()
str = list(map(int, str))
count = str[0]
src = str[1]
dst = str[2]
if dst < src:
	print(min(src - dst - 1, count - src + dst - 1))
else:
	print(min(dst - src - 1, count - dst + src - 1))
