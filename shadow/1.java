class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int remain = target - nums[i];
            if (map.containsKey(remain)) {
                return new int[] {map.get(remain), i};
            }
            map.put(nums[i], i);
        }

        throw new IllegalArgumentException("no solution");
    }
}
