class Solution {
    public int[] decompressRLElist(int[] nums) {

        int len = 0;
        for (int i = 0; i < nums.length; i += 2) {
            len += nums[i];
        }

        int[] rst = new int[len];

        int idx = 0;
        for (int i = 0; i < nums.length; i += 2) {
            for (int t = 0; t < nums[i]; t++) {
                rst[idx++] = nums[i + 1];
            }
        }

        return rst;
    }
}