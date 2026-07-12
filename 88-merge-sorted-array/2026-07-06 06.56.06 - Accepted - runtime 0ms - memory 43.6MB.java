class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
      
        int a1 = m-1, a2 = n-1;
        int pos = m + n - 1;

        // Traverse backwards
        while (a2 >= 0) {
            if (a1 >= 0 && nums1[a1] > nums2[a2]) {
                nums1[pos--] = nums1[a1--];
            } else {
                nums1[pos--] = nums2[a2--];
            }
        }
    }
}
                
            
    