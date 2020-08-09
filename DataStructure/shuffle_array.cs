using System;
public class Solution {
    public int[] Shuffle(int[] nums, int n) {
        int counter = 0;
        int[] arr = new int[n*2];
        for(int i = 0; i < n; i++ )
        {
            arr[counter] = nums[i];
            counter++;
            arr[counter] = nums[n+i];
            counter++;
        }
        return arr;
    }
    public static void main()
    {
        Console.WriteLine("Leet Code Problem no = 1470 [Easy]")
        //https://leetcode.com/problems/shuffle-the-array/
    }
}