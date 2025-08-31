/**
 * 욕심쟁이 판다.java 1937
 * 특정 위치에서 움직이기 위해서는 이동하려고 하는 위치 값이 더 큰 경우에만 이동할 수 있다
 * 모든 위치마다 재귀를 돌릴 필요는 없다. 현재 위치에서 이동하려는 위치의 값만 사용해 구한다
 */

import java.io.*;
import java.util.*;

public class Main{

    static int n;
    static int[][] board;
    static int[] dx = {0, 1, -1, 0};
    static int[] dy = {1, 0, 0, -1};
    static int[][] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        board = new int[n+3][n+3];
        dp = new int[n+3][n+3];

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                dp[i][j] = -1;
            }
        }

        int res = -1;

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                res = Math.max(res, func(i, j));
            }
        }

        System.out.println(res);

    }

    public static int func(int x, int y) {

        if (dp[x][y] != -1) return dp[x][y];

        dp[x][y] = 1;

        for (int dir = 0; dir < 4; dir++) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if(nx < 0 || nx >= n || ny < 0 || ny >= n || board[x][y] >= board[nx][ny]) continue;

            if(board[nx][ny] > board[x][y]) dp[x][y] = Math.max(dp[x][y], func(nx, ny) + 1);

        }

        return dp[x][y];
    }



}