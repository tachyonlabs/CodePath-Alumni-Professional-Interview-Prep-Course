public class Solution {
    public int searchInsert(ArrayList<Integer> a, int b) {
        int start = 0;
        int end = a.size() - 1;
        int mid;
        int val;
        while (start <= end) {
            mid = (start + end) / 2;
            val = a.get(mid);
            if (val == b) {
                return mid;
            } else if (val < b) {
                start++;
            } else {
                end--;
            }
        }
        return start;
    }
}
