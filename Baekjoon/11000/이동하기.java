/**
 * 이동하기.java
 * (r+1, c), (r, c+1), (r+1, c+1) 세 가지 이동하기 때문에 dp를 위치마다 세 번씩 확인
 * dp[i][j] = board[i][j] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) -> 이전에 온 위치에서가장 큰 값과 현재 위치의 값을 더함
 */

import java.util.*;
import java.io.*;

public class Main {

    static int[][] board;
    static int n, m;
    static int[][] dp;
    static int[] dx = {0, -1, -1};
    static int[] dy = {-1, 0, -1};

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n+3][m+3];
        dp = new int[n+3][m+3];

        for(int i = 1 ; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= m; j++) {
                check(i, j);
            }
        }

        System.out.println(dp[n][m]);
    }

    private static void check(int x, int y) {

        for (int dir = 0; dir < 3; dir++) {
            int nx = dx[dir] + x;
            int ny = dy[dir] + y;

            dp[x][y] = Math.max(dp[x][y], board[x][y] + dp[nx][ny]);
        }
    }

}

