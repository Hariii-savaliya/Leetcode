class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        
        int j = 0; // Position for next unique element
        
        for (int i = 1; i < nums.length; i++) {
            if(nums[i]==nums[j]){
                
            }
            else{
                nums[j+1]=nums[i];
                j++;
            }
        }
        
        return j + 1; // Why j + 1?
    }
}