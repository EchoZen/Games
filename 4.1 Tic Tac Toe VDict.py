import random
print("Let's play tic tac toe!")
tictac={"Top-L":" ", "Top-M":" ", "Top-R":" ",
        "Mid-L":" ", "Mid-M":" ", "Mid-R":" ",
        "Bot-L":" ", "Bot-M":" ", "Bot-R":" "}

windict= {}

def tic_tac(tictac):
    print(tictac["Top-L"]+"|"+tictac["Top-M"]+"|"+tictac["Top-R"]+"|")
    print("------")
    print(tictac["Mid-L"]+"|"+tictac["Mid-M"]+"|"+tictac["Mid-R"]+"|")
    print("------")
    print(tictac["Bot-L"]+"|"+tictac["Bot-M"]+"|"+tictac["Bot-R"]+"|")


tic_tac(tictac)
x_o= input("Do you want to be X or O?").upper()
if x_o=="X":
    cp="O"
else:
    cp="X"

notWin= True
question = ['Top-L', 'Top-M', 'Top-R',
'Mid-L', 'Mid-M', 'Mid-R',
'Bot-L', 'Bot-M', 'Bot-R']
user_inputs= ''
cp_inputs= ''
while notWin:
    invalid_input= True
    print("Where do you want to play?")
    user= input(question)
    if user in question:
        invalid_input= False
    while invalid_input: #Will keep asking until user adds a valid input
        if user not in question:
            print("Invalid input. Try again.")
            user = input(question)
        else:
            invalid_input= False

    tictac[user]=x_o
    question.remove(user) #Removes user choices
    user_inputs += user +"-"
    #Determine win or lose
    user_inputList= user_inputs.split("-")
    print(user_inputs)
    windict["top"]= user_inputList.count("Top")
    windict["mid"]= user_inputList.count("Mid")
    windict["bot"]= user_inputList.count("Bot")
    windict["left"]= user_inputList.count("L")
    windict["middle"] = user_inputList.count("M")
    windict["right"]= user_inputList.count("R")
    if 3 in windict.values():
        tic_tac(tictac)
        notWin= False
        break
    elif "Top-L" in user_inputs and "Mid-M" in user_inputs and "Bot-R" in user_inputs:
        tic_tac(tictac)
        notWin= False
        break
    elif "Top-R" in user_inputs and "Mid-M" in user_inputs and "Bot-L" in user_inputs:
        tic_tac(tictac)
        notWin= False
        break
    else:
        windict.clear()
    # For now its easy mode. Will code a separate function for computer to decide how to win
    computer= random.choice(question)
    tictac[computer]= cp
    question.remove(computer)
    cp_inputs += computer+ "-"
    cp_inputList= cp_inputs.split("-")
    windict["top"]= cp_inputList.count("Top")
    windict["mid"]= cp_inputList.count("Mid")
    windict["bot"]= cp_inputList.count("Bot")
    windict["left"]= cp_inputList.count("L")
    windict["middle"]= cp_inputList.count("M")
    windict["right"]= cp_inputList.count("R")
    if 3 in windict.values():
        tic_tac(tictac)
        break
    elif "Top-L" in cp_inputs and "Mid-M" in cp_inputs and "Bot-R" in cp_inputs:
        tic_tac(tictac)
        break
    elif "Top-R" in cp_inputs and "Mid-M" in cp_inputs and "Bot-L" in cp_inputs:
        tic_tac(tictac)
        break
    else:
        windict.clear()
    tic_tac(tictac)

if notWin== False:
    print("Congratulations! You won the game!")
else:
    print("Too bad, you lost. Better luck next time!")
