import java.util.Stack;

class Solution {
    public int minOperations(String[] logs) {
        Stack<String> st = new Stack<>();

        for (String log : logs) {
            if (log.equals("../")) {
                if (!st.isEmpty()) {
                    st.pop();  // Move up one level if possible
                }
            } else if (!log.equals("./")) {
                st.push(log);  // Add directory to stack if it's a valid folder
            }
        }

        return st.size();  // Remaining stack size represents final depth
    }
}
