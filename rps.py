import random
rock = '''
        _________
_______'     ____)
            (_____)
            (______)
_______     (_____)
        '___(____)

'''
paper = '''
        _________
_______'     ____)____
                 _____)__
            _____________)
_______     __________)
        '___________)

'''
scissors = '''
        _________
_______'     ____)_____
             __________)
             ____________)
_______     (_____)
        '___(____)

'''
rpc = [rock, paper, scissors]
user_inp = int(input("What do you choose? \nType 0 for Rock \nType 1 for Paper \nType 2 for Scissor \n"))
print(rpc[user_inp])
comp_inp = random.randint(0, 2)
print(f"Computer choose {comp_inp}")
print(rpc[comp_inp])

if user_inp >= 3 or user_inp < 0:
    print("You enter invalid number")
elif user_inp == comp_inp:
    print("Match Draw")
elif user_inp < comp_inp:  # use = 0 and comp = 1
    print("Oops, You loose the match!!")
elif user_inp == 0 and comp_inp == 2:
    print("!!! Hurray, You won the match !!")
elif user_inp > comp_inp:   # user = 1 nd comp = 0
    print("!!! Hurray, You won the match !!")
elif user_inp == 2 and comp_inp == 0:
    print("Oops, You loose the match!!")
