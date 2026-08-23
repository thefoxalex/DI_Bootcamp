import random

class Game:
    def get_user_item(self):
        valid_items = ['rock', 'paper', 'scissors']
        while True:
            # We strip whitespace and make it lowercase to handle accidental spaces or caps
            user_input = input("Select an item (rock/paper/scissors): ").strip().lower()
            if user_input in valid_items:
                return user_input
            print("Invalid choice. Please enter rock, paper, or scissors.")

    def get_computer_item(self):
        items = ['rock', 'paper', 'scissors']
        return random.choice(items)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
            
        # Determine if the user won
        if (user_item == 'rock' and computer_item == 'scissors') or \
           (user_item == 'paper' and computer_item == 'rock') or \
           (user_item == 'scissors' and computer_item == 'paper'):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"\nYou chose: {user_item}")
        print(f"Computer chose: {computer_item}")
        print(f"Result: {result}!")

        return result