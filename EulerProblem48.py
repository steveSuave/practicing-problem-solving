a=0
for i in range(1,1001):
	a+=i**i
b=str(a)
print(b[len(b)-10:len(b)])
