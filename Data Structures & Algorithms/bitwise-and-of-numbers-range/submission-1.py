class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return right
        res = 0
        diff_loc = 0
        for i in range(32):
            if left & (1<<i) != right & (1<<i):
                diff_loc = i
        
        for i in range(diff_loc+1, 32):
            res |= right & (1<<i)
        return res



        