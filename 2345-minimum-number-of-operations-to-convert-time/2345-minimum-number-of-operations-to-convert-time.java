class Solution {
    public int convertTime(String current, String correct) {
        int current_time_in_minutes = Integer.parseInt(current.substring(0,2)) * 60 + 
        Integer.parseInt(current.substring(3,current.length()));
        int correct_time_in_minutes = Integer.parseInt(correct.substring(0,2)) * 60 + 
        Integer.parseInt(correct.substring(3,correct.length()));

        int diff = correct_time_in_minutes - current_time_in_minutes;
        int count = 0;
        if (diff == 0){
            return count;
        }
        count += (int)diff/60;
        diff = diff % 60;
        if (diff == 0){
            return count;
        }
        count += (int)diff/15;
        diff = diff % 15;
        if (diff == 0){
            return count;
        }
        count += (int) diff/5;
        diff = diff % 5;
        if (diff == 0){
            return count;
        }
        count += (int)diff /1;
        return count;
    }
}