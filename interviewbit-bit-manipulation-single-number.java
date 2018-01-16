public class Solution {
    // DO NOT MODIFY THE LIST
    public int singleNumber(final List<Integer> a) {
        return a.stream().reduce(0, (x, y) -> x ^ y);
    }
}
