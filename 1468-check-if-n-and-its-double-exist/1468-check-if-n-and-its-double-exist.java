class Solution {
    public boolean checkIfExist(int[] arr) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < arr.length; i++) {
            map.put(arr[i], map.getOrDefault(arr[i], 0) + 1);
        }

        for (int num : arr) {
            
            if (num != 0 && map.containsKey(num * 2)) {
                return true;
            }

            
            if (num == 0 && map.get(num) > 1) {
                return true;
            }
        }

        return false;
    }
}
