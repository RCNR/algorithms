// 가장 긴 증가하는 부분 수열 11053

import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int[] board = new int[1003];
    static int[] dp = new int[1003];
    static int n;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            dp[i] = -1;
        }

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        for (int i = 0; i < n; i++) {
            board[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < n; i++) {
            func(i);
        }

        int res = -10000;
        for (int i = 0; i < n; i++) {
            res = Math.max(res, dp[i]);
        }

        System.out.println(res);

        br.close();
        bw.flush();
        bw.close();
    }

    static int func(int cur) {

        if (dp[cur] == -1) {

            dp[cur] = 1;

            for (int i = cur - 1; i >= 0; i--) {
                if (board[i] < board[cur]) { // 앞 수가 더 작다면
                    dp[cur] = Math.max(dp[cur], func(i) + 1);
                }
            }
        }
        return dp[cur];
    }
}
