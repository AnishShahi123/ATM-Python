import random
import time
min=1
max=6
roll="yes"
while(roll=="yes" or roll=="y"):
	print("The dice is rolling.....")
	time.sleep(1)
	print("The value in dice is...")
	time.sleep(1)
	print(random.randint(min,max))
	roll=input("Do you want to roll again?")


