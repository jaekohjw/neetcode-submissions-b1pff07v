class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int lo = 1;
        int hi = piles[0];
        int ans = 0;

        for (int i = 1; i < piles.length; i++) {
            if (piles[i] > hi) {
                hi = piles[i];
            }
        }

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            long totalTime = 0;

            for (int p : piles) {
                totalTime += Math.ceil((double) p / mid);
            }

            if (totalTime <= h) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return ans;
    }
}
