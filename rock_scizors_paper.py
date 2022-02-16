from random import choice

# globals
ls_choices = ["rock", "scissors", "paper"]


# functions
def pc_play(ls):
    return choice(ls)


def menu_for_play():
    while True:
        print("*" * 15)
        print("****Player choice****")
        print("1-for rock")
        print("2-for scissors")
        print("3-for paper")
        player_ch = (input("What's your choice?:")).strip()
        if player_ch.isdigit():
            player_ch = int(player_ch)
            if 1 <= player_ch <= 3:
                if player_ch == 1:
                    player_ch = "rock"
                elif player_ch == 2:
                    player_ch = "scissors"
                else:
                    player_ch = "paper"
                return player_ch
            else:
                print("Wrong input\n1 or 2 or 3 please!")
        else:
            print("Wrong input. Please try again!")


def who_is_winner(pc_choice, pl_choice, ls):  # You can change the conditions with 1-3 and list indexes+1.
    if pc_choice == pl_choice:
        print(f"PC    :{pc_choice}\nPLAYER:{pl_choice}\n***DRAW!***")
        print("TRY AGAIN!")
        pc_choice = pc_play(ls)
        pl_choice = menu_for_play()
        who_is_winner(pc_choice, pl_choice, ls)
    elif pc_choice == "rock":
        if pl_choice == "scissors":
            print(f"PC    :{pc_choice}\nPLAYER:{pl_choice}\n***PC WINS!***")
        else:
            print(f"PC    :{pc_choice}\nPLAYER:{pl_choice}\n***PLAYER WINS!***")
    elif pc_choice == "scissors":
        if pl_choice == "paper":
            print(f"PC    :{pc_choice}\nPLAYER:{pl_choice}\n***PC WINS!***")
        else:
            print(f"PC    :{pc_choice}\nPLAYER:{pl_choice}\n***PLAYER WINS!***")
    else:  # pc_choice == "paper"
        if pl_choice == "rock":
            print(f"PC    :{pc_choice}\nPLAYER:{pl_choice}\n***PC WINS!***")
        else:
            print(f"PC    :{pc_choice}\nPLAYER:{pl_choice}\n***PLAYER WINS!***")


def read_rules():
    print("*" * 30)
    print('''Hello Player, if you are new to this game here are the simple rules:
    You make a choice between these 3:
    1-Rock
    2-Scissors
    3-Paper
    The computer makes its choice.
    -The rock beats the scissors and loses from paper
    -The scissors beats the paper and loses from rock
    -The paper beats the rock and loses from scissors
    If you pick tha same you play again, untill someone wins.
    ENJOY THE GAME!''')
    print("*" * 30)


def menu():
    comp_choice = pc_play(ls_choices)
    player_choice = menu_for_play()
    who_is_winner(comp_choice, player_choice, ls_choices)


def main():
    while True:
        print("*" * 15)
        print("***MENU***")
        print("1-PLAY")
        print("2-EXIT")
        print("3-GAME RULES")
        action = (input("Press 1(for play) or 2(for exit) or 3(for rules):")).strip()
        if action.isdigit():
            action = int(action)
            if action == 1:
                menu()
            elif action == 2:
                print("*" * 15)
                print("EXIT COMPLETED!")
                exit()
            elif action == 3:
                read_rules()
            else:
                print("Wrong Input! Try 1 or 2 or 3.")
        else:
            print("Wrong Input! Please Try Again.")

# main
main()