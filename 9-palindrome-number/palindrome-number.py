class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            temp=x
            r=0
            while temp !=0:
                d=temp%10
                r=(r)*10+d
                temp//=10
            if x==r:
                return True
            else:
                return False
        