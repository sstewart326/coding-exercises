package onehunderedthirtysix.single.number;

public class Solution {

    public int singleNumber(int[] nums) {
        int answer = 0;

        for (int num : nums) {
            answer ^= num;
        }

        return answer;
    }
}