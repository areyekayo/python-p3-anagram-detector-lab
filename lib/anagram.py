# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, match_list):
        return [item for item in match_list if sorted(list(item)) == sorted(list(self.word))]
             
