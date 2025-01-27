class Solution {
    public boolean containsDuplicate(int[] nums) {
        int i,n;
        Arrays.sort(nums);
        n=nums.length;
        for (i=1;i<n;i++)
        {
            if (nums[i]==nums[i-1])
            {
                return true;
            }
        }
       
            
        return false;

        
    }
}