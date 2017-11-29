public class Solution {
    public String intToRoman(int a) {
        int[] decimals = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] romans = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < decimals.length; i++) {
            while (a >= decimals[i]) {
                a -= decimals[i];
                sb.append(romans[i]);
            }
        }
        return sb.toString();
    }
}
