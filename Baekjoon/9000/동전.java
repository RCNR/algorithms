// 동전 9084
/**
 * dp[i] = dp[i-1] + dp[i-2] 로 풀면 중복이 되기에 경우의 수가 올바르지 않게 된다
 * i 번째 동전까지 썼을 때 j원 만드는 경우의 수를 구해야 한다. => dp[i][j]
 * 두 가지 경우로 볼 수 있다
 * 1. i 번째 동전을 사용하지 않은 경우 -> dp[i-1][j]
 * +
 * 2. i 번째 동전을 1개 이상 사용한 경우 -> dp[i][j-cost[i]] => 1 ~ i까지 동전을 다 사용하는 게 가능
 */
import java.io.*;
import java.util.*;

public class Main{

    public static int[] cost = new int[22];
    public static int[][] dp = new int[22][10005];


    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());

        while(t-- > 0) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            for(int i = 0; i < n; i++) {
                cost[i] = Integer.parseInt(st.nextToken());
                dp[i][0] = 1;
            }
            st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());

            for(int i = 0; i < n; i++) dp[i][0] = 1;

            for(int i = 0; i < n; i++) {
                for(int j = 1; j <= m; j++) {
                    dp[i][j] = 0;

                    if(i - 1 >= 0) dp[i][j] += dp[i-1][j]; // i번째 동전 0개 사용
                    if(j - cost[i] >= 0) dp[i][j] += dp[i][j - cost[i]]; // i번째 동전 1개 이상 사용
                }
            }

            System.out.println(dp[n-1][m]);
        }

    }
}