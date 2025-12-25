class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        Arrays.sort(happiness); 

        long res = 0;
        int dec = 0;

        for (int i = happiness.length - 1; i >= 0 && k > 0; i--) {
            int curr = happiness[i] - dec;
            if (curr <= 0) break;

            res += curr;
            dec++;
            k--;
        }
        return res;
    }
}
