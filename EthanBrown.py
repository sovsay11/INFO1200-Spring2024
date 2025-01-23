import random

name = 'Ethan Brown'
card_dict = {
        'numbers':['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'],
        'suits':['H', 'D', 'S', 'C']
    }

def deck_cards(card_dict):
    cards = []
    num_counter = -1
    for x in card_dict['numbers']:
        suits_counter = -1
        num_counter+=1
        current_num = card_dict['numbers'][num_counter]
        for x in card_dict['suits']:
            suits_counter+=1
            cards.append(current_num + card_dict['suits'][suits_counter])
    return cards

def deal_hand(num, deck):
    hand = []
    for x in range(num):
        random_card = random.choice(deck)
        hand.append(random_card)
        deck.remove(random_card)
    return hand





