class Solution {
    public int findFinalValue(int[] nums, int original) {
        // Arrays.sort(nums);
        // for(int i = 0;i<nums.length;i++){
        //     if (nums[i] == original)
        //     {
        //         nums[i] = nums[i]*2;
        //         original = nums[i];
        //     }
        // }
        // return original;
        
    //     boolean x = true;
    //     while(x){
    //         x = found(nums,original);
    //         original *= 2;
    //     }
    //     return original/2;
    // }
    // public boolean found(int[] nums,int original){
    //     for(int ele:nums){
    //         if(ele==original){
    //             return true;
    //         }

    //     }
    //     return false;
    HashSet<Integer>set = new HashSet<>();
    for(int ele:nums){
        set.add(ele);
    }
    while(set.contains(original)){
        original *= 2;
    }
    return original;
    }
}