
# Challenge 1

def sort_words_in_string():
    words_input = input("Enter a comma-separated string of words (e.g., 'apple,banana,cherry'): ")

    word_list = [word.strip() for word in words_input.split(',')]

    word_list.sort()

    sorted_words_output = ','.join(word_list)

    print(f"The sorted words are: {sorted_words_output}")

if __name__ == "__main__":
    sort_words_in_string()

# Challenge 2

def longest_word(sentence):
    words = sentence.split()

    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

print(longest_word("Margaret's toy is a pretty doll."))           
print(longest_word("A thing of beauty is a joy forever."))        
print(longest_word("Forgetfulness is by all means powerless!"))