def IsPrime():
	n=7
	if n<=1:
		flag=1
	if n==2 or n==3:
		flag=0
	if n%2==0 or n%3==0:
		flag=1
	i=5
	while i*i <= n:
		if (n%i==0 or n%(i+2)==0):
			flag=1
		i=i+6
	flag=0

	if(flag==0):
		return "Yes"
	else:
		return "No"




		
	