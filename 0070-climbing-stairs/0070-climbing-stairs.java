class Solution {
    int[] dp;
    public int climbStairs(int n) {
        dp = new int[n+1];
        return f(n);
    }
    private int f(int n){
        if(n == 1){
            return 1;
        }
        else if(n == 2){
            return 2;
        }
        else if(dp[n] != 0){
            return dp[n];
        }
        dp[n] = f(n-1) + f(n-2);
        return dp[n];
    }
}