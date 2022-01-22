import random

x= int(input(" enter 0 to roll "))

while(x==0):

 if(x==0):
     y= int(random.randint(1,6))
     print ("______\n|     |\n| ",y," |\n|_____|")
     x= int(input(" enter 0 to roll "))
