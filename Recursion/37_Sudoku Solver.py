class Solution(object):
    def isSafe(self,board,row,col,num):

        #checking for the row
        for i in range(0,len(board)):
            if board[row][i]==num:
                return False
        
        #checking for the col
        for j in range(0,len(board)):
            if board[j][col]==num:
                return False

        #checking in the matrix
        square_root = int(math.sqrt(len(board)))
        startrow = row-row%square_root
        startcol = col-col%square_root

        for i in range(startrow,startrow+square_root):
            for j in range(startcol,startcol+square_root):
                if board[i][j]==num:
                    return False
        return True

    def solveSudoku(self, board):
        n = len(board)
        row = -1
        col = -1
        
        emptyleft = True
        for i in range(0,n):
            for j in range(0,n):
                if board[i][j]==".":
                    row = i
                    col = j
                    emptyleft = False
                    break

            if emptyleft==False:
                break
        
        if emptyleft==True:
            return True
        
        for i in range(1,len(board)+1):
            if self.isSafe(board,row,col,str(i)):
                board[row][col]=str(i)
                if self.solveSudoku(board):
                    return True
                else:
                    board[row][col]="."
        return False
        