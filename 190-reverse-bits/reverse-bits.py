class Solution:
    def reverseBits(self, n: int) -> int:
        v=bin(n)[2:]
        v=v.zfill(32)
        v=v[::-1]
        
        return int(v,2)