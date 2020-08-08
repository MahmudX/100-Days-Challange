import java.lang.reflect.Array;
import java.util.Arrays;

public class Squares_of_a_Sorted_Array {
    public int[] sortedSquares(int[] A) {
        for (int i = 0; i < A.length; i++) {
            A[i] = A[i] * A[i];
        }
        Arrays.sort(A);
        return A;
    }
    public static void main(String[] args) {
        
    }
}