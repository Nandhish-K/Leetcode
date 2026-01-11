class Solution {
    public int longestSubarray(int[] nums) {
        if(nums.length == 1){
            return 1;
        }
        else if(nums.length == 2){
            return 2;
        }
        int res = 0;
        int count = 0;
        for(int i = 2; i < nums.length; i++){
            if(nums[i] == nums[i-1] + nums[i-2]){
                count++;
                res = Math.max(res,count);
            }
            else{
                count = 0;
            }
        }
        return res + 2;
    }
}