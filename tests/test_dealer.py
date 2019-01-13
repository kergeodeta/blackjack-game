# -*- coding: utf-8 -*-

import unittest

from blackjack.model import Dealer


class DealerTest(unittest.TestCase):

    def setUp(self):
        self.deck = Dealer()

    def test_deck_generation(self):
        self.assertEqual(len(self.deck.deck), 52)

    def test_get_all_card(self):
        for _ in range(0, 52):
            self.deck.get_card()

        self.assertEqual(len(self.deck.deck), 0)
