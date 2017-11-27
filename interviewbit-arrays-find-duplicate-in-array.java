public class Solution {
    // DO NOT MODIFY THE LIST
    public int repeatedNumber(final List<Integer> a) {
        int missing = 0;
        for (int i = 1; i < a.size(); i++) {
            missing ^= i;
        }
        missing = a.stream().reduce(missing, (x, y) -> x ^ y);
        return missing != 0 ? missing : -1;
    }
}
