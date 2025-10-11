/**
 * 넷이 놀기.java 2121
 * 좌표 값 4개가 주어진 가로, 세로 조건을 만족해야한다.
 * 특정 좌표의 x, y 값에 각 가로, 세로 값을 더한 좌표가 존재하는지 확인하면 된다.
 * 좌표 여부를 확인하기 위해 Set을 사용
 * 자표를 나타내기 위해 Pair<x, y>를 사용해도 되지만 이는 객체 동등성을 판다해 eqauls와 hashCode를 오버라이드 해야한다.
 * 따라서 따로 사용자 정의 클래스 없이 문자열로 x, y를 합쳐서 Set에 넣어준다.
 */

import java.io.*;
import java.util.*;

public class Main {

    
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        int row = Integer.parseInt(st.nextToken());
        int column = Integer.parseInt(st.nextToken());


        List<int[]> points = new ArrayList<>();
        Set<String> s = new HashSet<>();

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            points.add(new int[] {x, y});
            s.add(x + "," + y);
        }

        int cnt = 0;

        for (int[] p : points) {
            int curX = p[0];
            int curY = p[1];

            if (s.contains((curX + row) + "," + curY) &&
                s.contains((curX + row) + "," + (curY + column)) &&
                s.contains(curX + "," + (curY + column))) {
                    cnt ++;
                }
        }

        System.out.println(cnt);


    }
}