public class Solution {
    public int lengthOfLastWord(final String a) {
        String trimmed = a.trim();
        for (int i = trimmed.length() - 1; i >= 0; i--) {
            if (trimmed.charAt(i) == ' ') {
                return trimmed.length() - i - 1;
            }
        }
        return trimmed.length();
    }
}
