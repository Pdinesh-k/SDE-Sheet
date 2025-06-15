class Solution(object):
    def display(self,board,arr):
        new_arr = []
        for i in range(len(board)):
            row = ""
            for j in range(len(board)):
                if board[i][j]==True:
                    row+="Q"
                else:
                    row+="."
            new_arr.append(row)
        arr.append(new_arr)

    def isSafe(self,board,row,col):
        for i in range(0,row):
            if board[i][col]==True:
                return False

        maxLeft = min(row,col)
        for i in range(1,maxLeft+1):
            if board[row-i][col-i]==True:
                return False

        maxRight = min(row,len(board)-col-1)
        for i in range(1,maxRight+1):
            if board[row-i][col+i]==True:
                return False
        return True

    def queens(self,board,row,arr):
        if row==len(board):
            self.display(board,arr)
            return
        
        for col in range(0,len(board)):
            if self.isSafe(board,row,col):
                board[row][col] = True
                self.queens(board,row+1,arr)
                board[row][col]=False

        
    def solveNQueens(self, n):
        board = [[False for _ in range(n)]for _ in range(n)]
        arr = []
        self.queens(board,0,arr)
        return arr
        