from card import Deck, Hand

class BlackJack():
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        print("Welcome to BlackJack!")
        name = input("What is your name: ")
        self.player_hand = Hand(name)
        self.dealer_hand = Hand("Dealer")
    
    def dealInitial(self):
        self.player_hand.addCard(self.deck.deal())
        self.dealer_hand.addCard(self.deck.deal())

    #player 1 is player, 2 is dealer
    def displayCards(self, player):
        if player == 1:
            print(str(self.player_hand))
        else:
            print(str(self.dealer_hand))
    
    def dealerPlay(self):
        while self.dealer_hand.getValue() < 17:
            self.dealer_hand.addCard(self.deck.deal())

    def playerPlay(self):
        while True:
            if self.player_hand.getValue() > 21:
                print("Oh no. You went above 21. Dealer Wins :(")
                return False
            play = input("Would you like to (H)it or (S)tand: ")
            if play == "S":
                break
            elif play == 'H':
                self.player_hand.addCard(self.deck.deal())
                self.displayCards(1)
            else:
                print("Invalid Input!")
        return True
    
    def winner(self):
        playerTotal = self.player_hand.getValue()
        dealerTotal = self.dealer_hand.getValue()
        print("Final Results:")
        self.displayCards(1)
        self.displayCards(2)

        if dealerTotal > 21 or playerTotal > dealerTotal:
            print("You Win")
        elif playerTotal < dealerTotal:
            print("Dealer Wins")   
        else:
            print("It's a tie")


    
    def game(self):
        self.dealInitial()
        self.displayCards(1)
        self.displayCards(2)
        
        if self.playerPlay():
            self.dealerPlay()
            self.winner()



