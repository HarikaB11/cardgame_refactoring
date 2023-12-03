from random import shuffle
class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            return self.suit < other.suit
        return False
    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            return self.suit > other.suit
        return False
    def __repr__(self):
        return f"{self.values[self.value]} of {self.suits[self.suit]}"
class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for value in range(2, 15) for suit in range(4)]
        shuffle(self.cards)
    def rm_card(self):
        return self.cards.pop() if self.cards else None
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name
class Game:
    def __init__(self):
        self.deck = Deck()
        self.p1 = Player(input("Player 1 name: "))
        self.p2 = Player(input("Player 2 name: "))
    def wins(self, winner):
        print(f"{winner} wins this round")
    def draw(self, p1, p1_card, p2, p2_card):
        print(f"{p1} drew {p1_card} | {p2} drew {p2_card}")
    def play_game(self):
        cards = self.deck.cards
        print("Beginning War!")
        while len(cards) >= 2:
            response = input("Press 'q' to quit. Any other key to play: ")
            if response == 'q':
                break
            p1_card = self.deck.rm_card()
            p2_card = self.deck.rm_card()
            self.draw(self.p1.name, p1_card, self.p2.name, p2_card)
            if p1_card > p2_card:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        winner_name = self.winner(self.p1, self.p2)
        print(f"War is over. {winner_name} wins")
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"
if __name__ == "__main__":
    game = Game()
    game.play_game()
