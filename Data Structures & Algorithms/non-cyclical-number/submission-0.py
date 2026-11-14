class Solution:
    def isHappy(self, n: int) -> bool:
        # We use a hash set to detect if a number has already been process
        def helper_sumOfSquares(n):
            output = 0
            while n:
                digit = n%10
                output+=digit**2
                n=n//10
            return output

        visited = set()
        while n not in visited:
            visited.add(n)
            n = helper_sumOfSquares(n)
            if n==1:
                return True
        return False
        