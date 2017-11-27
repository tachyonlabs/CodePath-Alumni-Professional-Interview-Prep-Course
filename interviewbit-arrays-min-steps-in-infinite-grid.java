public class Solution {
    // X and Y co-ordinates of the points in order.
    // Each point is represented by (X.get(i), Y.get(i))
    public int coverPoints(ArrayList<Integer> X, ArrayList<Integer> Y) {
        int steps = 0;
        int currX = X.get(0);
        int currY = Y.get(0);
        for (int i = 1; i < X.size(); i++) {
            steps += Math.max(Math.abs(X.get(i) - currX), Math.abs(Y.get(i) - currY));
            currX = X.get(i);
            currY = Y.get(i);
        }
        return steps;
    }
}
