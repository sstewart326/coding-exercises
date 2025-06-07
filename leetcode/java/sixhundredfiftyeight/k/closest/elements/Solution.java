package sixhundredfiftyeight.k.closest.elements;

import java.util.*;

public class Solution {

    private static class HeapInt implements Comparable<HeapInt> {

        int value;
        int target;
        int k;

        public HeapInt(int v, int t, int k) {
            this.value = v;
            this.target = t;
            this.k = k;
        }

        @Override
        public int compareTo(HeapInt o) {
            if (Math.abs(this.target - this.value) == Math.abs(o.target - o.value)) {
                if (this.value < o.value) {
                    return -1;
                } else {
                    return 1;
                }
            } else {
                if (Math.abs(this.target - this.value) < Math.abs(o.target - o.value)) {
                    return -1;
                } else {
                    return 1;
                }
            }
        }
    }

    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        Queue<HeapInt> heap = new PriorityQueue<>();

        for (int curr : arr) {
            heap.add(new HeapInt(curr, x, k));
        }
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            answer.add(heap.poll().value);
        }

        Collections.sort(answer);
        return answer;
    }

}
