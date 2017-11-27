public class Solution {
    // DO NOT MODIFY THE LIST
    public ArrayList<Integer> spiralOrder(final List<ArrayList<Integer>> a) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        int top = 0;
        int left = 0;
        int right = a.get(0).size() - 1;
        int bottom = a.size() - 1;
        String[] directions = {"Right", "Down", "Left", "Up"};
        int direction = 0;
        while (left <= right && top <= bottom) {
            switch (directions[direction]) {
                case "Right":
                    for (int i = left; i <= right; i++) {
                        result.add(a.get(top).get(i));
                    }
                    top++;
                    break;
                case "Down":
                    for (int i = top; i <= bottom; i++) {
                        result.add(a.get(i).get(right));
                    }
                    right--;
                    break;
                case "Left":
                    for (int i = right; i >= left; i--) {
                        result.add(a.get(bottom).get(i));
                    }
                    bottom--;
                    break;
                case "Up":
                    for (int i = bottom; i >= top; i--) {
                        result.add(a.get(i).get(left));
                    }
                    left++;
            }
            direction = (direction + 1) % 4;
        }
        return result;
    }
}
