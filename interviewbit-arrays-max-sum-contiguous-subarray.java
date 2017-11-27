public class Solution {
    // DO NOT MODFIY THE LIST.
    public int maxSubArray(final List<Integer> a) {
        int maxSoFar = a.get(0);
        int maxEndingHere = a.get(0);
        for (int i = 1; i < a.size(); i++) {
            maxEndingHere = Math.max(maxEndingHere + a.get(i), a.get(i));
            maxSoFar = Math.max(maxSoFar, maxEndingHere);
        }
        return maxSoFar;
    }
}
