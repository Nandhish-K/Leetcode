class Solution {
    public int minMoves(int[] nums) {
        int sum = nums[0];
        int min = nums[0];
        for(int i = 1; i < nums.length; i++){
            if(nums[i] < min){
                min = nums[i];
            }
            sum += nums[i];
        }
        return sum - (min*nums.length);
    }
}