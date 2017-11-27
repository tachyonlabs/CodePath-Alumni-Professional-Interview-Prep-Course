public class Solution {
    public int isPalindrome(String a) {
        a = a.toLowerCase().replaceAll("[^a-z0-9]", "");
        int start = 0;
        int end = a.length() - 1;
        while (start < end) {
            if (a.charAt(start) != a.charAt(end)) {
                return 0;
            }
            start++;
            end--;
        }
        return 1;
    }
}
