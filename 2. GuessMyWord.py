secretword= "Lightbulb"
guess= ""
tries= 0
max_try=5
outofguesses= False
#Code will loop as long as they haven't guessed the word and are not out of guesses
while guess!=secretword and not(outofguesses):
    #Check if they have guesses left
    if tries<max_try:
        guess= input("Enter guess:")
    else:
        outofguesses= True
    tries= tries+1

if outofguesses:
    print("You lost!")
else:
    print("You won with", tries, " tries")
