import java.math.BigInteger;

public class Solution {
    public ArrayList<BigInteger> toIntList(String s) {
        String[] vStr = s.split("\\.");
        ArrayList<BigInteger> vLst = new ArrayList<BigInteger>();
        for (String part : vStr) {
            vLst.add(new BigInteger(part));
        }
        return vLst;
    }

    public int compareVersion(String a, String b) {
        ArrayList<BigInteger> aVer = toIntList(a);
        ArrayList<BigInteger> bVer = toIntList(b);
        while (aVer.size() < bVer.size()) {
            aVer.add(BigInteger.ZERO);
        }
        while (bVer.size() < aVer.size()) {
            bVer.add(BigInteger.ZERO);
        }
        for (int i = 0; i < aVer.size(); i++) {
            int diff = aVer.get(i).compareTo(bVer.get(i));
            if (diff != 0) {
                return diff;
            }
        }
        return 0;
    }
}
