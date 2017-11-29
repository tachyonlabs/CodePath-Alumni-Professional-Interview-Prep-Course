public class Solution {
    public String longestCommonPrefix(ArrayList<String> a) {
        if (a.size() == 1) {
            return a.get(0);
        }
        StringBuilder sb = new StringBuilder();
        int minStrLen = Integer.MAX_VALUE;
        for (int i =0; i < a.size(); i++) {
            minStrLen = Math.min(minStrLen, a.get(i).length());
        }
        for (int i = 0; i < minStrLen; i++) {
            for (int j = 1; j < a.size(); j++) {
                if (a.get(j).charAt(i) != a.get(0).charAt(i)) {
                    return sb.toString();
                }
            }
            sb.append(a.get(0).charAt(i));
        }
        return sb.toString();
    }
}
