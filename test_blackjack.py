import unittest
from unittest.mock import patch, MagicMock

from card import Deck, Card, Hand
from blackjack import BlackJack

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_initialization(self):
        self.assertEqual(len(self.deck.cards), 52)
    
    def test_deck_shuffle(self):
        original = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(original, self.deck.cards)
    
    def test_deck_deal(self):
        card = self.deck.deal()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(self.deck.cards), 51)

class TestHand(unittest.TestCase):
    def setUp(self):
        self.hand = Hand("Manasha")
    
    def test_initial(self):
        v = self.hand.value
        self.assertEqual(v, 0)
        self.assertEqual(len(self.hand.cards), 0)

    def test_add_card(self):
        card = Card(2, "Hearts")
        self.hand.addCard(card)
        self.assertEqual(len(self.hand.cards), 1)
        self.assertEqual(self.hand.getValue(), 2)

class TestBlackJack(unittest.TestCase):

    @patch('builtins.input', side_effect=["Player", "H", "S"])
    def test_blackjack_game(self, mock_input):
        """Test the full game flow with mocked inputs"""
        game = BlackJack()  # Mocked name input as "Player"
        game.dealInitial()

        # Mock "Hit" and then "Stand" during playerPlay
        with patch('builtins.print') as mock_print:
            game.game()
            # Assert final result prints
            mock_print.assert_any_call("Final Results:")

    @patch('builtins.input', side_effect=["Player"])
    def test_blackjack_initialization(self, mock_input):
        """Test game initialization with mocked name input"""
        game = BlackJack()
        self.assertEqual(game.player_hand.name, "Player")
        self.assertEqual(game.dealer_hand.name, "Dealer")
    
    @patch('builtins.input', side_effect=["Player"])
    def test_player_wins(self, mock_input):
        game = BlackJack()
        game.player_hand.getValue = MagicMock(return_value = 20)
        game.dealer_hand.getValue = MagicMock(return_value=18)

        with patch('builtins.print') as mock_print:
            game.winner()
            you_win_present = any("You Win" in call.args[0] for call in mock_print.call_args_list)
            self.assertTrue(you_win_present, "You Win was not in answer")
    
    @patch('builtins.input', side_effect=["Player"])
    def test_player_wins(self, mock_input):
        game = BlackJack()
        game.player_hand.getValue = MagicMock(return_value = 18)
        game.dealer_hand.getValue = MagicMock(return_value=20)

        with patch('builtins.print') as mock_print:
            game.winner()
            you_win_present = any("Dealer Wins" in call.args[0] for call in mock_print.call_args_list)
            self.assertTrue(you_win_present, "Dealer Wins was not in answer")
        

if __name__ == '__main__':
    unittest.main()