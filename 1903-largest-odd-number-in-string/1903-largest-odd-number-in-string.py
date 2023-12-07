class Solution:
    def largestOddNumber(self, num: str) -> str:
        str_len = len(num)
        
        while str_len > 0:
            last_element = int(num[-1])
            if last_element%2 > 0:
                return num
            else:
                num = num[:str_len-1]
                str_len = str_len -1
                
        return ""
            