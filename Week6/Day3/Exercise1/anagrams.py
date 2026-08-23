from anagram_checker import AnagramChecker

def main():
    # Replace 'words.txt' with the actual name of your provided text file!
    file_name = 'words.txt'
    
    try:
        checker = AnagramChecker(file_name)
    except FileNotFoundError:
        print(f"Error: Could not find the file '{file_name}'. Make sure it is in the same folder.")
        return

    while True:
        print("\n=== Anagram Checker ===")
        print("1. Input a word")
        print("2. Exit")
        
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == '2':
            print("Goodbye!")
            break
            
        elif choice == '1':
            user_input = input("Enter a word: ").strip()

            # Validation 1: Only a single word allowed
            if ' ' in user_input:
                print("Error: Only a single word is allowed. Please try again.")
                continue
                
            # Validation 2: Only alphabetic characters
            if not user_input.isalpha():
                print("Error: Only alphabetic characters are allowed. Please try again.")
                continue

            # Process the valid word
            word_upper = user_input.upper()
            print(f"\nYOUR WORD : \"{word_upper}\"")

            if checker.is_valid_word(user_input):
                print("This is a valid English word.")
            else:
                print("This is NOT a valid English word.")

            # Get and display anagrams
            anagrams = checker.get_anagrams(user_input)
            
            if anagrams:
                # Join the list into a nicely formatted, comma-separated string
                anagrams_str = ", ".join(anagrams)
                print(f"Anagrams for your word: {anagrams_str}.")
            else:
                print("Anagrams for your word: none found.")
                
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()