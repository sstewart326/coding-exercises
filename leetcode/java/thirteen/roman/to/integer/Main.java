package thirteen.roman.to.integer;

import thirteen.roman.to.integer.Solution;

class Main {
    public static void main() {

        // Symbol       Value
        //I             1
        //V             5
        //X             10
        //L             50
        //C             100
        //D             500
        //M             1000
        // I can be placed before V (5) and X (10) to make 4 and 9.
        //X can be placed before L (50) and C (100) to make 40 and 90.
        //C can be placed before D (500) and M (1000) to make 400 and 900.
        Solution sol = new Solution();
        System.out.println(sol.romanToInt("MCMXCIV"));
    }
}
