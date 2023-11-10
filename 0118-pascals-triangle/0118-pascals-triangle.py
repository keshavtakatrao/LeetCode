class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        
        arr = [[1]]
        
        for i in range(1, numRows):
            tempArr = [1]
            
            for j in range(1, i):
                tempArr.append(arr[i-1][j-1] + arr[i-1][j])
            
            tempArr.append(1)
            arr.append(tempArr)
        
        return arr
