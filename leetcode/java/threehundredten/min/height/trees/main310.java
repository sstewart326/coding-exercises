import threehundredten.min.height.trees.Solution;

public static void main() {
    Solution sol = new Solution();
    int[][] edges = {{0,1}, {1,2}, {1,3}, {2,4}, {3,5}, {4,6}};
    println(sol.findMinHeightTrees(6, edges));
    //println(sol.findMinHeightTrees(1, new int[][]{}));
}