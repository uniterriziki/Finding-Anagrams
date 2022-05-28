# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    
    sorted1 = ''.join(sorted(word))
    sorted2 = ''.join(sorted(anagram))
    if (sorted1 == sorted2):
        return True
    

