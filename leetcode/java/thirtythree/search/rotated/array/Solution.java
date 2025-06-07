package thirtythree.search.rotated.array;

public class Solution {
    public int search(int[] nums, int target) {

        // [4,5,6,7,8,9,0,1,2,3], target = 0
        //  0 1 2 3 4 5 6 7 8 9
        // if target lies in the sorted side, basic binary search lookup
        // else, continue to split the array and check which side if ordered and which is not


        // mid = 4, target is in right side, based off our logic that determines which side is ordered
        // mid = 1, target is in left side
        // mid = 6, index 6 is the target

        int left = 0;
        int right = nums.length-1;

        while (left <= right) {
            // [4,5,6,7,0,1,2] target=0
            //.       L M   R
            int mid = (left + right) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[left] == target) {
                return left;
            } else if (nums[right] == target) {
                return right;
            }

            // check if left is ordered
            // [4,5,6,7,0,1,2]
            //. 0 1 2 3 4 5 6
            //.         ^
            if (nums[left] < nums[mid]) {
                if (nums[left] < target && target < nums[mid]) {
                    // target is in the ordered side and the ordered side is left
                    right = mid-1;
                } else {
                    // target is on the right side
                    left = mid+1;
                }
            }
            // right side is ordered
            else {
                // target is in the ordered side and the ordered side is right
                if (nums[mid] < target && target < nums[right]) {
                    left = mid+1;
                }
                // target is on the left side
                else {
                    right = mid-1;
                }
            }
        }
        return -1;
    }
}