class Solution:
    def isValid(self, word: str) -> bool:
        vowels = set('aeiouAEIOU')

        if not word.isalnum() or len(word) < 3:
            return False

        has_vowel = any(char in vowels for char in word if char.isalpha())
        has_consonant = any(char.isalpha() and char not in vowels for char in word)

        return has_vowel and has_consonant
