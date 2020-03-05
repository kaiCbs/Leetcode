class Solution(object):
    def isValidSudoku(self, board):
        def valid(inp):
            if len(inp) == 3:
                temp = []
                for i in inp:
                    temp += i
                inp = temp
            b = [i for i in inp if i != '.']
            return len(set(b)) == len(b)
        
        for i in board:
            if not valid(i):
                print("1",i)
                return False
        for i in range(9):
            if not valid([r[i] for r in board]):
                print("2",[r[i] for r in board])
                return False
        for i in range(3):
            for j in range(3):
                if not valid([r[i*3:(i+1)*3] for r in board[j*3:(j+1)*3]]):
                    print("3",[r[i*3:(i+1)*3] for r in board[j*3:(j+1)*3]])
                    return False
        return True