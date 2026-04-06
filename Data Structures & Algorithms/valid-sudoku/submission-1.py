class Solution:
    def isValidSudoku(self, board):
        colMaps = [{},{},{},{},{},{},{},{},{}]
        for row in board:
            rowMap = {}
            for elIndex in range(9):
                el = row[elIndex]
                if el != ".":
                    rowMap[el] = 1 + rowMap.get(el, 0)
                    colMaps[elIndex][el] = 1 + colMaps[elIndex].get(el, 0)
            for val in rowMap.values():
                if val != 1:
                    return False
        for col in colMaps:
            for val in col.values():
                if val != 1:
                    return False
        sqMaps = [{},{},{},{},{},{},{},{},{}]
        for col in range(0, 9, 3):
            for row in range(0,9,3):
                sqMap = {}
                for rowIndex in range(row, row+3):
                    for colIndex in range(col, col+3):
                        el = board[rowIndex][colIndex]
                        if el != ".":
                            sqMap[el] = 1 + sqMap.get(el, 0)
                for val in sqMap.values():
                    if val != 1:
                        return False
        return True