public class Solution {
    public int sqrt(int a) {
        int start = 0;
        int end = a;
        int mid;
        long squared;
        while (start <= end) {
            mid = (start + end) / 2;
            squared = mid * mid;
            if (squared == a) {
                return mid;
            } else if (squared < a) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return start - 1;
    }
}
