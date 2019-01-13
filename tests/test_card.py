# -*- coding: utf-8

import unittest
from blackjack.model import Card


class CardTest(unittest.TestCase):

    def testRaiseValueException_whenGiveFalseSuitName(self):
        # given
        suit_name = 'whoops!'
        rank_name = 'A'

        # when
        card = Card

        # then
        self.assertRaises(ValueError, card, suit_name, rank_name)

    def testRaiseValueException_whenGiveFalseRankName(self):
        # given
        suit_name = 'Spades'
        rank_name = 'whoops!'

        # when
        card = Card

        # then
        self.assertRaises(ValueError, card, 'Spades', 'whoops!')

    def testDrawCard_whenIsNotHidden(self):
        # given
        ace_of_spades = Card('Spades', 'A')
        expected = ''
        expected += '┌─────────┐\n'
        expected += '| A       |\n'
        expected += '|         |\n'
        expected += '|    ♠    |\n'
        expected += '|         |\n'
        expected += '|       A |\n'
        expected += '└─────────┘\n'

        # when
        drawing = ace_of_spades.draw()

        # then
        self.assertEqual(drawing, expected)

    def testDrawCard_whenIsHidden(self):
        # given
        ace_of_spades = Card('Spades', 'A', True)
        expected = ''
        expected += '┌─────────┐\n'
        expected += '|         |\n'
        expected += '|         |\n'
        expected += '|         |\n'
        expected += '|         |\n'
        expected += '|         |\n'
        expected += '└─────────┘\n'

        # when
        drawing = ace_of_spades.draw()

        # then
        self.assertEqual(drawing, expected)
