public class Solution {
    // DO NOT MODIFY THE LIST
    public int binSearch(final List<Integer> a, int b, int low, int high) {
        int med;
        while (low <= high) {
            med = (low + high) / 2;
            if (a.get(med) == b) {
                return med;
            } else if (a.get(med) < b) {
                low = med + 1;
            } else {
                high = med - 1;
            }
        }
        return -1;
    }

    public int search(final List<Integer> a, int b) {
        int low, high, med, pivot;
        if (a.get(0) < a.get(a.size() - 1)) {
            // no pivot
            return binSearch(a, b, 0, a.size() - 1);
        }
        // find pivot
        low = 1;
        high = a.size() - 1;
        while (low <= high) {
            med = (low + high) / 2;
            if (a.get(med) < a.get(0)) {
                high = med - 1;
            } else {
                low = med + 1;
            }
        }
        pivot = low;
        if (b < a.get(pivot) || b > a.get(pivot - 1)) {
            return -1;
        }
        if (b >= a.get(0)) {
            return binSearch(a, b, 0, pivot - 1);
        } else {
            return binSearch(a, b, pivot, a.size() - 1);
        }
    }
}
