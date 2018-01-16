import java.util.Collections;

public class Solution {
    public int findMinXor(ArrayList<Integer> A) {
        if (A.size() < 2) {
            return 0;
        }
        Collections.sort(A);
        int minXor = A.get(0) ^ A.get(1);
        for (int i = 1; i < A.size() - 1; i++) {
            minXor = Math.min(minXor, A.get(i) ^ A.get(i + 1));
        }
        return minXor;
    }
}
