# -*- coding: utf-8 -*-

import random

from .card import Card
from .card_holder import CardHolder


class Dealer(CardHolder):

    def __init__(self):
        super().__init__()
        self.deck = []
        self.generate_deck()

    def generate_deck(self):
        for suit in Card.suits.keys():
            for rank in Card.ranks:
                self.deck.append(Card(suit, rank))

        random.shuffle(self.deck)

    def get_card(self, is_hidden=False):
        card_index = random.randint(0, len(self.deck) - 1)
        card = self.deck.pop(card_index)
        card.is_hidden = is_hidden

        return card

    def turn(self, dealer):
        is_dealer_turn = True

        for card in self.hand:
            card.is_hidden = False

        while is_dealer_turn:
            if 17 <= self.get_hand_value() <= 21:
                print(self.draw_deck())
                print('End of Dealer\'s turn. ')
                is_dealer_turn = False
            else:
                try:
                    self.add_card(dealer.get_card())
                except OverflowError as e:
                    print(f'\n==== {str(e)} ====\n')
                    raise OverflowError('Player won!')
                finally:
                    print('Dealer\'s hand: ')
                    print(self.draw_deck())
