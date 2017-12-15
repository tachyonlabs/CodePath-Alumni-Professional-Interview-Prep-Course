public class Solution {
    // DO NOT MODIFY THE LIST
    public ArrayList<Integer> searchRange(final List<Integer> a, int b) {
        ArrayList<Integer> range = new ArrayList<>();
        int low = 0;
        int high = a.size() - 1;
        int med;
        while (low <= high) {
            med = (low + high) / 2;
            if (a.get(med) < b) {
                low = med + 1;
            } else {
                high = med - 1;
            }
        }
        if (a.get(low) != b) {
            range.add(-1);
            range.add(-1);
        } else {
            range.add(low);
            high = a.size() - 1;
            while (low <= high) {
                med = (low + high) / 2;
                if (a.get(med) <= b) {
                    low = med + 1;
                } else {
                    high = med - 1;
                }
            }
            range.add(high);
        }
        return range;
    }
}
