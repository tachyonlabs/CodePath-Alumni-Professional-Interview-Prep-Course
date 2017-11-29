public class Solution {
    public int[][] generateMatrix(int A) {
        int[][] squareMatrix = new int[A][A];
        int top = 0;
        int right = A - 1;
        int bottom = A - 1;
        int left = 0;
        int num = 1;
        while (top <= bottom) {
            for (int col = left; col <= right; col++) {
                squareMatrix[top][col] = num;
                num++;
            }
            top++;
            for (int row = top; row <= bottom; row++) {
                squareMatrix[row][right] = num;
                num++;
            }
            right--;
            for (int col = right; col >= left; col--) {
                squareMatrix[bottom][col] = num;
                num++;
            }
            bottom--;
            for (int row = bottom; row >= top; row--) {
                squareMatrix[row][left] = num;
                num++;
            }
            left++;
        }
        return squareMatrix;
    }
}
