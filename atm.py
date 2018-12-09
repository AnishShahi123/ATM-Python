balance=500
chances=3
restart=("y")
while(chances>=0):
	print("WELCOME TO AAA BANK")
	pin=int(input("Enter your 4 digit pin no:"))
	if(pin==1234):
		a=int(input("Choose your transaction:\n"
			    "1.Cash Withdraw\n"
			    "2.Cash Deposite\n"
			    "3.Balance Inquiry\n"))
		if(a==1):
			b=int(input("Enter the amount you want to Withdraw:"))
			balance-=b
			print("The total balance in your account is",balance)
			restart=input("Would you like to transit again?")
			if restart in ("n","N"):
				print("Thank you for your transaction\n"
				      "Visit again.\n")
				break
		elif(a==2):
			c=int(input("Enter the amount you want to deposite"))
			balance+=c
			print("The total balance in your account is",balance)
			restart=input("Would you like to transit again?")
			if restart in ("n","N"):
				print("Thank you for your transaction\n"
				      "Visit again....\n")
				break
		elif(a==3):
			print("The total balance in your account is",balance)
			restart=input("Would you like to transit again?")
			if restart in ("n","N"):
				print("Thank you for your transaction\n"
				      "Visit again....\n")
				break
	else:
		print("Please enter a valid pin no.")
		chances=chances-1
		if(chances==0):
			print("NO more tries")
			break













		
































		


