import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Test {
    public static void main(String[] args) {
        System.out.println("Hello, World!");

        int[] arr = { 1, 2, 3, 4, 5, 6 };
        int[] arr2 = { 2, 4, 6, 8, 10 };
        int[] arr3 = { 1, 4, 6, 7, 10 };

        int[] result = intersections(arr, arr2, arr3);
        System.out.println(Arrays.toString(result));

        int[] r2 = intersections_2(arr, arr2, arr3);
        System.out.println(Arrays.toString(result));

    }

    /*
     * Given three arrays, return a new array containing intersection of all three
     */
    public static int[] intersections(int[] arr1, int[] arr2, int[] arr3) {
        List<Integer> list1 = Arrays.stream(arr1).boxed().collect(Collectors.toList());
        List<Integer> list2 = Arrays.stream(arr2).boxed().collect(Collectors.toList());
        List<Integer> list3 = Arrays.stream(arr3).boxed().collect(Collectors.toList());

        list1.retainAll(list2);
        list1.retainAll(list3);

        return list1.stream().mapToInt(Integer::intValue).toArray();
    }

    /*
     * Given three arrays, return a new array containing union of all three
     */
    public static int[] intersections_2(int[] arr1, int[] arr2, int[] arr3) {

        for (int i = 0; i < arr1.length; i++) {
            for (int j = 0; j < arr2.length; j++) {
                for (int k = 0; k < arr3.length; k++) {
                    if (arr1[i] == arr2[j] && arr2[j] == arr3[k]) {
                        return new int[] { arr1[i] };
                    }
                }
            }
        }

        return null;

    }

}