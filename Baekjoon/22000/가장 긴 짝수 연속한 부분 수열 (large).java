/**
 * 가장 긴 짝수 연속한 부분 수열 (large), 22862
 * 투 포인터를 이용한 답 구하기
 * 처음엔 하나씩 삭제하면서 확인해야하나 싶었지만 시간복잡도 상 불가능
 * 도식화를 해보니 배열을 하나씩 이동하면서 K개를 넘을만큼 삭제한 게 아니라면 삭제했다고 가정하고 문제를 풀 수 있음
 */
import java.io.*;
import java.util.*;

public class Main{

    public static int[] board;
    public static int cnt; // 가능한 길이
    public static int res;
    public static int is_ok; // k의 개수를 초과하는지

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        board = new int[n];

        st = new StringTokenizer(br.readLine());

        for(int i = 0; i < n; i++) {
            board[i] = Integer.parseInt(st.nextToken());
        }

        int en = 0;
        res = -1;

        for (int start = 0; start < board.length; start++) {

            while (en < board.length && is_ok <= k) {

                if (board[en] % 2 == 1) is_ok++;
                else cnt++;
                en++;
            }

//            System.out.println("start: " + start + ", end: " + en + ", cnt: " + cnt + ", is_ok: " + is_ok);

            res = Math.max(res, cnt);


            if(board[start] % 2 == 1) is_ok--;
            else cnt--;


//            System.out.println("start: " + start + ", end: " + en + ", cnt: " + cnt + ", is_ok: " + is_ok);


        }

        System.out.println(res);

    }
}