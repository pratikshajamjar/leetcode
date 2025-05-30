class Solution {
    public int countKDifference(int[] nums, int k) {
        int count = 0;
        HashMap <Integer, Integer> hm = new HashMap <>();
        for(int num: nums){
            hm.put(num, hm.getOrDefault(num, 0)+1);
        }
        for(int num: nums){
            if(hm.containsKey(num-k)){
                count+=hm.get(num-k);
            }
            if(hm.containsKey(num+k)){
                count+=hm.get(num+k);
            }
        }
        return count/2;
    }
}