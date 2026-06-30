class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        dr = {}
        s = s.split()
        if len(s) != len(pattern):
            return False

        for i in range(len(s)):
            if pattern[i] in d:
                if d[pattern[i]] != s[i]:
                    return False
            else:
                d[pattern[i]] = s[i]
            if s[i] in dr:
                if dr[s[i]] != pattern[i]:
                    return False
            else:
                dr[s[i]] = pattern[i]
            
            
        
        return True

        