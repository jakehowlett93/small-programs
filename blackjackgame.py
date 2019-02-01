import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  # build Card objects and add them to the list
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:

    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Aces':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 10

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('Choose bet amount: '))
        except ValueError:
            print('The bet amount must be an integer!')            
        else:
            if chips.bet <= 0:
                print('bet must be greater than 0')
            elif chips.bet > chips.total:
                print('Not enough chips!')
            else:
                return chips.bet
            


def hit(deck, hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):

    global playing
    
    while True:

        action = input('hit or stand?: ')
        if action == 'hit':
            print('player hits')
            hit(deck, hand)
            print('----------')
            print('Player has: ', *player_hand.cards, sep='\n ')
            print('Total: ', player_hand.value)
        elif action == 'stand':
            print('player stands')
            playing = False
        else:
            print("Please enter 'hit' or 'stand'")
            continue
        break


def show_some_cards(dealer_hand, player_hand):

    print('----------')
    print('The dealer has: ', dealer_hand.cards[0], sep='\n ')
    print('Total: ', values[dealer_hand.cards[0].rank])
    print('----------')
     #the * symbol is used to print every item in a collection and the sep='\n ' argument prints each item on a new line
    print('Player has: ', *player_hand.cards, sep='\n ')
    print('Total: ', player_hand.value)

def show_all_cards(dealer_hand, player_hand):

    print('----------')
    print('The dealer has: ', *dealer_hand.cards, sep='\n ')
    print('Total: ', dealer_hand.value)
    print('----------')
    print('Player has: ', *player_hand.cards, sep='\n ')
    print('Total: ', player_hand.value)

def player_bust(chips):
    print('Player busts!')
    chips.lose_bet()

def player_win(chips):
    print('Player wins!')
    chips.win_bet()

def dealer_bust(chips):
    print('Dealer busts!')
    print('Player wins!')
    chips.win_bet()
    

def dealer_win(chips):
    print('dealer wins!')
    chips.lose_bet()


player_chips = Chips()

while True:

    playing = True
    game_deck = Deck()
    game_deck.shuffle()
    bet_amount = take_bet(player_chips)
    
    while bet_amount > player_chips.total:
        print('Not enough chips! Please choose a smaller amount.')
    
    player_hand = Hand()
    dealer_hand = Hand()

    dealer_hand.add_card(game_deck.deal())
    player_hand.add_card(game_deck.deal())
    dealer_hand.add_card(game_deck.deal())
    player_hand.add_card(game_deck.deal())
    show_some_cards(dealer_hand, player_hand)

    while playing:
        
        hit_or_stand(game_deck, player_hand)
        if player_hand.value > 21:
            playing = False
    
    show_all_cards(dealer_hand, player_hand)

    while dealer_hand.value < 16:
        dealer_hand.add_card(game_deck.deal())
        
    if player_hand.value > 21:
            player_bust(player_chips)
    elif dealer_hand.value > 21:
        show_all_cards(dealer_hand, player_hand)
        dealer_bust(player_chips)
    elif player_hand.value > dealer_hand.value:
        show_all_cards(dealer_hand, player_hand)
        player_win(player_chips)
    elif player_hand.value == dealer_hand.value:
        show_all_cards(dealer_hand, player_hand)
        print('Push!')
    else:
        show_all_cards(dealer_hand, player_hand)
        dealer_win(player_chips)

    print('player has: ', player_chips.total, ' chips')

    play_again = ''
    while play_again != 'y' and play_again != 'n':
        play_again = input('Play again? (y/n): ')

    if play_again == 'y':
        continue
    else:
        break