package threethirtyeight.counting.bits;

public class Solution {

    /**
     * Input: n = 5
     * Output: [0,1,1,2,1,2]
     * Explanation:
     * 0 --> 0             0
     * 1 --> 1             1     INDEXES
     * 2 --> 10            1      1 + 0
     * 3 --> 11            2      1 + 1
     * 4 --> 100           1      2 + 0
     * 5 --> 101           2      2 + 1
     * 6 --> 110           2      3 + 0
     * 7 --> 111           3      3 + 1
     * 8 --> 1000          1      4 + 0
     */
    public int[] countBits(int n) {

        int[] numOfOnes = new int[n+1];
        if (n == 0) {
            return numOfOnes;
        }
        numOfOnes[1] = 1;

        for (int i = 2; i<n+1; i++) {
            numOfOnes[i] = numOfOnes[i/2] + numOfOnes[i%2];
        }
        return numOfOnes;
    }
}
