public class Solution {
    /**
     * @param A: lists A
     * @param B: lists B
     * @return: the index mapping
     */
    public int[] anagramMappings(int[] A, int[] B) {
        int[] mapping = new int[A.length];
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < B.length; i++) {
            set.add(i);
        }

        for (int i = 0; i < A.length; i++) {
            for (int index : set) {
                if (B[index] == A[i]) {
                    mapping[i] = index;
                    set.remove(index);
                    break;
                }
            }
        }

        return mapping;
    }
}
