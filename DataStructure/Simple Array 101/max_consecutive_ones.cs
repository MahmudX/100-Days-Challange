using System;
using System.Diagnostics;

namespace MaxConsecutiveOnes
{
    public class Program
    {
        public int FindMaxConsecutiveOnes(int[] nums)
        {
            int max = 0, counter = 0;
            foreach (var item in nums)
            {
                Console.WriteLine(item);
                if (item == 1)
                {
                    counter++;
                    if (counter >= max)
                        max = counter;
                }
                else
                    counter = 0;
            }
            return max;
        }
        public static void main()
        {
            int[] a = new int[] { 1 };
            Console.WriteLine(FindMaxConsecutiveOnes(a));
        }
    }
}
