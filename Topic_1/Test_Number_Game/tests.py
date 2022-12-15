import unittest
import Topic_1.Number_Game.numberguesser as n

class GameTest (unittest.TestCase):
    def setUp(self):
        self.Game = n.NumberGuesser()

    def tearDown(self):
        del self.Game

    def testConstructor(self):
        self.assertEqual(self.Game.randomNum, 0)
        self.assertEqual(len(self.Game.guessed_list), 0)

    def test_guess_1(self):
        self.Game.Guess_1()
        self.assertIn(1, self.Game.guessed_list)

    def test_guess_2(self):
        self.Game.Guess_2()
        self.assertIn(2, self.Game.guessed_list)

    def test_guess_3(self):
        self.Game.Guess_3()
        self.assertIn(3, self.Game.guessed_list)

    def test_guess_4(self):
        self.Game.Guess_4()
        self.assertIn(4, self.Game.guessed_list)

    def test_guess_5(self):
        self.Game.Guess_5()
        self.assertIn(5, self.Game.guessed_list)

    def test_guess_6(self):
        self.Game.Guess_6()
        self.assertIn(6, self.Game.guessed_list)

    def test_guess_7(self):
        self.Game.Guess_7()
        self.assertIn(7, self.Game.guessed_list)

    def test_guess_8(self):
        self.Game.Guess_8()
        self.assertIn(8, self.Game.guessed_list)

    def test_guess_9(self):
        self.Game.Guess_9()
        self.assertIn(9, self.Game.guessed_list)

    def test_guess_10(self):
        self.Game.Guess_10()
        self.assertIn(10, self.Game.guessed_list)

    def test_reset(self):
        self.Game.Guess_4()
        self.assertIn(4, self.Game.guessed_list)
        self.Game.ResetGame()
        self.assertNotIn(4, self.Game.guessed_list)
