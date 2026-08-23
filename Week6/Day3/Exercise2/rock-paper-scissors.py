from game import Game

def get_user_menu_choice():
    print("\n=== Main Menu ===")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")
    
    valid_choices = ['1', '2', '3']
    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice in valid_choices:
            return choice
        print("Invalid input. Please enter 1, 2, or 3.")

def print_results(results):
    print("\n=== Game Summary ===")
    print(f"Wins: {results['win']}, Losses: {results['loss']}, Draws: {results['draw']}")
    print("Thank you for playing!")

def main():
    # Initialize the results dictionary to track the score
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == '1':
            # Create a new Game object and play it
            game = Game()
            game_result = game.play()
            
            # Update the dictionary based on the returned string
            results[game_result] += 1
            
        elif choice == '2':
            # Show current scores without quitting
            print(f"\nCurrent Scores - Wins: {results['win']}, Losses: {results['loss']}, Draws: {results['draw']}")
            
        elif choice == '3':
            # Quit the game and display the final summary
            print_results(results)
            break

if __name__ == "__main__":
    main()