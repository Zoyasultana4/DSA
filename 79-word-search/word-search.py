class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            # Base case: If we have found all characters of the word
            if i == len(word):
                return True
            # Base case: Out of bounds or current cell character doesn't match
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[i]:
                return False

            # Mark the current cell as visited by temporarily changing its value
            original_char = board[r][c]
            board[r][c] = '#'  # Use a placeholder to mark as visited

            # Explore neighbors (up, down, left, right)
            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))

            # Backtrack: Restore the original character
            board[r][c] = original_char
            return found

        # Iterate through every cell in the board as a potential starting point
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False