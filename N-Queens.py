class Solution:
    def solveNQueens(self, n):
        def is_valid(row, col):
            return col not in cols and (row - col) not in diag1 and (row + col) not in diag2

        def place_queen(row):
            if row == n:
                board = []
                for i in range(n):
                    row_str = ['.'] * n
                    row_str[queens[i]] = 'Q'
                    board.append(''.join(row_str))
                results.append(board)
                return

            for col in range(n):
                if is_valid(row, col):
                    queens[row] = col
                    cols.add(col)
                    diag1.add(row - col)
                    diag2.add(row + col)

                    place_queen(row + 1)

                    # Backtrack
                    cols.remove(col)
                    diag1.remove(row - col)
                    diag2.remove(row + col)

        results = []
        queens = [-1] * n
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col

        place_queen(0)
        return results
