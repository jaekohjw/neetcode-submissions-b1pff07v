class Solution {
    public int maxArea(int[] heights) {
        int l = 0;
        int r = heights.length - 1;
        int max = 0;
        int cur = 0;

        while (l < r) {
            cur = Math.min(heights[r], heights[l]) * (r - l);
            max = Math.max(cur, max);
            if (heights[l] < heights[r]) {
                l = l + 1;
            }  else {
                r = r - 1;
            }
        }
        return max;
    }
}
