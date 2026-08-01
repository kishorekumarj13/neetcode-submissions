class Solution:
    def scoreOfString(self, s: str) -> int:
        sum_of_num = 0
        for i in range(len(s)-1):
            sum_of_num = sum_of_num + abs(ord(s[i])-ord(s[i+1]))
        return sum_of_num