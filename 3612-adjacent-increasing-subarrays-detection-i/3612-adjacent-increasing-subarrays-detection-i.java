import java.util.*;

class Solution {
    public boolean hasIncreasingSubarrays(List<Integer> nums, int k) {
        int n = nums.size();

        for (int i = 0; i <= n - 2 * k; i++) {
            List<Integer> arr1 = nums.subList(i, i + k);
            List<Integer> arr2 = nums.subList(i + k, i + 2 * k);

            if (isStrictlyIncreasing(arr1) && isStrictlyIncreasing(arr2)) {
                return true;
            }
        }
        return false;
    }

    private boolean isStrictlyIncreasing(List<Integer> arr) {
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) <= arr.get(i - 1)) return false;
        }
        return true;
    }
}
