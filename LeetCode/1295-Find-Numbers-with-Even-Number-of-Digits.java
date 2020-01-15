class Solution {
    public int findNumbers(int[] nums) {

        int evenNums = 0;
        for (int i = 0; i < nums.length; i++) {
            int digits = this.getNumberDigits(nums[i]);
            evenNums += ~digits & 1;
        }
        return evenNums;
    }

    private int getNumberDigits(int num) {
        int digits = 0;

        while (num > 0) {
            digits++;
            num /= 10;
        }

        return digits;
    }
}