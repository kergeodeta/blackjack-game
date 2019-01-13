# -*- coding: utf-8 -*-


class Card:
    suits = {
        'Hearts': '\u2665',
        'Diamonds': '\u2666',
        'Spades': '\u2660',
        'Clubs': '\u2663'
    }
    ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    values = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11
    }

    def __init__(self, suit, rank, is_hidden=False):
        if suit not in self.suits.keys():
            raise ValueError(f'Given suit \'{suit}\' is not exists')

        if rank not in self.ranks:
            raise ValueError(f'Given rank \'{rank}\' is not exists')

        self.suit = suit
        self.rank = rank
        self.is_hidden = is_hidden

    def get_value(self):
        return Card.values.get(self.rank)

    def draw(self):
        face = Card.suits.get(self.suit)
        res = ''

        if self.is_hidden:
            res += '┌─────────┐\n'
            res += '|         |\n'
            res += '|         |\n'
            res += '|         |\n'
            res += '|         |\n'
            res += '|         |\n'
            res += "└─────────┘\n"
        else:
            res += '┌─────────┐\n'
            res += '| {: <2}      |\n'.format(self.rank)
            res += '|         |\n'
            res += '|    {}    |\n'.format(face)
            res += '|         |\n'
            res += '|      {: >2} |\n'.format(self.rank)
            res += "└─────────┘\n"

        return res

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank


if __name__ == '__main__':
    card = Card('Heart', '10')
    print(card.draw())

    card = Card('Diamond', '3')
    print(card.draw())
