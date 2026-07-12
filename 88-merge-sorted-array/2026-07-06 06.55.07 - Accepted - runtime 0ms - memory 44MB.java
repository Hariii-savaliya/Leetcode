class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int pos = m + n - 1;
    // Traverse backwards
        while (n-1 >= 0) {
            if (m-1 >= 0 && nums1[m-1] > nums2[n-1]) {
                nums1[pos--] = nums1[m-1];
                m--;
            } else {
                nums1[pos--] = nums2[n-1];
                n--;
            }
        }
    }
}
                
            
    
