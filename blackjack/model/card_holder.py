# -*- coding: utf-8 -*-


class CardHolder:

    def __init__(self):
        self.hand = []

    def add_card(self, card):
        if card in self.hand:
            raise ValueError('This card already in the deck!')

        self.hand.append(card)

        if self.get_hand_value() > 21:
            raise OverflowError('BUST!')

    def get_hand_value(self):
        value = 0
        for card in filter(lambda c: c.rank != 'A', self.hand):
            value += card.get_value()

        for _ in filter(lambda c: c.rank == 'A', self.hand):
            if value <= 10:
                value += 11
            else:
                value += 1

        return value

    def get_card_count(self):
        return len(self.hand)

    def draw_deck(self):
        tmp_out = [''] * 7
        for card in self.hand:
            card_lines = card.draw().split('\n')

            for cntr in range(0, len(card_lines) - 1):
                tmp_out[cntr] += card_lines[cntr]

        out = ''
        for line in tmp_out:
            out += f'{line}\n'

        return out

    def drop_cards(self):
        self.hand = []

    def turn(self, dealer):
        raise NotImplementedError('Abstract method. Sould implemented in child class')
