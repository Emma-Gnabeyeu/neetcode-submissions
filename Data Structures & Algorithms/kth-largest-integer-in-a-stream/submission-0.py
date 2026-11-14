class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.tab = nums
        

    def add(self, val: int) -> int:
        self.tab.append(val)
        self.tab.sort()
        return self.tab[-self.k]
        
