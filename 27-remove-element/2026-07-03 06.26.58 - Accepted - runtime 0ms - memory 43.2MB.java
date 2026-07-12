class Solution {
    public int removeElement(int[] nums, int val) {
        int i=0;
        int l=nums.length;
        for(int j=0;j<l;j++){
            if(nums[j]!=val){
                    nums[i]=nums[j];
                   i++;  
                }
        }
            return i;
        
    }    
        
    
}