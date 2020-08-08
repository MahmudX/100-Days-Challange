/**
 * Find_Numbers_with_Even_Number_of_Digits
 */
public class Find_Numbers_with_Even_Number_of_Digits {

    public int FindNumbers(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            int l = String.valueOf(nums[i]).length();
            if (l % 2 == 0) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {

    }
}