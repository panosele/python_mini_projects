import random

aritmoi = ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
sximata = ["karo", "kardia", "mpastouni", "trifili"]


class Card:
    """Class who creates the 52 cards of the class Deck(Colour,shape,number)"""
    def __init__(self, arithmos, sxhma):
        self.arithmos = arithmos
        self.sxhma = sxhma
        if self.sxhma in ["karo", "kardia"]:
            self.xrwma = "red"
        else:
            self.xrwma = "black"

    def __str__(self):
        return f"({str(self.arithmos)}-{self.sxhma})"

    def __add__(self, other):
        if isinstance(other, Card):
            return self.arithmos + other.arithmos
        else:
            return self.arithmos + other


class Deck:
    """Class who creates the Deck of 52 cards with method to shuffle the cards"""
    def __init__(self):
        self.deck = []
        for sxima in sximata:
            for arithmos in aritmoi:
                self.deck.append(Card(arithmos, sxima))

    def __str__(self):
        s = "-".join([str(card) for card in self.deck])
        return s

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, item):
        return self.deck[item]

    def shuffle_deck(self):
        random.shuffle(self.deck)


class PlayerPlay:

    def __init__(self):
        self.hand = []
        self.card_value = 0
        self.wins = 0

    def __str__(self):
        ls = []
        for card in self.hand:
            t = "(" + str(card.arithmos) + "," + card.sxhma + ")"
            ls.append(t)
        return f"Your hand:{'|'.join(ls)}\nYour hands value:{str(self.card_value)}"

    def pop_card_for_player(self, d):
        '''Draw a card from deck, with checking so the card is not drawn.'''
        while True:
            p = random.choice(d)
            if p not in self.hand:
                self.hand.append(p)
                break

    def sum_cards(self):
        """Sums the value of self.deck with card.arithmos--> number on the card
        The 'A' is balander so we check with pr_value the 2 possible hand_values"""
        pr_value = self.card_value
        self.card_value = 0
        for card in self.hand:
            if card.arithmos == "J":
                self.card_value += 10
            elif card.arithmos == "Q":
                self.card_value += 10
            elif card.arithmos == "K":
                self.card_value += 10
            elif card.arithmos == "A":
                if pr_value + 10 > 21:
                    self.card_value += 1
                else:
                    self.card_value += 10
            else:
                self.card_value += card.arithmos

    def continue_to_draw(self, d):
        """The player decides to draw or not. If after the draw exceeds the 21 hand value
        automatically he loses"""
        while True:
            if self.card_value >= 21:
                break

            while True:
                cont = input("Continue(y/n)? :")
                if cont == "y" or cont == "n":
                    break

            if cont == "y":
                self.pop_card_for_player(d)
                self.sum_cards()
                print(self)
            else:
                break


class ComputerPlay:

    def __init__(self):
        self.hand = []
        self.card_value = 0
        self.wins = 0

    def __str__(self):
        ls = []
        for card in self.hand:
            t = "(" + str(card.arithmos) + "," + card.sxhma + ")"
            ls.append(t)
        return f"Computers hand:{'|'.join(ls)}\nComputer value:{str(self.card_value)}"

    def pop_card_for_player(self, d, pl):
        '''Draw a card from deck, with checking so the card is not drawn.'''
        while True:
            p = random.choice(d)
            if p not in self.hand and p not in pl.hand:
                self.hand.append(p)
                break

    def sum_cards(self):
        '''Sums the value of self.deck with card.arithmos--> number on the card
        The 'A' is balander so we check with pr_value the 2 possible hand_values'''
        pr_value = self.card_value
        self.card_value = 0
        for card in self.hand:
            if card.arithmos == "J":
                self.card_value += 10
            elif card.arithmos == "Q":
                self.card_value += 10
            elif card.arithmos == "K":
                self.card_value += 10
            elif card.arithmos == "A":
                if pr_value + 10 > 21:
                    self.card_value += 1
                else:
                    self.card_value += 10
            else:
                self.card_value += card.arithmos

    def continue_to_draw(self, d, p):
        """Computer continues to draw until he wins the player or is burnt(above 21)"""
        while self.card_value < p.card_value:
            self.pop_card_for_player(d, p)
            self.sum_cards()
            if self.card_value >= p.card_value or self.card_value > 21:
                break


def show_rules():
    print("""
    The rules are:
    1. You draw two(2) cards
    2. You decide if you want to continue drawing for more cards
    3. You must not exceed the sum of cards above 21. If you do you lose.
    4. When you decide to stop drawing (without having lost), the computer draws card until it is equal to your sum of cards
       or is above your sum, but less-equal to 21.
    5. The winner is the one with bigger sum (NOTE! the computer wins if there is a Draw)
    6. The 'A' card counts as 10 or 1. The figures 'J'=10, 'Q'=10, 'K'=10.
    """)


def control_menu():
    # Creation of opposite players(objects) and Deck
    player = PlayerPlay()
    comp = ComputerPlay()
    d = Deck()

    while True:
        print("*" * 20)
        print("MENU".center(20))
        print("______".center(20))
        print("1-PLAY")
        print("2-RULES")
        print("3-EXIT")
        print("*" * 20)

        menu_choice = input("What's your choice(1-2-3)? :").strip()

        if menu_choice.isdigit():
            menu_choice = int(menu_choice)
            if menu_choice == 1 or menu_choice == 2 or menu_choice == 3:
                pass
            else:
                print("You inserted wrong number!")
        else:
            print("Wrong Input! TRY AGAIN!")

        if menu_choice == 3:
            exit()
        elif menu_choice == 2:
            show_rules()
        else:
            d.shuffle_deck()
            # we set the values to 0 for next round
            player.card_value = 0
            player.hand = []
            comp.card_value = 0
            comp.hand = []
            # player drops 2 card and he/she sees them on the screen
            player.pop_card_for_player(d)
            player.pop_card_for_player(d)
            player.sum_cards()
            print(player)
            # player is going to choose to continue drawing or not
            player.continue_to_draw(d)
            # if players hand is > 21 ...he looses
            if player.card_value > 21:
                print("You LOST!")
                comp.wins += 1
            else:  # if players hand is <= 21 computer plays
                comp.continue_to_draw(d, player)
                print(player)
                print(comp)
                # here is the decision of WINNER
                if player.card_value > comp.card_value or comp.card_value > 21:
                    print("You WIN!")
                    player.wins += 1
                else:
                    print("You LOST!")
                    comp.wins += 1

            print("*" * 20)
            print(f"Total Games:{player.wins+comp.wins}|PLAYER:{player.wins}-PC:{comp.wins}")
            print("*" * 20)


control_menu()

