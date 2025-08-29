/**
 * 가장 큰 정사각형.java 1915
 * 새로 보는 dp 유형이었다. 모르겠어서 이런 방식의 dp접근 방식으로 풀 수 있음을 알았다
 * dp[i][j] = (i, j)가 오른쪽 하단 모서리인 정사각형의 최대 크기 로 정한다
 * 그러면서 dp[i-1][j], dp[i-1][j-1], dp[i][j-1] 중 min 값을 구해 + 1 을 해준다
 * dp[i][j] = k 라면 위 3가지의 값의 최솟값은 k-1이 된다
 */
import java.io.*;
import java.util.*;

public class Main{

    static int n, m;
    static int[][] board;
    static int[][] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        board = new int[n+3][m+3];
        dp = new int[n+3][m+3];

        for(int i = 0; i < n; i++) {
            String line = br.readLine();
            for(int j = 0; j < m; j++) {
                board[i][j] = line.charAt(j) - '0';
            }
        }
        int maxNum = 0;

        for(int i = 0; i < m; i++){
            dp[0][i] = board[0][i];
            maxNum = Math.max(maxNum, dp[0][i]); // 단일 행 처리
        }
        for(int i = 0; i < n; i++){
            dp[i][0] = board[i][0];
            maxNum = Math.max(maxNum, dp[i][0]); // 단일 열 처리
        }



        for(int i = 1; i < n; i++) {
            for(int j = 1; j < m; j++) {
                if(board[i][j] == 1) {
                    dp[i][j] = Math.min(dp[i - 1][j], Math.min(dp[i][j - 1], dp[i - 1][j - 1])) + 1;
                }
//                System.out.print(dp[i][j] + " ");
                maxNum = Math.max(maxNum, dp[i][j]);
            }
//            System.out.println();
        }

        System.out.println(maxNum * maxNum);
    }

}