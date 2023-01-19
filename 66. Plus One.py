class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        one, i = 1, 0
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                    i += 1
                elif digits[i] != 9:
                    digits[i] += 1
                    one = 0
            else: 
                digits.append(1)
                one = 0    
        return digits[::-1]
            
