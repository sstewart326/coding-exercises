import threethirtyeight.counting.bits.Solution;

public static void main() {
    Solution sol = new Solution();
    Arrays.stream(sol.countBits(8)).forEach(bit -> System.out.println(bit));
}