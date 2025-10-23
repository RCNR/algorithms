/**
 * 나이트 투어.java 1331
 * 고려해야할 조건 : 다음 입력 값이 나이트가 이동할 수 있는지, 총 이동해서 모든 배열을 다 방문했는지, 마지막 위치에서 처음 위치로 이동할 수 있는지
 * 빡구현
 */

import java.util.*;
import java.io.*;

public class Main {

    static int[] dx = {1, 1, -1, -1, 2, -2, 2, -2};
    static int[] dy = {2, -2, 2, -2, 1, -1, -1, 1};
    static boolean[][] is_visited = new boolean[7][7];

    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        boolean flag = true;
        int startX = 0, startY = 0, prevX = 0, prevY = 0;

        for(int i = 0; i < 36; i++) {
            String s = br.readLine();
            int m = s.charAt(0) - 'A' + 1;
            int n = s.charAt(1) - '0';

            if (is_visited[n][m]) flag = false;
            is_visited[n][m] = true;

            if (i == 0) {
                startX = n; startY = m;
            }
            else {
                boolean move = false;
                for(int dir = 0; dir < 8; dir++) {
                    if (prevX + dx[dir] == n && prevY + dy[dir] == m) {
                        move = true;
                        break;
                    }
                }

                if (!move) flag = false;
            }
            prevX = n; prevY = m;
        }

        int cnt = 0;
        for(int i = 1; i <= 6; i++) {
            for(int j = 1; j <= 6; j++) {
                if(is_visited[i][j]) cnt++;
            }
        }
        if (cnt != 36) flag = false;

        boolean lastCheck = false;

        for(int dir = 0; dir < 8; dir++) {
            if(prevX + dx[dir] == startX && prevY + dy[dir] == startY) {
                lastCheck = true;
                break;
            }
        }
        if (!lastCheck) flag = false;

        System.out.println(flag ? "Valid" : "Invalid");
    }


}