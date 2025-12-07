class Solution {
    public int countPartitions(int[] nums) {
        int count = 0;
        for(int i = 1; i < nums.length; i++){
            int left = summation(0,i,nums);
            int right = summation(i,nums.length,nums);
            if(Math.abs(right - left)%2 == 0){
                count++;
            }
        }
        return count;
    }
    public static int summation(int left,int right,int[] nums){
        int sum = 0;
        for(int i = left; i < right; i++ ){
            sum += nums[i];
        }
        return sum;
    }
}