a=[]
s=[]
r=[]
i=[]
n=int(input('no of elements? \n'))
for x in range(0,n):
	a.append(input())
for x in a:
	if x not in s:
		s.append(x)
	else:
		r.append(x)
for x in s:
	if x not in r:
		i.append(x)
print (i)
