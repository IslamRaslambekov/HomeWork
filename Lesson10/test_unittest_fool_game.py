import unittest
from Lesson10.fool_game import Fool


class Test_Lesson9_fool(unittest.TestCase):
    def setUp(self):
        self.fool = Fool()

    def tearDown(self):
        pass

    # def test_deck_lenght(self):
    #     self.assertEqual(len(self.fool.deck), 36)

    def test_on_hand(self):
        self.fool.on_hand()
        self.assertEqual(len(self.fool.player_deck), 6)
        self.assertEqual(len(self.fool.player_deck), len(self.fool.computer_deck))

    def test_cut_str(self):
        check = self.fool.cut_str("[('♠10', 10)]")
        self.assertEqual(check, '♠10')

    def test_add_cards(self):
        some_list = ['1', '2', '3']
        new_list = self.fool.add_cards(some_list)
        self.assertEqual(len(new_list), 6)
