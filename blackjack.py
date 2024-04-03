import random

# Function to create a deck of cards
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

# Function to calculate the value of a hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        if card['rank'] in ['Jack', 'Queen', 'King']:
            value += 10
        elif card['rank'] == 'Ace':
            num_aces += 1
            value += 11
        else:
            value += int(card['rank'])
    
    # Adjust the value if there are aces and the total value exceeds 21
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    
    return value

# Function to display a hand
def display_hand(hand):
    for card in hand:
        print(f"{card['rank']} of {card['suit']}")

# Function to play a round of Blackjack
def play_blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    print("Your hand:")
    display_hand(player_hand)
    print("\nDealer's hand:")
    print(f"{dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}")
    print("Unknown card\n")
    
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    # Player's turn
    while player_value < 21:
        choice = input("Do you want to hit or stand? (h/s): ").lower()
        if choice == 'h':
            player_hand.append(deck.pop())
            print("\nYour hand:")
            display_hand(player_hand)
            player_value = calculate_hand_value(player_hand)
            print(f"\nValue of your hand: {player_value}")
        elif choice == 's':
            break
    
    if player_value > 21:
        print("\nYou busted! Dealer wins.")
        return
    
    # Dealer's turn
    print("\nDealer's turn:")
    print("\nDealer's hand:")
    display_hand(dealer_hand)
    print(f"\nValue of dealer's hand: {dealer_value}")
    
    while dealer_value < 17:
        dealer_hand.append(deck.pop())
        dealer_value = calculate_hand_value(dealer_hand)
        print("\nDealer hits.")
        print("\nDealer's hand:")
        display_hand(dealer_hand)
        print(f"\nValue of dealer's hand: {dealer_value}")
    
    if dealer_value > 21 or dealer_value < player_value:
        print("\nDealer busted! You win.")
    elif dealer_value > player_value:
        print("\nDealer wins.")
    else:
        print("\nIt's a tie!")

# Main function
def main():
    while True:
        play_blackjack()
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()