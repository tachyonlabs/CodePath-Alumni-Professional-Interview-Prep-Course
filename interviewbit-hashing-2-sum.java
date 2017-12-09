public class Solution {
    public ArrayList<Integer> twoSum(final List<Integer> a, int b) {
        ArrayList<Integer> returnIndices = new ArrayList<Integer>();
        HashMap<Integer, ArrayList<Integer>> nums = new HashMap<Integer, ArrayList<Integer>>();
        for (int i = 0; i < a.size(); i++) {
            int target = b - a.get(i);
            if (nums.containsKey(target)) {
                returnIndices.add(nums.get(target).get(0) + 1);
                returnIndices.add(i + 1);
                return returnIndices;
            }
            if (nums.containsKey(a.get(i))) {
                nums.get(a.get(i)).add(i);
            } else {
                ArrayList<Integer> al = new ArrayList<Integer>();
                al.add(i);
                nums.put(a.get(i), al);
            }
        }
        return returnIndices;
    }
}
