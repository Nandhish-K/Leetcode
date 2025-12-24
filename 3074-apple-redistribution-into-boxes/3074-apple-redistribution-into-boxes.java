import java.util.*;

class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {

        int sum = 0;
        for (int a : apple) {
            sum += a;
        }

        
        Integer[] cap = new Integer[capacity.length];
        for (int i = 0; i < capacity.length; i++) {
            cap[i] = capacity[i];
        }

        Arrays.sort(cap, Collections.reverseOrder());

        int used = 0;
        int total = 0;

        for (int c : cap) {
            total += c;
            used++;
            if (total >= sum) {
                return used;
            }
        }

        return used; 
    }
}
