public class Solution {
    public String reverseWords(String a) {
        a = a.trim().replaceAll("\\s+", " ");
        String[] words = a.split("\\s");
        int start = 0;
        int end = words.length - 1;
        String temp;
        while (start < end) {
            temp = words[start];
            words[start] = words[end];
            words[end] = temp;
            start++;
            end--;
        }
        return String.join(" ", words);
    }
}
