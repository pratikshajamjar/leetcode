class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        int seq = 0;

        for(int n : arr){
            if((n&1) == 1) {
                if(++seq == 3) return true;
            }
            else seq = 0;
        }

        return false;
    }
}