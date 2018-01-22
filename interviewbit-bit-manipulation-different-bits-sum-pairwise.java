public class Solution {
    public int cntBits(int[] A) {
        int[] bits = new int[31];
        for (int num : A) {
            for (int i = 0; i < 31; i++) {
                if ((num & (1 << i)) != 0) {
                    bits[i]++;
                }
            }
        }
        long diffBits = 0;
        for (int bit : bits) {
            diffBits += 2L * bit * (A.length - bit);
        }
        return (int) (diffBits % 1000000007);
    }
}
