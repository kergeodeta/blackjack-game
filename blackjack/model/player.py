# -*- coding: utf-8 -*-

from . import CardHolder


class Player(CardHolder):

    def __init__(self):
        super().__init__()
        self.balance = 100

    def bet(self, amount):
        if self.balance < amount:
            raise ValueError(f'Your balance ({self.balance}) is lower than your bet ({amount})!')

        self.balance -= amount

    def turn(self, dealer):
        is_player_turn = True

        while is_player_turn:
            choice = input('Do you want to hit [hit|stand]: ')
            if 'hit' == choice:
                print('Player take another card')
                try:
                    self.add_card(dealer.get_card())
                except OverflowError as e:
                    print(f'\n==== {str(e)} ====\n')
                    raise OverflowError('Dealer won!')
                finally:
                    print('Player\'s hand: ')
                    print(self.draw_deck())

            elif 'stand' == choice:
                print('End of Player\'s turn. Dealer comes...')
                is_player_turn = False
            else:
                print('Unknown operation. Type \'hit\' or \'stand\'!')
