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

        int mid = lo + (hi - lo) / 2;
        while (lo <= hi) {
            mid = lo + (hi - lo) / 2;
            if (this.canFinish(piles, mid, h)) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return ans;
    }

    public boolean canFinish(int[] piles, int r, int maxH) {
        long h = 0;
        for (int pile : piles) {
            h += Math.ceil((double) pile / r);
        }
        return h <= maxH;
    }
}
