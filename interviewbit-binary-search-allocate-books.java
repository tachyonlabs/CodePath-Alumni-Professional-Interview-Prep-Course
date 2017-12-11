public class Solution {
    public int books(ArrayList<Integer> a, int b) {
        if (a.size() < b) {
            return -1;
        }
        int longestBook = Collections.max(a);
        if (a.size() == b) {
            return longestBook;
        }
        int low = longestBook;
        int high = a.stream().reduce(0, (x, y) -> x + y);
        int mid, student, sumPer;
        while (low <= high) {
            mid = (low + high) / 2;
            student = 1;
            sumPer = 0;
            for (int book : a) {
                if (sumPer + book > mid) {
                    student++;
                    sumPer = book;
                } else {
                    sumPer += book;
                }
            }
            if (student <= b) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
}
