class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        counter = 0
        for n in range(len(s)):
            if s[n] == " ":
                counter += 1
            if counter == k:
                return s[0:n]
        return s

