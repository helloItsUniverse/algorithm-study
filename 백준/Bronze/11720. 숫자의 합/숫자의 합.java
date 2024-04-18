import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int sum = 0;
        int N = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder(br.readLine());
        for (int i = 0; i < N; i++) {
            sum += (sb.charAt(i) - '0');
        }
        bw.write(Integer.toString(sum));
        bw.flush();
        bw.close();
    }
}