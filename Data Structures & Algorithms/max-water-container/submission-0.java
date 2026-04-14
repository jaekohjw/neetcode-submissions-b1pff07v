class Solution {
    public int maxArea(int[] heights) {
        int maxArea = 0;
        int curArea = 0;

        for (int i = 0; i < heights.length; i++) {
            for (int j = i; j < heights.length; j++) {
                curArea = Math.min(heights[i], heights[j]) * (j - i);
                maxArea = Math.max(maxArea, curArea);
            }
        }
        return maxArea;
    }
}
