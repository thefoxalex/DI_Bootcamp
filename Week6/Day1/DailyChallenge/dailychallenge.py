import string
import re

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)
        
        if count == 0:
            return f"The word '{word}' was not found in the text."
        return count

    def most_common_word(self):
        words = self.text.split()
        if not words:
            return None
            
        word_counts = {}
        for w in words:
            if w in word_counts:
                word_counts[w] += 1
            else:
                word_counts[w] = 1
                
        most_common = None
        highest_count = 0
        
        for w, count in word_counts.items():
            if count > highest_count:
                highest_count = count
                most_common = w
                
        return most_common

    def unique_words(self):
        words = self.text.split()
        unique_set = set(words) 
        return list(unique_set)

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return cls(content)


class TextModification(Text):

    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        modified_text = self.text.translate(translator)
        return modified_text


    def remove_stop_words(self):
        stop_words = {
            "a", "an", "the", "and", "but", "if", "or", "because", "as", 
            "what", "which", "this", "that", "is", "are", "was", "were", 
            "be", "been", "being", "have", "has", "had", "do", "does", 
            "did", "to", "of", "in", "for", "on", "with", "at", "by", "from"
        }
        
        words = self.text.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        
        return " ".join(filtered_words)

    def remove_special_characters(self):
        modified_text = re.sub(r'[^\w\s]', '', self.text)
        return modified_text
    


print("--- Testing Text Class ---")
my_text = Text("hello world hello python python python is great")
print("Word frequency of 'python':", my_text.word_frequency("python"))
print("Word frequency of 'java':", my_text.word_frequency("java"))
print("Most common word:", my_text.most_common_word())
print("Unique words:", my_text.unique_words())


print("\n--- Testing TextModification Class ---")
dirty_text = TextModification("Wow! Python is so great, don't you think? @Python #coding")
print("Original text:", dirty_text.text)
print("No punctuation:", dirty_text.remove_punctuation())
print("No stop words:", dirty_text.remove_stop_words())
print("No special characters:", dirty_text.remove_special_characters())    