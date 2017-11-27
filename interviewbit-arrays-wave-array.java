import java.util.Collections;

public class Solution {
    public ArrayList<Integer> wave(ArrayList<Integer> a) {
        if (a != null && a.size() > 1) {
            Collections.sort(a);
            int temp;
            for (int i = 0; i < a.size() - 1; i = i + 2) {
                temp = a.get(i);
                a.set(i, a.get(i + 1));
                a.set(i + 1, temp);
            }
        }
        return a;
    }
}
