/**
 * DNA.java 1969
 * 문자열을 이용한 구현, 그리디 문제
 * A, C, G, T 네 개의 문자로 이루어진 DNA 염기서열
 * haming distance를 구하기 위해, 각 column에서 가장 많이 등장하는 문자를 찾고,
 * 그 문자를 제외한 나머지 문자들의 개수를 더하면 된다.
 * 가장 많이 등장하는 단어가 여러 개면 사전 순이기에, 사전을 보장해주는 TreeMap을 사용
 * 따라서 같아도 A C G T 순으로 정렬이 되어있기에, 가장 앞에 있는 key를 선택하게 된다.
 */

import java.io.*;
import java.util.*;


public class Main {

    static String[] board;
    static int cnt = 0;
    static StringBuffer sb = new StringBuffer();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        board = new String[n+2];
        for (int i = 0; i < n; i++) {
            board[i] = br.readLine();
        }

//        System.out.println(Arrays.toString(Arrays.stream(board).toArray()));
        for (int j = 0; j < m; j++) {
            Map<Character, Integer> map = new TreeMap<>();
            for (int i = 0; i < n; i++) {
                map.put(board[i].charAt(j), map.getOrDefault(board[i].charAt(j), 0) + 1);
            }
            // map에서 가장 큰 value를 갖고 있는 key를 찾기 + 정렬을 통해 가장 작은 아스키코드 key 찾기(TreeMap)
            int maxNum = 0;
            char maxKey = ' ';

            for (char key : map.keySet()) {
                if (map.get(key) > maxNum) {
                    maxNum = map.get(key);
                    maxKey = key;
                }
            }
            sb.append(maxKey);
            cnt += (n - maxNum);
        }

        System.out.println(sb);
        System.out.println(cnt);


    }

}