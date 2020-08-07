public class Solution
{
    public int[] RunningSum(int[] nums)
    {
        //https://leetcode.com/problems/running-sum-of-1d-array/submissions/
        int n = nums.Length;
        int[] res = new int[n];
        res[0] = nums[0];
        for (int i = 1; i < n; i++)
        {
            res[i] = nums[i] + res[i - 1];
        }
        return res;
    }
}