# -*- coding: utf-8 -*-

from .model import Dealer, Player


def run():
    dealer, player = init_game()

    running = True
    while running:
        bet = get_player_bet(player)

        print('Dealer\'s hand:')
        print(dealer.draw_deck())

        print('Player\' hand: ')
        print(player.draw_deck())

        try:
            player.turn(dealer)
            dealer.turn(dealer)

            if player.get_hand_value() > dealer.get_hand_value():
                print('Player won!')
                player.balance += bet * 1.5
            else:
                print('Dealer won!')
        except OverflowError as e:
            s = str(e)
            if s == 'Player won!':
                player.balance += bet * 1.5
            print(s)
        finally:
            if check_player_balance(player):
                choice = input('Do you wan\'t play one more round [yes|no]: ')
                if 'yes' == choice:
                    dealer, player = init_game(player)
                else:
                    running = False
            else:
                running = False


def init_game(player=None):
    dealer = Dealer()

    if not player:
        player = Player()
    else:
        player.drop_cards()

    dealer.add_card(dealer.get_card(True))
    dealer.add_card(dealer.get_card())

    player.add_card(dealer.get_card())
    player.add_card(dealer.get_card())

    return dealer, player


def get_player_bet(player):
    valid_bet = False
    while not valid_bet:
        try:
            bet = place_bet(player)
            player.bet(bet)
            valid_bet = True

            return bet
        except ValueError as e:
            print(str(e))


def place_bet(player):
    bet = 0
    valid_bet = False
    while not valid_bet:
        try:
            bet = int(input(f'Place your bet [Your balance: {player.balance}]: '))
            valid_bet = True
        except ValueError:
            print('Your bet is invalid. Place an integer bet.')

    return bet


def check_player_balance(player):
    if player.balance <= 0:
        print('You\'re out of money... The game is ended!')
        return False

    return True
