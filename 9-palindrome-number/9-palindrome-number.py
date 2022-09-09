class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp = x #keep value of original x
        if x < 0: return False #negatives will never be true
        left = 10
        reverseX = 0
        while x > 0:
            last = x%10 #current last digit of x
            x = x//10
            reverseX = reverseX*10 + last #adds last digit of x to revrseX in reverse order
        return (tmp == reverseX) #compare to orginal value of x
        
        