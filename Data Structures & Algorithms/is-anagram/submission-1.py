class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        char_s = {}
        char_t = {}

        for i in s:
            if i in char_s:
                char_s[i] += 1
            else:
                char_s[i] = 1

        for i in t:
            if i in char_t:
                char_t[i] += 1
            else:
                char_t[i] = 1
    
        if char_s == char_t:
            return True
        else:
            return False

                
            