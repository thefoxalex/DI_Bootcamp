import random
import sys
import json 

# EXERCISE 1: Random Sentence Generator

WORD_FILE_PATH = "words.txt"

def get_words_from_file(file_path):
    """Reads a file and returns a list of words."""
    try:
        with open(file_path, "r") as file:
            content = file.read()
            return content.split()
    except FileNotFoundError:
        print(f"Error: Could not find '{file_path}'. Please make sure it is in your directory.")
        sys.exit(1)

def get_random_sentence(length):
    """Generates a random, lowercase sentence of a given length."""
    words = get_words_from_file(WORD_FILE_PATH)
    selected_words = random.choices(words, k=length)
    sentence = " ".join(selected_words)
    return sentence.lower()

def main(): 
    """Handles user input and program flow for Exercise 1."""
    print("--- Exercise 1: Random Sentence Generator ---")
    
    user_input = input("Enter the desired sentence length (between 2 and 20): ")
    
    try:
        length = int(user_input)
    except ValueError:
        print("Error: Invalid input. The length must be an integer.")
        return 
        
    if not (2 <= length <= 20):
        print("Error: The sentence length must be between 2 and 20 (inclusive).")
        return 
        
    final_sentence = get_random_sentence(length)
    print(f"Generated Sentence:\n> {final_sentence}\n")



# EXERCISE 2: Working with JSON

def run_json_exercise():
    """Parses JSON, modifies it, and saves it to a file."""
    print("--- Exercise 2: Working with JSON ---")
    
    sampleJson = """{ 
       "company":{ 
          "employee":{ 
             "name":"emma",
             "payable":{ 
                "salary":7000,
                "bonus":800
             }
          }
       }
    }"""

    data = json.loads(sampleJson)

    salary = data["company"]["employee"]["payable"]["salary"]
    print(f"Emma's accessed salary is: {salary}")

    data["company"]["employee"]["birth_date"] = "1992-08-24"

    output_filename = "employee_data.json"
    with open(output_filename, "w") as file:
        json.dump(data, file, indent=4)
        
    print(f"Modified JSON has been successfully saved to '{output_filename}'.")

if __name__ == "__main__":
    main()
    
    print("-" * 40 + "\n")
    
    # Run Exercise 2
    run_json_exercise()