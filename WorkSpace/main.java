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


class Tester {
    public static void main(String args[]) {

        Solution s = new Solution();
        int data[] = {12, 345, 2, 6, 7896};

        System.out.println(s.findNumbers(data));
    }
}