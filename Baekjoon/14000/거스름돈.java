// 14916 거스름돈
import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        int cnt = 0;

        while (n >= 0) {
            if (n % 5 == 0) {
                cnt += n / 5;
                bw.write(cnt +"");
                bw.flush();
                bw.close();

                System.exit(0);
            } else {
                n -= 2;
                cnt += 1;
            }
        }
        bw.write(String.valueOf(-1));

        bw.flush();
        bw.close();
    }
}
