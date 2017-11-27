public class Solution {
    public String countAndSay(int a) {
        String sequence = "1";
        for (int i = 1; i < a; i++) {
            char current = sequence.charAt(0);
            int count = 1;
            StringBuilder sb = new StringBuilder();
            for (int j = 1; j < sequence.length(); j++) {
                if (current == sequence.charAt(j)) {
                    count++;
                } else {
                    sb.append(count + Character.toString(current));
                    current = sequence.charAt(j);
                    count = 1;
                }
            }
            sb.append(count + Character.toString(current));
            sequence = sb.toString();
        }
        return sequence;
    }
}
