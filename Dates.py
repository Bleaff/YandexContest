str = input().split()
str = list(map(int, str))
x = str[0]
y = str[1]
z = str[2] 
year = max(x, y, z)
str.remove(year)
if str[0] <= 12 and str[1] <= 12 and str[0] != str[1]:
	print(0)
else:
	print(1) 
