/**
 * 귀걸이.java 1380
 * Hash 적당히 잘 사용하기
 */

import java.util.*;
import java.io.*;


public class Main {


    public static void main(String[] args) throws Exception {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int cnt = 0;
        while (true) {
            int n = Integer.parseInt(br.readLine());
            if(n == 0) break;
            String[] board = new String[n + 1];

            Map<Integer, Integer> m = new HashMap<>();

            for (int i = 0; i < n; i++) {
                board[i] = br.readLine();
            }

            for (int i = 0; i < n * 2 - 1; i++) {
                st = new StringTokenizer(br.readLine());
                int num = Integer.parseInt(st.nextToken());
                char c = st.nextToken().charAt(0);

                m.put(num, m.getOrDefault(num, 0) + 1);
            }

            for (Integer key : m.keySet()) {
                if (m.get(key) == 1) {
                    System.out.println(++cnt + " " + board[key - 1]);
                }
            }


        }
    }


}