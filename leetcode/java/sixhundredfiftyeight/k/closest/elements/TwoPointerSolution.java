package sixhundredfiftyeight.k.closest.elements;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class TwoPointerSolution {

    
    /**
     * 1. binary search to find index closest to x
     * 2. set left to that value and right to that value's index + x
     * 3. shift left until new left > last right
     */

    private int getClosestIndex(int[] arr, int x, int k) {
        int left = 0;
        int right = arr.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (arr[mid] == x || (arr[mid-1] < x && x < arr[mid+1])) {
                if (mid + k > arr.length) {
                    return arr.length - k - 1;
                }
                return mid;
            } else if (arr[mid] < x) {
                left = mid;
            } else {
                right = mid;
            }
        }
        return -1;
    }

    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        if (arr.length == 1) {
            if (k == 1) {
                return Arrays.stream(arr).boxed().collect(Collectors.toList());
            } else {
                return new ArrayList<>();
            }
        }

        int left = getClosestIndex(arr, x, k);
        int right = left + k - 1;
        while (left >= 1) {
            int rightVal = arr[right];
            int shiftedLeftVal = arr[left-1];
            if (Math.abs(shiftedLeftVal - x) < Math.abs(rightVal - x)) {
                left--;
                right--;
            } else {
                int[] slicedArray = Arrays.copyOfRange(arr, left, right+1);
                return Arrays.stream(slicedArray).boxed().collect(Collectors.toList());
            }
        }
        return Arrays.stream(Arrays.copyOfRange(arr, left, right+1)).boxed().collect(Collectors.toList());
    }
    
}
