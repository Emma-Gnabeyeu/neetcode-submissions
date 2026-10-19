class Solution:
    def reverseBits(self, n: int) -> int:
        val = 0
        for i in range(32):
            bit_val = (n >> i) & 1 # extract the bit at the i-th position
            val += (bit_val << (31-i)) # the bit at formely at pos i become at position 31-i when reversed
        return val
        