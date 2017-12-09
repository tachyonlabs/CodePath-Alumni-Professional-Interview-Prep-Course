public class Solution {
    public ArrayList<ArrayList<Integer>> anagrams(final List<String> a) {
        HashMap<String, ArrayList<Integer>> words = new HashMap<String, ArrayList<Integer>>();
        ArrayList<ArrayList<Integer>> indicesList = new ArrayList<ArrayList<Integer>>();
        char[] letters;
        String word;
        for (int i = 0; i < a.size(); i++) {
            letters = a.get(i).toCharArray();
            Arrays.sort(letters);
            word = new String(letters);
            if (!words.containsKey(word)) {
                words.put(word, new ArrayList<Integer>());
            }
            words.get(word).add(i + 1);
        }
        for (String key : words.keySet()) {
            indicesList.add(words.get(key));
        }
        return indicesList;
    }
}
