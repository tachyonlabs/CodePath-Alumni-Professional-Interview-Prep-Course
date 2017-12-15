public class Solution {
    public int nchoc(int A, ArrayList<Integer> B) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((x, y) -> y - x);
        for (int i = 0; i < B.size(); i++) {
            maxHeap.add(B.get(i));
        }
        long howMany = 0;
        int bag;
        for (int i = 0; i < A; i++) {
            bag = maxHeap.poll();
            howMany += bag;
            maxHeap.add(bag / 2);
        }
        return (int) (howMany % 1000000007);
    }
}
