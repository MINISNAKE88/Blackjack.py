import random 
def deal_card():
    cards = [11 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare_cards(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw."
    elif computer_score == 0:
        return "You lose, computer has a blackjack."
    elif user_score == 0:
        return "You win with a blackjack."
    elif user_score > 21:
        return "You went over, you lose."
    elif computer_score > 21:
        return "Computer went over, you win."
    elif user_score > computer_score:
        return "You win, computer loses."
    else:
        return "You lose, computer wins."
def play_game():
    user_cards = []
    computer_cards = []
    game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:        
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                print("\n" * 1)
                user_cards.append(deal_card())
            else:
                game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_cards(user_score, computer_score))
while True:
    play_game_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_game_input == "y":
        
        play_game()
    elif play_game_input == "n":
        print("ok ")
        break
