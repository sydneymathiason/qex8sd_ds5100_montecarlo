import unittest
import numpy as np
import pandas as pd
from montecarlo.montecarlo import Die, Game, Analyzer

class TestDie(unittest.TestCase):
    def test_d__init__(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        self.assertEqual(len(die.faces), 6)
        
    def test_change_weight(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        die.change_weight(1, 0.5)
        self.assertEqual(die.show_state().loc[1, "weights"], 0.5)

    def test_roll(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        outcomes = die.roll_die(10)
        self.assertEqual(len(outcomes), 10)
    
    def test_show_state(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        self.assertIsInstance(die.show_state(), pd.DataFrame)

    def setUp(self):
        faces1 = np.array([1, 2, 3, 4, 5, 6])
        faces2 = np.array(["H", "T"])
        self.die1 = Die(faces1)
        self.die2 = Die(faces2)
        self.game1 = Game([self.die1, self.die1])
        self.game2 = Game([self.die1, self.die2, self.die2])
        self.analyzer1 = Analyzer(self.game1)
        self.analyzer2 = Analyzer(self.game2)
        
    def test_g__init__(self):
        self.game1.play(10)
        self.assertIsInstance(self.game1._dice, list)
        
        self.game2.play(10)
        self.assertIsInstance(self.game2._dice, list)
    
    def test_play(self):
        self.game1.play(10)
        self.assertEqual(self.game1._play_data.index.name, "roll_number")
        
        self.game2.play(10)
        self.assertEqual(self.game2._play_data.index.name, "roll_number")
        
    def test_show_results(self):
        self.game1.play(10)
        self.assertEqual(self.game1.show_result(dftype="wide").shape, (10, 2))
        
        self.game2.play(10)
        self.assertEqual(self.game2.show_result(dftype="narrow").shape, (30, 1))
        
    def test_a__init__(self):
        self.game1.play(100)
        self.assertIsInstance(self.analyzer1._game, Game)

        self.game2.play(100)
        self.assertIsInstance(self.analyzer2._game, Game)

    def test_jackpot(self):
        self.game1.play(100)
        self.assertIsInstance(self.analyzer1.jackpot(), int)

        self.game2.play(100)
        self.assertIsInstance(self.analyzer2.jackpot(), int)

    def test_face_counts_per_roll(self):
        self.game1.play(100)
        self.assertIsInstance(self.analyzer1.face_counts(), pd.DataFrame)

        self.game2.play(100)
        self.assertIsInstance(self.analyzer2.face_counts(), pd.DataFrame)

    def test_combo_count(self):
        self.game1.play(100)
        self.assertIsInstance(self.analyzer1.combo_count(), pd.DataFrame)

        self.game2.play(100)
        self.assertIsInstance(self.analyzer2.combo_count(), pd.DataFrame)

    def test_permutation_count(self):
        self.game1.play(100)
        self.assertIsInstance(self.analyzer1.permutation_count(), pd.DataFrame)

        self.game2.play(100)
        self.assertIsInstance(self.analyzer2.permutation_count(), pd.DataFrame)

if __name__ == "__main__":
    unittest.main()
