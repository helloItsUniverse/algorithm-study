import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int hStart;
        int hEnd;
        int sum = 0;
        Scanner sc = new Scanner(System.in);
//        System.out.print("N M 입력: ");
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] arr = new int[N + 1];
        int[] arrOut = new int[M];

        for (int i = 1; i <= N; i++) {
//            System.out.println("총 "+ N + "번째 중 " + (i + 1) + "번째 숫자 입력" );
            arr[i] = arr[i-1] + sc.nextInt();
        }
//        System.out.println(Arrays.toString(arr));

        for (int i = 0; i < M; i++) {
            hStart = sc.nextInt();
            hEnd = sc.nextInt();
            arrOut[i] = arr[hEnd] - arr[hStart - 1];

        }
        for (int out : arrOut) {
            System.out.println(out);
        }
    }
}
