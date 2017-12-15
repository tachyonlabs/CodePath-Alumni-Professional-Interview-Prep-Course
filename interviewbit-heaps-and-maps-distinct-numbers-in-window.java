public class Solution {
    public int[] dNums(int[] A, int B) {
        if (B > A.length) {
            return new int[0];
        }
        int[] distinct = new int[A.length - B + 1];
        HashMap<Integer, Integer> counts = new HashMap<>();
        for (int i = 0; i < B; i++) {
            counts.put(A[i], counts.getOrDefault(A[i], 0) + 1);
        }
        distinct[0] = counts.size();
        for (int i = 0; i < A.length - B; i++) {
            if (counts.get(A[i]) == 1) {
                counts.remove(A[i]);
            } else {
                counts.put(A[i], counts.get(A[i]) - 1);
            }
            counts.put(A[i + B], counts.getOrDefault(A[i + B], 0) + 1);
            distinct[i + 1] = counts.size();
        }
        return distinct;
    }
}
