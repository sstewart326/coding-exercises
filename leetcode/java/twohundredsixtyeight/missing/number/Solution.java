package twohundredsixtyeight.missing.number;

public class Solution {

    public int missingNumber(int[] nums) {
        int expectedSum = 0;
        int actualSum = 0;
        for (int i=0; i<nums.length; i++) {
            expectedSum += i+1;
            actualSum += nums[i];
        }
        return expectedSum - actualSum;
    }

}
