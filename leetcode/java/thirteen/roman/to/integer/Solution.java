package thirteen.roman.to.integer;

import java.util.Map;

class Solution {

    private static final Map<Character, Integer> ROMAN_NUMERALS = Map.of(
            'I', 1,
            'V', 5,
            'X', 10,
            'L', 50,
            'C', 100,
            'D', 500,
            'M', 1000
    );

    private static final Map<String, Integer> SPECIAL_NUMERALS = Map.of(
            "IV", 4,
            "IX", 9,
            "XL", 40,
            "XC", 90,
            "CD", 400,
            "CM", 900
    );



    private int getIntValue(String s) {
        if (SPECIAL_NUMERALS.containsKey(s)) {
            return SPECIAL_NUMERALS.get(s);
        } else {
            return ROMAN_NUMERALS.get(s.charAt(0));
        }
    }

    public int romanToInt(String s) {
        int count = 0;
        for (int i=0; i<s.length(); i++) {
            if (i != s.length()-1 && SPECIAL_NUMERALS.containsKey(s.substring(i, i+2))) {
                count += getIntValue(s.substring(i, i+2));
                i++;
            } else {
                count += getIntValue(s.substring(i, i+1));
            }
        }
        return count;
    }
}