public class Solution {
    public long reverse(long a) {
        long rev = 0;
        for (int i = 0; i < 32; i++) {
            rev <<= 1;
            rev += a & 1;
            a >>= 1;
        }
        return rev;
    }
}
