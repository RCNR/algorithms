/**
 * 색종이 - 2.java 2567
 * 주어진 영역만큼 1로 채우고, 1인 부분의 상하좌우를 탐색하여 0이거나 범위를 벗어나면 개수(길이)증가
 */

import java.util.*;
import java.io.*;

public class Main {

    static int n;
    static int res;
    static boolean[][] board = new boolean[103][103];
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        List<int[]> li = new ArrayList<>();

        n = Integer.parseInt(br.readLine());
        for(int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            li.add(new int[]{x, y});
            paint(x, y);
        }
        check();

        System.out.println(res);

    }

    public static void check() {
        for(int i = 0; i < 100; i++) {
            for(int j = 0; j < 100; j++) {
                if (board[i][j]) {
                    for(int dir = 0; dir < 4; dir++) {
                        int nx = i + dx[dir];
                        int ny = j + dy[dir];
                        if (nx < 0 || nx >= 100 || ny < 0 || ny >= 100){
                            res++;
                            continue;
                        }
                        if (!board[nx][ny]){
                            res++;
                        }
                    }
                }

            }
        }
    }

    public static void paint(int x, int y) {
        for(int i = x; i < x+10; i++) {
            for(int j = y; j < y+10; j++) {
                board[i][j] = true;
            }
        }
    }
}