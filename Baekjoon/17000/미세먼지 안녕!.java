import java.util.*;
import java.io.*;

// 먼지 뿌리기
// 먼지 합치기
// 먼지 한칸씩 밀기

/**
 * 
 * 주어진 시간동안 1. 먼지를 뿌린다 2. 공기청정기를 작동시킨다 => 반복한다
 * 마지막에 남은 먼지의 양을 구한다
 * 
 * 조건에 맞게 먼지를 뿌리고
 */

public class Main {

    static int R, C, T;
    static int m1_x, m1_y;
    static int m2_x, m2_y;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());

        int is_first = 0;

        int[][] board = new int[R+3][C+3];

        for(int i = 1; i <= R; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 1; j <= C; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if(board[i][j] == -1 && is_first == 0) {
                    m1_x = i;
                    m1_y = j;
                    is_first = 1;
                }
                else if(board[i][j] == -1 && is_first == 1) {
                    m2_x = i;
                    m2_y = j;
                }

            }
        }


        for(int i = 0; i < T; i++) {
            board = spread(board); // 먼지 뿌리기
            clean(board); // 공기청정기
        }

        int ret = 0;

        for(int i = 1; i <= R; i++) {
            for(int j = 1; j <= C; j++) {
                if(board[i][j] > 0) ret += board[i][j];
            }
        }

        System.out.println(ret);

    }

    private static int[][] spread(int[][] check) {
        int[][] dust = new int[R+3][C+3];

        dust[m1_x][m1_y] = -1;
        dust[m2_x][m2_y] = -1;

        int[] dx = {0, 1, -1 ,0};
        int[] dy = {1, 0, 0, -1};

        for(int x = 1; x <= R; x++) {
            for(int y = 1; y <= C; y++) {
                if(check[x][y] > 0) {
                    int originalAmount = check[x][y];
                    int amount = originalAmount / 5;
                    int cnt = 0; // 뿌린 개수

                    for(int dir = 0; dir < 4; dir++) {
                        int nx = x + dx[dir];
                        int ny = y + dy[dir];

                        if(nx < 1 || nx > R || ny < 1 || ny > C) continue;
                        if(check[nx][ny] == -1) continue;

                        dust[nx][ny] += amount;
                        cnt += 1;
                    }

                    // 남은 양
                    dust[x][y] += originalAmount - (amount * cnt);

                }
            }
        }

        return dust;
    }

    private static void clean(int[][] check) {

        for(int i = m1_x; i > 1; i--) {
            check[i][1] = check[i-1][1];
        }

        for(int j = 1; j < C; j++) {
            check[1][j] = check[1][j+1];
        }

        for(int i = 1; i < m1_x; i++) {
            check[i][C] = check[i+1][C];
        }

        for(int j = C; j > 2; j--) {
            check[m1_x][j] = check[m1_x][j-1];
        }

        check[m1_x][m1_y] = -1;
        check[m1_x][m1_y + 1] = 0; // 청정기 옆

        // ----------------------- 밑에는 시계

        for(int i = m2_x; i < R; i++) {
            check[i][1] = check[i+1][1];
        }

        for(int j = 1; j < C; j++) {
            check[R][j] = check[R][j+1];
        }

        for(int i = R; i > m2_x; i--) {
            check[i][C] = check[i-1][C];
        }

        for(int j = C; j > 2; j--) {
            check[m2_x][j] = check[m2_x][j-1];
        }

        check[m2_x][m2_y] = -1;
        check[m2_x][m2_y + 1] = 0; // 청정기 옆

    }

}