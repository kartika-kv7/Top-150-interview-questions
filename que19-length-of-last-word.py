class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        n = len(s)
        
        # Start from the end of the string and ignore trailing spaces
        i = n - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # Count the characters of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length
        