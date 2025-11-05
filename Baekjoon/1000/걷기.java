// 걷기 1459
// 봐야할 것은 2 * w <= s인 경우와 그렇지 않은 경우
// 그렇지 않은 경우에서 w > s인 경우와 그렇지 않은 경우이다.
// 이는 그림을 통해 여러 상황을 그려보고 조건을 나누게 되었다.

import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        long x = Integer.parseInt(st.nextToken());
        long y = Integer.parseInt((st.nextToken()));
        long w = Integer.parseInt(st.nextToken());
        long s = Integer.parseInt(st.nextToken());

        long result = 0;

        if (2 * w <= s) {
            result = (x + y) * w;
        } else {
            long small = Math.min(x, y);
            result = small * s;
            long rest = Math.abs(x - y);

            if (w > s) {
                if (rest % 2 == 0) result += (rest * s);
                else result += (rest -1) * s + w;
            }
            else {
                result += rest * w;
            }

        }

        bw.write(String.valueOf(result));
        bw.flush();
    }


}
