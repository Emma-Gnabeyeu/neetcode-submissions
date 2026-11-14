class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        number = 0
        for i in range(n):
            number+=digits[i]*10**(n-i-1)
        new_number = number + 1
        
        new_digits = []
        while new_number:
            new_digits.append(new_number%10)
            new_number=new_number//10
        return new_digits[::-1]

        