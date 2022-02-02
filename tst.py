n=5
for i in range(n,0,-1):
	if i==n:
		print("*"*(n*2-1))
	else:
		print(" "*(n-i),end="")
		for j in range(1,2*i):
			if j==1 or j==2*i-1:
				print("*",end="")
			else:
				print(" ",end="")
		print()
	