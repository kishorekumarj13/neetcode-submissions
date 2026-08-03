class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        else:
            return self._get_alphabet_count(s) == self._get_alphabet_count(t)
    def _get_alphabet_count(self, word: str) -> dict:
        letters = list(set(sorted(word)))
        alphabet_count = {}
        for i in range(len(letters)):
            alphabet_count[letters[i]] = word.count(letters[i])
        return alphabet_count

        