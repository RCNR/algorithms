/**
 * 내려가기.java 2096
 * dp를 이용해 풀 수 있다.
 * 현재 위치에서 올 수 있는 위치는 3가지 이므로
 * 현재 위치의 값 + 이전 위치에서 올 수 있는 위치의 최대값을 더해주면 된다.
 * 최소값도 같은 방식으로 구할 수 있다.
 * 다만 최솟값을 구할 때는 초기화가 0으로 되어있기에 인덱스를 나눠서 계산한다.
 */

import java.util.*;
import java.io.*;

public class Main {

    static long[][] dp = new long[100002][5];
    static long[][] a = new long[100002][5];
    static int n;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        for(int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 1; j <= 3; j++) {
                a[i][j] = Long.parseLong(st.nextToken());
            }
        }

        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= 3; j++) {
                dp[i][j] = Math.max(dp[i-1][j-1], Math.max(dp[i-1][j], dp[i-1][j+1])) + a[i][j];
            }
        }

        System.out.print(Arrays.stream(dp[n]).max().getAsLong() + " ");


        for(int i = 0; i < dp.length; i++) Arrays.fill(dp[i], 0);


        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= 3; j++) {
                if (j == 2) {
                    dp[i][j] = Math.min(dp[i-1][j-1], Math.min(dp[i-1][j], dp[i-1][j+1])) + a[i][j];
                }

                else if (j == 1) {
                    dp[i][j] = Math.min(dp[i-1][j], dp[i-1][j+1]) + a[i][j];
                }
                else {
                    dp[i][j] = Math.min(dp[i-1][j], dp[i-1][j-1]) + a[i][j];
                }
            }
        }

        System.out.println(Arrays.stream(Arrays.copyOfRange(dp[n], 1, 4)).min().getAsLong());

//          for(int i = 1; i <= 3; i++) {
//             System.out.println(dp[n][i]);
//         }



    }
}