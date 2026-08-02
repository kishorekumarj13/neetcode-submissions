class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        for char1, char2 in zip(s, t):
            if char1 in s_map and s_map[char1] != char2:
                return False
            if char2 in t_map and t_map[char2] != char1:
                return False
            s_map[char1] = char2
            t_map[char2] = char1
        return True