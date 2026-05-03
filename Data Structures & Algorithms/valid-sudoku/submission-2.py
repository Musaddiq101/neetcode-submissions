class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #check rows
        for i in range(9):
            nums = set()
            for j in range(9):
                if board[i][j] in nums:
                    return False
                if board[i][j] == ".":
                    continue
                else:
                    nums.add(board[i][j])
        
        #check columns
        for i in range(9):
            nums = set()
            for j in range(9):
                if board[j][i] in nums:
                    return False
                if board[j][i] == ".":
                    continue
                else:
                    nums.add(board[j][i])
    
        for k in range(9):
            nums = set()
            row = k // 3 * 3
            col = k % 3 * 3
            for i in range(3):
                for j in range(3):
                    if board[row+i][col+j] == ".":
                        continue
                    elif board[row+i][col+j] in nums:
                        return False
                    nums.add(board[row+i][col+j])
        return True
