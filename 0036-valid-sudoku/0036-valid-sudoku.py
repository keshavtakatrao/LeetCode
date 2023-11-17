class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = collections.defaultdict(set)
        row = collections.defaultdict(set)        
        matrix = collections.defaultdict(set)        
        
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j]==".":
                    continue
                
                if board[i][j] in row[i] or board[i][j] in cols[j] or board[i][j] in matrix[(i//3,j//3)]:
                    return False
                
                else:   
                    cols[j].add(board[i][j])
                    row[i].add(board[i][j])    
                    matrix[(i//3,j//3)].add(board[i][j])
                    
        return True 