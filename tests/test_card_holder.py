# -*- coding: utf-8 -*-

import unittest

from blackjack.model import Card, CardHolder


class CardHolderTest(unittest.TestCase):

    def setUp(self):
        self.card_holder = CardHolder()

    def test_WhenAddingACard_thenItAppendsToDeck(self):
        # given
        card = Card('Spades', 'A')

        # when
        self.card_holder.add_card(card)

        # then
        self.assertEqual(len(self.card_holder.hand), 1)

    def test_WhenAddingACardTwice_thenRaiseValueError(self):
        # given
        ace_of_spades = Card('Spades', 'A')

        # when
        self.card_holder.add_card(ace_of_spades)

        # then
        self.assertRaises(ValueError, self.card_holder.add_card, ace_of_spades)

    def test_WhenAddingAnAceWhenHandValueIsBelow11_thenAceValueIs11(self):
        # given
        cards = (
            Card('Clubs', '2'),
            Card('Clubs', '6')
        )
        ace_of_spades = Card('Spades', 'A')

        # when
        for card in cards:
            self.card_holder.add_card(card)

        # then
        self.card_holder.add_card(ace_of_spades)
        self.assertEqual(self.card_holder.get_hand_value(), 19)

    def test_WhenAddingAnAceWhenHandValueIsAbove11_thenAceValueIs1(self):
        # given
        cards = (
            Card('Clubs', '2'),
            Card('Clubs', '6'),
            Card('Clubs', 'J')
        )
        ace_of_spades = Card('Spades', 'A')

        # when
        for card in cards:
            self.card_holder.add_card(card)

        # then
        self.card_holder.add_card(ace_of_spades)
        self.assertEqual(self.card_holder.get_hand_value(), 19)

    def test_WhenAddingCards_thenGiveTheCorrectValueOfHand(self):
        # given
        cards = (
            Card('Clubs', '2'),
            Card('Clubs', '6'),
            Card('Clubs', 'J')
        )

        # when
        for card in cards:
            self.card_holder.add_card(card)

        # given
        self.assertEqual(self.card_holder.get_hand_value(), 18)

    def test_WhenAddingCardsUntilHandValueOver21_thenRaiseOverflowError(self):
        # given
        cards = (
            Card('Clubs', '2'),
            Card('Clubs', '6'),
            Card('Clubs', 'J')
        )
        overflow_card = Card('Diamonds', 'Q')

        # when
        for card in cards:
            self.card_holder.add_card(card)

        # given
        self.assertRaises(OverflowError, self.card_holder.add_card, overflow_card)

    def test_WhenAddingCards_thenDrawTheHandCorrectly(self):
        # given
        cards = (
            Card('Clubs', '2'),
            Card('Hearts', '6'),
            Card('Clubs', 'J'),
            Card('Diamonds', '3')
        )
        expected = ''
        expected += '┌─────────┐┌─────────┐┌─────────┐┌─────────┐\n'
        expected += '| 2       || 6       || J       || 3       |\n'
        expected += '|         ||         ||         ||         |\n'
        expected += '|    ♣    ||    ♥    ||    ♣    ||    ♦    |\n'
        expected += '|         ||         ||         ||         |\n'
        expected += '|       2 ||       6 ||       J ||       3 |\n'
        expected += '└─────────┘└─────────┘└─────────┘└─────────┘\n'

        # when
        for card in cards:
            self.card_holder.add_card(card)

        # given
        self.assertEqual(self.card_holder.draw_deck(), expected)
