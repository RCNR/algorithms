/**
 * 필터.java 1895
 * 주어진대로 코드치기
 * 2중 for 문에 3x3 크기로 돌기 -> 값 넣기 -> 정렬하기 -> 중간값 구하기 -> 결과 리스트에 추가
 */

import java.util.*;
import java.io.*;

public class Main {

    static int n, m, t;
    static int[][] board;
    static List<Integer> res = new ArrayList<>();

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n+3][m+3];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        t = Integer.parseInt(br.readLine());

        filter();

        int cnt = 0;
        for(int i = 0; i < res.size(); i++) {
            if (res.get(i) >= t) cnt++;
        }

        System.out.println(cnt);
    }

    public static void filter() {

        for (int i = 0; i <= n - 3; i++) {
            for (int j = 0; j <= m - 3; j++) {
                List<Integer> li = new ArrayList<>();

                for(int k = i; k < i+3; k++) {
                    for(int z = j; z < j+3; z++) {
                        li.add(board[k][z]);
                    }
                }
                check(li);
            }
        }
    }

    public static void check(List<Integer> check) {
        Collections.sort(check);

        int mid = check.get(check.size() / 2);
        res.add(mid);
    }

}

