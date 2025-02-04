import java.util.Stack;

class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> st = new Stack<>();
        
        for (String op : operations) {
            if (op.equals("C")) {
                st.pop();  // Remove the last valid score
            } else if (op.equals("D")) {
                int top = st.peek();
                st.push(top * 2);  // Double the last valid score and add to stack
            } else if (op.equals("+")) {
                int last = st.pop();
                int secondLast = st.peek();
                st.push(last);  // Push the last score back
                st.push(last + secondLast);  // Add last and second last scores
            } else {
                st.push(Integer.parseInt(op));  // Convert string to integer and push
            }
        }
        
        int total = 0;
        while (!st.isEmpty()) {
            total += st.pop();  // Sum up all scores in the stack
        }
        
        return total;
    }
}
