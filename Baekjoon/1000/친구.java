/**
 * 친구 1058
 * 나와 연결된 친구와 그 친구의 친구까지 구하는 문제
 * 단순하게 생각하면 되는데, 어떻게 하면 그럴싸하게 풀까를 고민하는 바람에 코드가 이상해졌다
 */

import java.util.*;
import java.io.*;


public class Main {

    public static int[] is_visited;
    public static int n;
    public static int[][] board;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        board = new int[n+3][n+3];

        for(int i = 1; i <= n; i++) {
            String s = br.readLine().trim();
            for(int j = 0; j < n; j++) {
                if (s.charAt(j) == 'N') board[i][j+1] = 0;
                else board[i][j+1] = 1;
            }
        }

        int mx_cnt = 0;

        for(int i = 1; i <= n; i++) {
            boolean[] is_visited = new boolean[n+1];
            int cnt = 0;

            for(int j = 1; j <= n; j++) {
                if (i == j) continue;

                if (board[i][j] == 1) {
                    if(!is_visited[j]) {
                        is_visited[j] = true;
                        cnt++;
                    }

                    for(int k = 1; k <= n; k++) {
                        if(board[j][k] == 1) {
                            if(board[j][k] == 1 && !is_visited[k] && k != i) {
                                is_visited[k] = true;
                                cnt++;
                            }
                        }
                    }
                }
            }
            mx_cnt = Math.max(mx_cnt, cnt);
        }
        System.out.println(mx_cnt);

    }



}


