/**
 * 점프.java 1890
 * dp 이용해서 경우의 수 구하기
 * x축, y축 각각 이동할 수 있는 칸 수가 주어질 때
 * (0,0)에서 (n-1,n-1)까지 도달하는 경우의 수 구하기
 * 상태 전이 -> 이전에 이동했던 만큼 추가로 갈 수 있음
 */

import java.util.*;
import java.io.*;

public class Main {

    static int[][] board;
    static long[][] dp;
    static int n;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());

        board = new int[n+3][n+3];
        dp = new long[n+3][n+3];
//        for(long[] row : dp) {
//            Arrays.fill(row, -1);
//        }

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dp[0][0] = 1;

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {

                if (dp[i][j] != 0) {
                    move(i, j); //
                }
            }
        }
        System.out.println(dp[n-1][n-1]);
/*
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                System.out.print(dp[i][j] +  " ");
            }
            System.out.println();
        }*/

    }

    public static void move(int x, int y) {

        if(x == n-1 && y == n-1) return; // (n-1, n-1) 온거는 제외

        int moveDist = board[x][y];

        if (x + moveDist < n) dp[x + moveDist][y] += dp[x][y] ;
        if (y + moveDist < n) dp[x][y + moveDist] += dp[x][y] ;


    }
}