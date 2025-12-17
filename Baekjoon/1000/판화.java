/**
 * 판화.java 1730
 * 조건에 맞게 잘 나타내기
 * 단지 조금 더 괜찮게 할 수 있는 방법 생각하기
 */

import java.util.*;
import java.io.*;


public class Main {
    static int n;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        String s = br.readLine();

        boolean[][] v = new boolean[n][n];
        boolean[][] h = new boolean[n][n];

        int x = 0;
        int y = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int nx = x, ny = y;

            if (c == 'D') nx++;
            else if (c == 'U') nx--;
            else if (c == 'R') ny++;
            else if (c == 'L') ny--;

            if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;

            if (c == 'D' || c == 'U') v[x][y] = v[nx][ny] = true;
            else h[x][y] = h[nx][ny] = true;

            x = nx;
            y = ny;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (v[i][j] && h[i][j]) sb.append('+');
                else if (v[i][j]) sb.append('|');
                else if (h[i][j]) sb.append('-');
                else sb.append('.');
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }
}


