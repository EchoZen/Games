user_choice= int(input("Scissors(1), Paper(2), Stone(3)?"))
import random
my_choice= random.randint(1,3)
print("my choice:" + str(my_choice))
while my_choice==user_choice:
    print("Tie! Try again!")
    user_choice = int(input("Scissors(1), Paper(2), Stone(3)?"))
    my_choice = random.randint(1, 3)
    print("my choice:" + str(my_choice))

if my_choice-user_choice==1 or my_choice-user_choice==-2:
    print("You win!")
else:
    print("You lose!")
