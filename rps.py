import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    return 'lose'

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if result == 'win':
            print("You win!")
            user_score += 1
        elif result == 'lose':
            print("You lose!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"Score - You: {user_score} | Computer: {computer_score}")

        if input("Play again? (yes/no): ").strip().lower() != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
