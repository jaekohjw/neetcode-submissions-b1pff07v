class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;
        int lo = 0;
        int hi = m * n - 1;

        int mid = lo + (hi - lo) / 2;
        int r = 0;
        int c = 0;

        while (lo <= hi) {
            mid = lo + (hi - lo) / 2;
            r = mid / n;
            c = mid % n;
            if (matrix[r][c] == target) {
                return true;
            }
            if (matrix[r][c] < target) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return false;
    }
}
