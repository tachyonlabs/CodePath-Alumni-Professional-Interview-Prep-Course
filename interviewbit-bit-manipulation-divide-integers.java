public class Solution {
    public int divide(int A, int B) {
        if (B == 1) {
            return A;
        }
        if (A == -2147483648) {
            A = 2147483647;
            B = -B;
        }
        if (Math.abs(A) < Math.abs(B)) {
            return 0;
        }
        if (A < 0 && B < 0) {
            A = -A;
            B = -B;
        }
        int count = 0;
        while (A >= B) {
            A -= B;
            count++;
        }
        return count;
    }
}
