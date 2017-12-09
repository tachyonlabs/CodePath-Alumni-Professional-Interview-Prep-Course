public class Solution {
    public int diffPossible(final List<Integer> a, int b) {
        if (a.size() >= 2) {
            HashMap<Integer, Integer> vals = new HashMap<Integer, Integer>();
            for (Integer i : a) {
                if (vals.containsKey(b + i) || vals.containsKey(i - b)) {
                    return 1;
                }
                vals.put(i, 1);
            }
        }
        return 0;
    }
}
