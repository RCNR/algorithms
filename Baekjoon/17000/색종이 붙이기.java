// 색종이 붙이기 17136
// 10 x 10 종이에 색종이를 최소 개수로 붙여야 한다.
// 색종이가 1x1 ~ 5x5가 있고 최소 개수가 되기 위해 그리디스럽게 5x5로 먼저 접근해본다
// 브루트포스로 접근하여 모든 색종이를 다 붙여보지만 붙일 수 없는 경우라면 더 보지 않고 return 하는 게 낫다
// 붙일 수 없는 경우는 각 색종이를 다 사용한 경우 및 범위를 넘어간 경우, 붙인 색종이를 기존 개수보다 더 많이 사용한 경우이다.
// 색종이를 사용해 붙였다면 그 범위는 0으로 처리하여 행여나 다음번에 보게 되는 것을 막는다
// 색종이를 붙여 0으로 만든 경우 이후의 경우의 수를 더 봐야하기에 다시 1로 복구 시킨다.

import java.io.*;
import java.util.*;

public class Main{

    public static int[][] board = new int[12][12];
    public static int[] paperCount = {0, 5, 5, 5, 5, 5};
    public static int res = Integer.MAX_VALUE;


    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        for(int i = 0; i < 10; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < 10; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        func(0, 0);
        if(res == Integer.MAX_VALUE) System.out.println(-1);
        else System.out.println(res);

    }

    private static void func(int loc, int cnt) {

        if (loc == 100) {
            res = Math.min(res, cnt);
            return;
        }

        if (res <= cnt) return;

        int n = loc % 10;
        int m = loc / 10;

        if(board[n][m] == 1) {

            for(int i = 5; i >= 1; i--) {
                if(paperCount[i] > 0 && check(n, m, i)) {
                    paperCount[i]--;
                    fill(n, m, i, 0); // 1을 0으로 채우기
                    func(n * m + 1, cnt + 1);

                    fill(n, m, i, 1); // 0으로 채웠던 부분 다시 1로 복구
                    paperCount[i]++;

                }
            }
        } else {
            func(loc + 1, cnt);
        }

    }

    private static boolean check(int n, int m, int num) {

        if(n + num > 10 || m + num > 10) return false;

        for (int i = n; i < n + num; i++) {
            for (int j = m; j < m + num ; j++) {
                if(board[i][j] == 0) return false;
            }
        }

        return true;
    }

    private static void fill(int n, int m, int num, int k) {

        for(int i = n; i < n + num; i++) {
            for(int j = m; j < m + num; j++) {
                board[i][j] = k;
            }
        }
    }
}