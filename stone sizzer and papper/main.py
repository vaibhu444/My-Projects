import random
c=0
u=0
l=1
dra=0
while(l<11):
	print("---------------------------------------------------------")
	print("1.Stone\n2.Sizzer\n3.Paper")
	print("---------------------------------------------------------")
	n=int(input("Enter your choice"))
	list=["stone","sizzer","paper"]
	r=random.choice(list)
	if n==1:
		for i in range(3):
			for j in range(3):
				if  n==(i+1)  and r==list[j]:
					print(r)
					print("match draw")
					dra+=1
	if n==2:
		for i in range(3):
			for j in range(3):
				if  n==(i+1)  and r==list[j]:
					print(r)
					print("You lose")
					c+=1
	if n==3:
		for i in range(3):
			for j in range(3):
				if  n==(i+1) and r==list[j]:
					print(r)
					print("You win")
					u+=1
	l+=1
print("---------------------------------------------------------")
print("Computer  : ",c)
print("user  : ",u)
print("match draw  : ",dra)
print("---------------------------------------------------------")
