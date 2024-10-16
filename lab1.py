import random


number= random.randit (1,10)
attempts= 3
count= 1


while count<= attempt:
   guess=(int(input("Guess a number between 1-19: ")))
  
   if guess > number:
       print("Too high")
   elif guess < number:
       print("Too low")
   else:
       print("Correct")
       break
   count += 1


if count > attempts:
   print("Sorry, you're used all your attempts. The number was {number}"