// You are given an m x n grid where each cell can have one of three values:
//     0 representing an empty cell,
//     1 representing a fresh orange, or
//     2 representing a rotten orange.
// Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
// Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

// Example 1:
// Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
// Output: 4

// Example 2:
// Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
// Output: -1
// Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

// Example 3:
// Input: grid = [[0,2]]
// Output: 0
// Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

// Constraints:
//     m == grid.length
//     n == grid[i].length
//     1 <= m, n <= 10
//     grid[i][j] is 0, 1, or 2.

class Solution {
  public int orangesRotting(int[][] grid) {
    int m = grid.length;
    int n = grid[0].length;
    int minutes = 0;
    while (canProceed(grid)) {
      boolean[][] justTouched = new boolean[m][n];
      for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
          if (grid[i][j] == 2 && !justTouched[i][j]) {
            rotNeighbours(i, j, grid, justTouched);
          }
        }
      }
      minutes++;
    }
    return retValue(grid, minutes);
  }

  public void rotNeighbours(int i, int j, int[][] grid, boolean[][] justTouched) {
    int m = grid.length;
    int n = grid[0].length;
    if (i - 1 >= 0 && grid[i - 1][j] == 1) {
      grid[i - 1][j] = 2;
      justTouched[i - 1][j] = true;
    }
    if (i + 1 < m && grid[i + 1][j] == 1) {
      grid[i + 1][j] = 2;
      justTouched[i + 1][j] = true;
    }
    if (j - 1 >= 0 && grid[i][j - 1] == 1) {
      grid[i][j - 1] = 2;
      justTouched[i][j - 1] = true;
    }
    if (j + 1 < n && grid[i][j + 1] == 1) {
      grid[i][j + 1] = 2;
      justTouched[i][j + 1] = true;
    }
  }

  public boolean canProceed(int[][] grid) {
    int m = grid.length;
    int n = grid[0].length;
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 2
            && ((i - 1 >= 0 && grid[i - 1][j] == 1)
                || (i + 1 < m && grid[i + 1][j] == 1)
                || (j - 1 >= 0 && grid[i][j - 1] == 1)
                || (j + 1 < n && grid[i][j + 1] == 1))) return true;
      }
    }
    return false;
  }

  public int retValue(int[][] grid, int ret) {
    int m = grid.length;
    int n = grid[0].length;
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 1) return -1;
      }
    }
    return ret;
  }
}
