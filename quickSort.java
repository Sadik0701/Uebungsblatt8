import java.util.Arrays;
import static java.lang.Math.abs;
import java.util.Random;

public class quickSort {

    public static int partition(int[] array, int left, int right) {
        int i = left;
        int j = right - 1;
        int pivot = array[right];
        int temp = 0;

        while (i < j) {
            while (i < j && array[i] <= pivot) {
                i += 1;
            }
            while (j > i && array[j] > pivot) {
                j -= 1;
            }
            if (array[i] > array[j]) {
                temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
        if (array[i] > pivot) {
            temp = array[i];
            array[i] = array[right];
            array[right] = temp;
        } else {
            i = right;
        }
        return i;
    }

    public static void quickSort(int[] array, int left, int right) {
        if (left < right) {
            int pivotLocation = partition(array, left, right);
            quickSort(array, left, pivotLocation - 1);
            quickSort(array, pivotLocation + 1, right);
        }
    }

    public static void main(String[] args) {

        int arrayStart = 0;
        int[] array_sizes =  new int[]{10, 100, 500, 1000, 1500, 2000, 2500, 3000, 5000, 7500, 10000};
        for (int i = 0; i < array_sizes.length; i++){
            Random rd = new Random();
            int[] arr = new int[array_sizes[i]];
            for (int j = 0; j < arr.length; j++) {
                arr[i] = rd.nextInt(); // storing random integers in an array
            }
            long timeStart = System.nanoTime();
            quickSort(arr, arrayStart, arr.length-1);
            long timeEnd = System.nanoTime();
            System.out.println("Verlaufszeit der Schleife: " + (timeEnd - timeStart) + " Millisek.");
        }
    }
}