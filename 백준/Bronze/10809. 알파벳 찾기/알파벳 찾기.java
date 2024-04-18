import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder(br.readLine());
        int[] arr = new int[26];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = -1;
        }
        for (int i = 0; i < sb.length(); i++) {
            int idx = sb.charAt(i) - 'a';
            arr[idx] = sb.indexOf(sb.substring(i, i + 1));
        }
        for (int i = 0; i < arr.length; i++) {
            bw.write(arr[i] + " ");
        }
        bw.flush();
        bw.close();
    }
}