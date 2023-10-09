# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
import collections
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True

# broken solution
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        columns = [[] for i in range(9)]
        cells = [[] for i in range(9)]
        for i in range(len(board)):
            hash_set = []
            row = board[i]
            for j in range(len(row)-1):
                # populate columns list
                columns[j].append(row[j])

                # populate cells list
                if i < 3:
                    if j < 3:
                        cells[0].append(row[j])
                    elif j > 2 and j < 6:
                        cells[1].append(row[j])
                    else:
                        cells[2].append(row[j])
                if i > 2 and i < 6:
                    if j < 3:
                        cells[3].append(row[j])
                    elif j > 2 and j < 6:
                        cells[4].append(row[j])
                    else:
                        cells[5].append(row[j])
                else:
                    if j < 3:
                        cells[6].append(row[j])
                    elif j > 2 and j < 6:
                        cells[7].append(row[j])
                    else:
                        cells[8].append(row[j])

                # check valid row
                if row[j] != ".":
                    if row[j] not in hash_set:
                        hash_set.append(row[j])
                    else:
                        print(j)
                        return False
        for i in range(len(columns)-1):
            hash_set = []
            col = columns[i]
            print("length", len(columns))
            for j in range(8):
                if col[j] != ".":
                    if col[j] not in hash_set:
                        hash_set.append(col[j])
                    else:
                        print(j)
                        return False
        for i in range(len(cells)):
            hash_set = []
            cell = cells[i]
            for j in range(len(cell)-1):
                if cell[j] != ".":
                    if cell[j] not in hash_set:
                        hash_set.append(cell[j])
                    else:
                        print(j)
                        return False
        return True
