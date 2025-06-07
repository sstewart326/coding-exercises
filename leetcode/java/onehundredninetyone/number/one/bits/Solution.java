package onehundredninetyone.number.one.bits;

public class Solution {

    /**   binary     num_of_ones    Indexes
     * Iteration 1: 1101 & 1100 = 1100, answer = 1
     * Iteration 2: 1100 & 1011 = 1000, answer = 2
     * Iteration 3: 1000 & 0111 = 0000, answer = 3
     * Return 3 (correct - 1101 has three 1-bits)
     */
    public int hammingWeight(int n) {

        int answer = 0;

        while (n != 0) {
            answer++;
            n = n & (n-1);
        }
        return answer;
    }
}
