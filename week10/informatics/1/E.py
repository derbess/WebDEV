v,t = int(input()),int(input())
l=abs(v*t)

if l%109==0: 
	print(0)
elif v<0:
	print(109-(l%109))
else: 
	print(l%109)

