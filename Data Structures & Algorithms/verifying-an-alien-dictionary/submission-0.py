class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapp = dict(zip(order, range(26)))
        def compare(a,b):
            m,n = len(a), len(b)
            for j in range(min(m,n)):
                if mapp[a[j]] > mapp[b[j]]:
                    return False
                if mapp[a[j]] < mapp[b[j]]:
                    return True
            if m > n:
                return False
            return True
        
            
        for i in range(len(words)-1):
            if not compare(words[i], words[i+1]):
                return False

        return True
        