public class Solution {
    public int numSetBits(long a) {
        int onesCount = 0;
        while (a > 0) {
            a &= (a - 1);
            onesCount++;
        }
        return onesCount;
    }
}
