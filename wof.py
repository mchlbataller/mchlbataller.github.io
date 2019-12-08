from IPython.display import clear_output

## BEFORE GUI ###############################################################
# Uncomment prints, players, and phrases
#print("Input Player 1: ")
#player1 = (input())
#print("Input Player 2: ")
#player2 = (input())

#phrase1 = str(input("First phrase: ")).upper()
#for letter in phrase1:
    #phrase1_list.append(letter)
    
#phrase2 = str(input("Second phrase: ")).upper()
#for letter in phrase2:
    #phrase2_list.append(letter)
    
#phrase3 = str(input("Thirds phrase: ")).upper()
#for letter in phrase3:
    #phrase3_list.append(letter)

player1 = "Michael"
player2 = "Test"
phrase1 = str("nice onee").upper()
phrase2 = str("merry christmas").upper()
phrase3 = str("hello world").upper()


## IMPORT STATEMENTS ############################################
from tkinter import *
import random


## CLASS DEFINITIONS ############################################
    
class Player_Info:
    def __init__(self, name):
        self.totalMoney = 0
        self.roundMoney = 0
        self.player = name

    def getPlayerName(self):
        return self.player

    def getPrizePool(self):
        return self.PrizePool
    

    def action1(self):
        self.PrizePool += amount
        return "Transaction Complete"

class Wheel_of_Fortune:
    def __init__(self, phrase):
        self.money_Prizes = ["BANKRUPT",500,550,600,650,700,750,800,850,2500]
        self.money_Prizes_2x = ["BANKRUPT",1000,1100,1200,1300,1400,1500,1600,1700,5000]
        self.unused_Consonants = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
        self.unused_Vowels = ['A','E','I','O','U']
        self.vowel_Cost = 250
        self.turn = 1
        self.round = 1
        self.phrase = phrase
        self.active_player = 0
        self.dashed_string = ""
        self.prize = ''
    
    def phrase_Dash(self):
        dashed_list = []
        for char in self.phrase:
            if char in self.unused_Vowels or char in self.unused_Consonants:
                dashed_list.append("-")
            elif char == " ":
                dashed_list.append(" ")
            elif char not in self.unused_Consonants and char not in self.unused_Vowels:
                dashed_list.append(char)
        self.dashed_string = "".join(dashed_list)

    def player_Active(self):
        if self.playerActive == 0:
            self.playerActive = 1
        else:
            self.playerActive = 0
    
    def spin_Wheel(self):
        x = random.randint(0,9)
        wheel = self.money_Prizes[x]
        self.prize = wheel
    
    
## FUNCTION DEFINITIONS #########################################
    
def confirm_Action():
    if actionVar.get() == 1:
        action_frame.grid_remove()
        action1_frame.grid(row=1, column=0)
        Wheel_of_Fortune.spin_Wheel() 
        # Dev Doc:
        # configure alters the already set grid options
        label_your_roll.configure(text = "You rolled: " + str(Wheel_of_Fortune.prize))
    elif actionVar.get() == 2:
        action_frame.grid_remove()
        action2_frame.grid(row=1, column=0)
    elif actionVar.get() == 3:
        action_frame.grid_remove()
        action3_frame.grid(row=1, column=0)    
            
def buy_Vowel():
    action2_frame.grid_remove()
    action_frame.grid(row=1, column=0)

def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

def pick_Consonant(results):
    for i in range(len(phrase1)):
        entry = entry_chooseConsonant.get()
        results.append(phrase1.find(str(entry), i))
        
    print(results)

    if results > 0:
        for i in results:
            Wheel_of_Fortune.dashed_string = replacer(Wheel_of_Fortune.dashed_string, entry_chooseConsonant.get(), i)

    action1_frame.grid_remove()
    action_frame.grid(row=1, column=0)


    

    
## APPLICATION PROPER ###########################################

# OBJECT CALLING ########
Wheel_of_Fortune = Wheel_of_Fortune(phrase1)

Player_Info1 = Player_Info(player1)
Player_Info2 = Player_Info(player2)


Wheel_of_Fortune.phrase_Dash()
print(Wheel_of_Fortune.dashed_string)

# CREATING WINDOW ######

window = Tk()
window.title('Wheel of Fortune')
window.geometry('1000x500')

# TABLE ################
table_frame = Frame(window, bd=1, relief=SUNKEN)
table_frame.grid(row=0, column=0, columnspan=2)

# Column 1
label_players = Label(table_frame, text="Players", relief=SUNKEN)
label_players.grid(row=0, column=0)
label_player1 = Label(table_frame, text = Player_Info1.player)
label_player1.grid(row=1,column=0)
label_player2 = Label(table_frame, text = Player_Info2.player)
label_player2.grid(row=2,column=0)

# Column 2
label_active = Label(table_frame, text="Active", relief=SUNKEN)
label_active.grid(row=0, column=1)
label_active1 = Label(table_frame, text="*")
label_active1.grid(row=1, column=1)

# Column 3
label_roundMoney = Label(table_frame, text="Round Money", relief=SUNKEN)
label_roundMoney.grid(row=0, column=2)
lable_roundMoney_player1 = Label(table_frame, text="Round Money")
lable_roundMoney_player1.grid(row=1, column=2)
lable_roundMoney_player2 = Label(table_frame, text="Round Money")
lable_roundMoney_player2.grid(row=2, column=2)

# Column 4
label_totalMoney = Label(table_frame, text="Total Money", relief=SUNKEN)
label_totalMoney.grid(row=0, column=3)
lable_totalMoney_player1 = Label(table_frame, text=str(Player_Info1.totalMoney))
lable_totalMoney_player1.grid(row=1, column=3)
lable_totalMoney_player2 = Label(table_frame, text=str(Player_Info1.totalMoney))
lable_totalMoney_player2.grid(row=2, column=3)



# ACTIONS ##############
action_frame = Frame(window, bd=2, relief=RIDGE)
action_frame.grid(row=1, column=0)

# Action Select
actionVar = IntVar(window)
actionVar.set(1)

label_action = Label(action_frame, text="Actions:")
label_action.grid(row=0, column=0, sticky=W)
label_action1 = Label(action_frame, text="1) Spin Wheel & Pick Consonant")
label_action1.grid(row=1, column=0, sticky=W)
label_action2 = Label(action_frame, text="2) Buy a Vowel for 250")
label_action2.grid(row=2, column=0, sticky=W)
label_action3 = Label(action_frame, text="3) Guess the Phrase")
label_action3.grid(row=3, column=0, sticky=W)

space_row = Label(action_frame, text=" ")
space_row.grid(row=4, column=0)

label_chooseAction = Label(action_frame, text="Choose Action: ")
label_chooseAction.grid(row=5, column=0, sticky=E)
OptionMenu_chooseAction = OptionMenu(action_frame, actionVar, 1,2,3)
OptionMenu_chooseAction.grid(row=5, column=1, sticky=W)
button_chooseAction = Button(action_frame, text="Confirm", command=confirm_Action)
button_chooseAction.grid(row=6, column=1, sticky=W)

# Action 1
action1_frame = Frame(window, bd=2, relief=RIDGE)

label_action = Label(action1_frame, text="Actions:")
label_action.grid(row=0, column=0, sticky=W)

label_action1 = Label(action1_frame, text="1) Spin Wheel & Pick Consonant")
label_action1.grid(row=1, column=0, sticky=W)

label_your_roll = Label(action1_frame, text="You rolled")
label_your_roll.grid(row=2, column=0, sticky=W)

label_chooseConsonant = Label(action1_frame, text="Pick Consonant:")
label_chooseConsonant.grid(row=3, column=0, sticky=E)

entry_chooseConsonant = Entry(action1_frame)
entry_chooseConsonant.grid(row=3, column=1, sticky=W)

# Initialize a new array which returns the character positions
results = []

button_chooseConsonant = Button(action1_frame, text="Choose", command=pick_Consonant(results))
button_chooseConsonant.grid(row=4, column=1, sticky=W)


# Action 2
action2_frame = Frame(window, bd=2, relief=RIDGE)

label_action = Label(action2_frame, text="Actions:")
label_action.grid(row=0, column=0, sticky=W)

label_action2 = Label(action2_frame, text="2) Buy a Vowel")
label_action2.grid(row=1, column=0, sticky=W)

label_vowelCost = Label(action2_frame, text="Vowel costs 250")
label_vowelCost.grid(row=2, column=0, sticky=W)

label_buyVowel = Label(action2_frame, text="Buy Vowel: ")
label_buyVowel.grid(row=3, column=0, sticky=E)

entry_buyVowel = Entry(action2_frame)
entry_buyVowel.grid(row=3, column=1, sticky=W)

button_buyVowel = Button(action2_frame, text="Choose", comman=buy_Vowel)
button_buyVowel.grid(row=4, column=1, sticky=W)

# Action 3
action3_frame = Frame(window, bd=2, relief=RIDGE)

label_action = Label(action3_frame, text="Actions:")
label_action.grid(row=0, column=0, sticky=W)

label_action3 = Label(action3_frame, text="3) Guess the Phrase")
label_action3.grid(row=1, column=0, sticky=W)

label_guessThePhrase = Label(action3_frame, text="Guess the phrase, risk ending your turn.")
label_guessThePhrase.grid(row=2, column=0, sticky=W)

label_phrase = Label(action3_frame, text="Phrase: ")
label_phrase.grid(row=3, column=0, sticky=E)

entry_phrase = Entry(action3_frame)
entry_phrase.grid(row=3, column=1, sticky=W)

button_guess = Button(action3_frame, text="Guess")
button_guess.grid(row=4, column=1, sticky=W)


# INFORMATION ##########
info_frame = Frame(window, bd=2, relief=RIDGE)
info_frame.grid(row=1, column=1)

label_round = Label(info_frame, text="Round:")
label_round.grid(row=0, column=0, sticky=W)
label_dashPhrase = Label(info_frame, text="Phrase: " + Wheel_of_Fortune.dashed_string)
label_dashPhrase.grid(row=1, column=0, sticky=W)
label_turnsInRound = Label(info_frame, text="Turns:")
label_turnsInRound.grid(row=2, column=0, sticky=W)

space_row = Label(info_frame, text=" ")
space_row.grid(row=3, column=0)

label_unusedConsonants = Label(info_frame, text="Unused Consonants:")
label_unusedConsonants.grid(row=4, column=0, sticky=W)
label_unusedVowels = Label(info_frame, text="Unused Vowels:")
label_unusedVowels.grid(row=5, column=0, sticky=W)

## MAIN LOOP (LAST) #############################################
window.mainloop()