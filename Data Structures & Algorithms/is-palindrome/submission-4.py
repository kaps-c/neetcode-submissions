class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean up the string
        cleaned_str = ''.join([char.lower() for char in s if char.isalnum()])
        n = len(cleaned_str) - 1  # last index 

        # if string is empty or just one character return True
        if n <= 0: 
            return True
        
        # initialise two pointers
        l = 0 
        r = n

        # loop through cleaned string
        while l<r:
            if  (cleaned_str[l] == cleaned_str[r]):
                l += 1
                r -= 1
            else: 
                return False
        
        return True