/**
 * 사탕 게임.java 3085
 * 문제 조건은 간단
 * 완전 탐색으로 풀면됨
 * 모든 칸 오른쪽, 아래쪽 교환 - 2 x N^2
 * 교환마다 검사 2 * N^2
 * 총 O(N^4) 
 */

import java.util.*;
import java.io.*;

public class Main {

    static char[][] board;
    static int n;
    static int res;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        board = new char[n+3][n+3];
        for(int i = 0; i < n; i++) {
            board[i] = br.readLine().toCharArray();
        }

        for(int i = 0; i < n; i++) {
            for (int j = 0; j < n ; j++) {
                // 오른쪽과 교환
                if (j < n - 1) {
                    swap(i, j, i, j+1);
                    RowColumnCount();
                    swap(i, j, i, j+1);
                }

                // 밑에와 교환
                if (i < n - 1) {
                    swap(i, j, i+1, j);
                    RowColumnCount();
                    swap(i, j, i+1, j);
                }
            }
        }

        System.out.println(res);
    }

    public static void RowColumnCount() {

        // row 개수
        for(int i = 0; i < n; i++) {
            int cnt = 1;
            for (int j = 0; j < n-1; j++) {
                if (board[i][j] == board[i][j+1]) cnt++;
                else {
                    res = Math.max(res, cnt);
                    cnt = 1;
                }
            }
            res = Math.max(res, cnt);
        }

        // col 개수
        for(int j = 0; j < n; j++) {
            int cnt = 1;
            for(int i = 0 ; i < n-1; i++) {
                if (board[i][j] == board[i+1][j]) cnt++;
                else {
                    res = Math.max(res, cnt);
                    cnt = 1;
                }
            }
            res = Math.max(res, cnt);
        }
    }

    public static void swap(int x1, int y1, int x2, int y2) {
        char temp = board[x1][y1];
        board[x1][y1] = board[x2][y2];
        board[x2][y2] = temp;
    }


}

