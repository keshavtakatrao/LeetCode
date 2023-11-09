class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        cols = len(matrix[0])
        
        start = 0
        end = (row * cols)-1
            
        while start <= end:
            mid = (start+end) //2
            element = matrix[mid//cols][mid%cols]
            
            if element == target:
                return True
            
            if target > element:
                start = mid+1
            else:
                end = mid-1
                
        return False