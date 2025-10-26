class ATM {
    private int[] notes = new int[5];
    private final int[] values = {20, 50, 100, 200, 500};

    public ATM() {
        
        
    }
    
    public void deposit(int[] banknotesCount) {
        for(int i = 0; i < notes.length; i++){
            notes[i] += banknotesCount[i];
        }


        
    }
    
    public int[] withdraw(int amount) {
        int[] used = new int[5];
        int remaining = amount;
        for(int i = 4 ; i>=0 ; i--){
            int available = notes[i];
            int use = Math.min(remaining/values[i],available);
            used[i] = (int)use;
            remaining -= use * values[i];

        }
        if(remaining != 0){
            return new int[]{-1};
        }
        for(int j = 0 ; j<5 ; j++){
            notes[j] -= used[j];
        }
        return used;

        
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * ATM obj = new ATM();
 * obj.deposit(banknotesCount);
 * int[] param_2 = obj.withdraw(amount);
 */