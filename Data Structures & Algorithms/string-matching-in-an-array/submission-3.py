class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        subString = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j] and words[i] not in subString:
                    subString.append(words[i])
                elif words[j] in words[i] and words[j] not in subString:
                    subString.append(words[j])
        return subString