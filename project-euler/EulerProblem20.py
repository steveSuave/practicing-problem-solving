def fac(x):
	if x==1:
		return 1
	else:
		return x*fac(x-1)

a=fac(100)
b=str(a)
c=b[:]
d=[int(i) for i in c]
print(sum(d))
