import java.util.HashMap;
class Solution {
    public int repeatedNTimes(int[] nums) {
         Map<Integer, Integer> dict = new HashMap<>();
         for (int x : nums) {
            dict.put(x, dict.getOrDefault(x, 0) + 1);
        }
        int num_frequency = nums.length/2;
        for(int k:dict.keySet()){
            if(dict.get(k) == num_frequency){
                return k;
            }
        }
    return -1;

    }
}