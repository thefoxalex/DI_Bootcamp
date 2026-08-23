class AnagramChecker:
    def __init__(self, file_path):
        # Load the word list into a set for fast lookup
        with open(file_path, 'r', encoding='utf-8') as file:
            # We strip whitespace and convert to lowercase for consistency
            self.words = set(word.strip().lower() for word in file)

    def is_valid_word(self, word):
        # Check if the lowercase version of the word exists in our set
        return word.lower() in self.words

    def is_anagram(self, word1, word2):
        # Convert both to lowercase for comparison
        w1, w2 = word1.lower(), word2.lower()
        
        # A word cannot be an anagram of itself
        if w1 == w2:
            return False
            
        # If they have the same letters in different order, sorting them will result in the same list
        return sorted(w1) == sorted(w2)

    def get_anagrams(self, word):
        word = word.lower()
        anagrams = []
        
        # Loop through every word in our dictionary to find matches
        for dict_word in self.words:
            if self.is_anagram(word, dict_word):
                anagrams.append(dict_word)
                
        return anagrams