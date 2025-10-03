package Leetcode;

import java.util.Arrays;

public class Two_Sum_Easy {
    public static void main(String[] args) {
        int[] nums = {2,7,11,15};
        int target = 9;
        System.out.println(Arrays.toString(twoSum(nums, target)));
    }
    public static int[] twoSum(int[] nums, int target) {
        int[] out = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    out[1] = j;
                    out[0] = i;
                }
            }
        }
        return (out);

    }
}
