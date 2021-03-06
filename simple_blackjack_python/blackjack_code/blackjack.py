"""
Simple Black Jack in Python 3
A simple blackjack game contains all 52 cards in a deck, with 4 sets of 13 cards.
"""

import random
import os


class Blackjack():
    """
    Main class for the game.


    """

    # Function to calculate the hand.
    # In order to calculate the hand you have to pass the hand.
    def calc_hand(hand):
        sum_value = 0

        # Using lists comprehension.
        # Allows creation of a list which iterates over an existing list.
        # Create two lists for separating cards that are aces and non aces.
        non_aces = [card for card in hand if card != 'A']
        aces = [card for card in hand if card == 'A']

        # Iterates through the list of non aces and assign values
        for card in non_aces:
            if card in 'JQK':
                sum_value += 10
            else:
                sum_value += int(card)

        # Iterates through the list of aces and assign values
        for card in aces:
            if sum_value <= 10:
                sum_value += 11
            else:
                sum_value += 1

        return sum_value

    # Cards of the deck.
    cards = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    ]

    random.shuffle(cards)

    dealer = []
    player = [cards.pop(), cards.pop()]

    # Adds a card to the player, then adds one to the dealer
    dealer.append(cards.pop())
    dealer.append(cards.pop())

    standing = False
    first_hand = True

    while True:
        # Checks what kind of operational system is running the program. Clears the screen.
        os.system('cls' if os.name == 'nt' else 'clear')

        # Scores for the player and the dealer
        player_score = calc_hand(player)
        dealer_score = calc_hand(dealer)

        if standing:
            print('Dealer Cards: [{}] ({})'.format(
                ']['.join(dealer), dealer_score))
        else:
            print('Dealer Cards: [{}][?]'.format(dealer[0]))

        print('Player Cards: [{}] ({})\n'.format(']['.join(player), player_score))

        if standing:
            if dealer_score > 21:
                print('Dealer busted, you win!')
            elif player_score == dealer_score:
                print('Push, nobody wins or loses!')
            elif player_score > dealer_score:
                print('You beat the dealer, you win!')
            else:
                print('You lose... :(\n')

            break

        if first_hand and player_score == 21:
            print('BLACKJACK! Nice!')
            break

        first_hand = False

        if player_score > 21:
            print('You busted!')
            break

        choice = input('\nWhat would you like to do?\n[1] Hit\n[2] Stand:\n')

        if choice == '1':
            player.append(cards.pop())
        elif choice == '2':
            standing = True
            while calc_hand(dealer) <= 16:
                dealer.append(cards.pop())


# Executes the main class
Blackjack()
