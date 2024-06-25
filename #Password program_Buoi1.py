#Password program


l, u, p, d = 0, 0, 0, 0
s = input("Set your new password: ")

capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets="abcdefghijklmnopqrstuvwxyz"
specialchar="$@_"
digits="0123456789"
if (len(s) >= 8):
	for i in s:

		# counting lowercase alphabets
		if (i in smallalphabets):
			l+=1		

		# counting uppercase alphabets
		if (i in capitalalphabets):
			u+=1		

		# counting digits
		if (i in digits):
			d+=1		

		# counting the mentioned special characters
		if(i in specialchar):
			p+=1	
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
	print("Valid Password")
else:
	print("Invalid Password")

available = 0
while (available < 5):
	available +=1

	check = input("Enter your password: ")
	k=0
	if (len(s)==len(check)):
		k = 0
		while(k < len(check)):
			if check[k] != s[k]:
				#print(check[k])
				break
			else:
				#print(check[k])
				k+=1
		if k == len(s):
			print("You are loggged in to the system.")
			break		

print("The system is about to explode!!!")

