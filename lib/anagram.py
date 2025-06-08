# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, match_list):
        # ORIGINAL
        # matches = []
        # # loop through each item in match_list
        # for item in match_list:
        #     # check if sorted word letters and sorted item letters are the same
        #     if sorted(list(self.word)) == sorted(list(item)):
        #         # append item if true
        #         matches.append(item)
        # return matches

        return [item for item in match_list if sorted(list(item)) == sorted(list(self.word))]
             
