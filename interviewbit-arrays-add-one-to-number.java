public class Solution {
    public ArrayList<Integer> plusOne(ArrayList<Integer> a) {
        int carry = 1;
        for (int i = a.size() - 1; i >= 0; i--) {
            int sum = a.get(i) + carry;
            a.set(i, sum % 10);
            carry = sum / 10;
        }
        if (carry == 1) {
            a.add(0, 1);
        }
        while (a.get(0) == 0) {
            a.remove(0);
        }
        return a;
    }
}
