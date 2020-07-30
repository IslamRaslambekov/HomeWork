import pytest
from Lesson10.fool_game import Fool


class Test_Lesson9_fool:
    def setUp(self):
        self.fool = Fool()

    def tearDown(self):
        pass

    def test_deck_lenght(self):
        assert len(self.fool.deck) == 36

    def test_on_hand(self):
        self.fool.on_hand()
        assert len(self.fool.player_deck) == 6
        assert len(self.fool.player_deck) == len(self.fool.computer_deck)

    def test_cut_str(self):
        check = self.fool.cut_str("[('♠10', 10)]")
        assert check == '♠10'

