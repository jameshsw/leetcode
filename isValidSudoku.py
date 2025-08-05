class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                c = board[row][col]

                if c == ".":
                    continue

                box_i = (row//3)*3 + (col//3)

                if c in rows[row] or c in cols[col] or c in boxes[box_i]:
                    return False
                
                rows[row].add(c)
                cols[col].add(c)
                boxes[box_i].add(c)

        return True



        """
        n = 9
        sub = 3
        counter = Counter()

        # verify rows
        for row in range(n):
            counter.clear()
            for col in range(n):
                c = board[row][col]
                counter[c] += 1
                # print(f"row, col, c, counter: {row}, {col}, {c}, {counter}")
                if c != "." and counter[c] > 1:
                    # print(f"row, col, c: {row}, {col}, {c}")
                    return False

        # verify cols
        for col in range(n):
            counter.clear()
            for row in range(n):
                c = board[row][col]
                counter[c] += 1
                if c != "." and counter[c] > 1:
                    # print(f"row, col, c: {row}, {col}, {c}")
                    return False

        # verify sub-box
        for row in range(0,n,sub):
            for col in range(0,n,sub):
                counter.clear()

                for row1 in range(row,row+sub):
                    for col1 in range(col,col+sub):
                        c = board[row1][col1]
                        counter[c] += 1
                        # print(f"row, col, row1, col1, c, counter: {row}, {col}, {row1}, {col1}, {c}, {counter}")
                        if c != "." and counter[c] > 1:
                            # print(f"row, col, row1, col1, c: {row}, {col}, {row1}, {col1}, {c}")
                            return False

        return True
        """
            
