class Card:
    """Represents a single playing card in Tichu."""
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    """Represents a deck of cards used in Tichu, including special cards."""
    def __init__(self):
        self.cards = [Card(value, suit) for value in range(2, 15)  # 2-10, J, Q, K, A
                      for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']]
        # Adding special cards: Dragon(용용), Phoenix(봉봉), Dog(개), Mahjong (1)
        self.cards.extend([Card('용용', 'Special'),
                           Card('봉봉', '-50'),
                           Card('멍멍', 'Special'),
                           Card('짹짹', '1')])

    def shuffle(self):
        """Shuffles the deck."""
        import random
        random.shuffle(self.cards)

    def deal(self, num_players):
        """Deals cards to players."""
        hands = {i: [] for i in range(num_players)}
        for i in range(len(self.cards)):
            hands[i % num_players].append(self.cards[i])
        return hands

class Player:
    """Represents a player in the game."""
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_cards(self, cards):
        """Receives a hand of cards."""
        self.hand = cards

    def play_cards(self):
        """Placeholder for playing cards."""
        pass  # To be implemented: logic for playing cards

class TichuGame:
    """Represents a game of Tichu."""
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]

    def start_game(self):
        """Starts the Tichu game."""
        self.deck.shuffle()
        hands = self.deck.deal(len(self.players))
        for i, player in enumerate(self.players):
            player.receive_cards(hands[i])

# Example usage
game = TichuGame(["김", "박", "류", "조"])
game.start_game()

# Display initial hands (for demonstration purposes)
for player in game.players:
    print(f"{player.name}'s hand: {player.hand}")
