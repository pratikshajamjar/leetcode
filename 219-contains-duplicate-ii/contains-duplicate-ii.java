class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        int i,j,n;
        n=nums.length;
        for(i=0;i<n-1;i++)
        {
            for(j=i+1;j<n && j<=i+k;j++)
            {
                if (nums[i]==nums[j]) 
                {
                    return true;
                }
            }
        }
        return false;
        
    }
}