public class Solution {
    public int firstMissingPositive(int[] A) {
        int temp;
        for (int i = 0; i < A.length; i++) {
            // if a number is out of place, is in the range 1 to the length of the array, and is not
            // a duplicate of the number already in its correct place, swap them
            if (A[i] != i + 1 && A[i] > 0 && A[i] <= A.length && A[i] != A[A[i] - 1]) {
                temp = A[A[i] - 1];
                A[A[i] - 1] = A[i];
                A[i] = temp;
                // and stay in place to check the number that was just swapped into that position, too
                i--;
            }
        }
        for (int i = 0; i < A.length; i++) {
            if (A[i] != i + 1) {
                return i + 1;
            }
        }
        return A.length + 1;
    }
}
