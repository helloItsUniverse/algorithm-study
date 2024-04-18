import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int a, b;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] sumArr = new int[n];
        for (int i = 0; i < n; i++) {
            a = sc.nextInt();
            b = sc.nextInt();
            sumArr[i] = a + b;
        }
        for (int sum: sumArr) {
            System.out.println(sum);
        }
    }
}
