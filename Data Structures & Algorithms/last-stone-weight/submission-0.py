class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>=2:
            stones.sort()
            x,y = stones[-2], stones[-1]
            if x<y:
                stones[-2] = y-x
                stones = stones[:-1]
            if x==y:
                stones = stones[:-2]
        # print(stones)
        if len(stones)==1:
            return stones[0]
        else:
            return 0
            
