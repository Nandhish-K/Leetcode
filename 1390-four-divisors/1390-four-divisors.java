class Solution {
    public int sumFourDivisors(int[] nums) {
        int sum = 0;
        for(int ele:nums){
            List<Integer> d = divisors(ele);
            if(d.size() == 4){
                for(int e:d){
                    sum += e;
                }
            }
        }
        return sum;
        
    }
    static List<Integer> divisors(int n){
       
        List<Integer> div = new ArrayList<>();
        for(int i = 1; i*i <= n;i++){
            if(n%i == 0){
                
                div.add(i);
            
           if(i!=(int)n/i){
                
                div.add((int)n/i);
            }
            }
        }
        return div;
    }
}