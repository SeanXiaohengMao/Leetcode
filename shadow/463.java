class Solution {
    public int islandPerimeter(int[][] grid) {
        int result = 0;
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return result;
        }

        int n = grid.length;
        int m = grid[0].length;
        int count = 0, share = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) {
                    count++;
                    if (i < n - 1) {
                        share += (grid[i + 1][j]);
                    }
                    if (j < m - 1) {
                        share += (grid[i][j + 1]);
                    }
                }
            }
        }

        result = count * 4 - share * 2;
        return result;
    }
}
