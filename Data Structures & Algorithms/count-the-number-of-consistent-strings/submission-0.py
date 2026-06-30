class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allo = set(allowed)
        count = len(words)
        for word in words:
            for c in word:
                if c not in allo:
                    count -= 1
                    break
        return count

