package threehundredninetyfour.decode.string;

import java.util.Stack;

public class Solution {

    /**
     * Input: s = "2[abc]3[cd]ef"
     * Output: "abcabccdcdcdef"
     */
    public String decodeString(String s) {

        Stack<String> stack = new Stack<>();

        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == ']') {

                // substring
                StringBuilder substring = new StringBuilder();
                while (!"[".equals(stack.peek())) {
                    substring.insert(0, stack.pop());
                }

                // pop [
                stack.pop();

                // count
                StringBuilder count = new StringBuilder();
                while(!stack.isEmpty() && Character.isDigit(stack.peek().charAt(0))) {
                    count.insert(0, stack.pop());
                }

                for (int j = 0; j<Integer.parseInt(count.toString()); j++) {
                    stack.push(substring.toString());
                }
            } else {
                stack.push(s.substring(i, i+1));
            }
        }

        StringBuilder finalString = new StringBuilder();
        while (!stack.isEmpty()) {
            finalString.insert(0, stack.pop());
        }
        return finalString.toString();
    }
}
