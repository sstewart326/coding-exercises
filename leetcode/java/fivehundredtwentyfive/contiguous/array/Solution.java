package fivehundredtwentyfive.contiguous.array;

import java.util.HashMap;
import java.util.Map;

public class Solution {

    /**
     *
     * [  0,  1,  1,  1,  1,  1,  0,  0,  0]
     *   {-1 : [0], 0 : [1], 1 : [2, 8], 2 : [3, 7], 3 : [4, 6], 4 : [5]}
     */
    public int findMaxLength(int[] nums) {

        int count = 0;
        Map<Integer, Integer> countsToFirstOccurrence = new HashMap<>();
        countsToFirstOccurrence.put(0, -1);

        int maxLength = 0;

        for (int i=0; i<nums.length; i++) {
            if (nums[i] == 1) {
                count++;
            } else {
                count--;
            }
            if (countsToFirstOccurrence.containsKey(count)) {
                int currLength = i - countsToFirstOccurrence.get(count);
                if (currLength > maxLength) {
                    maxLength = currLength;
                }
            } else {
                countsToFirstOccurrence.put(count, i);
            }
        }

        return maxLength;
    }

}
