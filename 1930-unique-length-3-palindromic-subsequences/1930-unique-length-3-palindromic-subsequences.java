class Solution {
    public int countPalindromicSubsequence(String s) {
        int count = 0;
        
        for (char ch = 'a'; ch <= 'z'; ch++) {
            int left = s.indexOf(ch);
            int right = s.lastIndexOf(ch);
            
            if (left != -1 && right != -1 && right - left > 1) {
                HashSet<Character> mid = new HashSet<>();
                
                for (int i = left + 1; i < right; i++) {
                    mid.add(s.charAt(i));
                }
                
                count += mid.size();
            }
        }
        
        return count;
    }
}
