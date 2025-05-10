import unittest

import sys
sys.path.append('src/game')
from bankroll import Bankroll

class TestBankrollTypeCheck(unittest.TestCase):

    def test_current(self):
        with self.assertRaises(TypeError):
            Bankroll(100)

class TestBankrollValueCheck(unittest.TestCase):

    def test_current(self):
        with self.assertRaises(ValueError):
            Bankroll(-100.0)