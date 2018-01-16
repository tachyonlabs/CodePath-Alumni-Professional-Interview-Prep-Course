public class Solution {
    // DO NOT MODIFY THE LIST
    public int singleNumber(final List<Integer> a) {
        int single = 0;
        HashMap<Integer, Integer> counts = new HashMap<Integer, Integer>();
        for (Integer num : a) {
            if (counts.containsKey(num)) {
                if (counts.get(num) == 2) {
                    counts.remove(num);
                } else {
                    counts.put(num, 2);
                }
            } else {
                counts.put(num, 1);
            }
        }
        for (int num : counts.keySet()) {
            single = num;
        }
        return single;
    }
}
