import sixhundredfiftyeight.k.closest.elements.Solution;
import sixhundredfiftyeight.k.closest.elements.TwoPointerSolution;

public static void main() {
    Solution solution = new Solution();
    System.out.println(solution.findClosestElements(new int[] {1,2,3,4,5}, 4, 3));

    TwoPointerSolution tps = new TwoPointerSolution();
    System.out.println(tps.findClosestElements(new int[] {1,2,3,4,5}, 4, 3));
    System.out.println(tps.findClosestElements(new int[] {1,3,5,7,8,9,10,11}, 4, 5));
}