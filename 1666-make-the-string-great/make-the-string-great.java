class Solution {
    public String makeGood(String s) {
        StringBuilder result = new StringBuilder();
        
        for (char ch : s.toCharArray()) {
            if (result.length() > 0 && 
                (result.charAt(result.length() - 1) == ch + 32 || 
                 result.charAt(result.length() - 1) == ch - 32)) {
                result.deleteCharAt(result.length() - 1);  // Remove last character
            } else {
                result.append(ch);
            }
        }
        
        return result.toString();
    }
}
