/**
 * 두 점이 모두 원 내부에 있으면 +0
 * 두 점이 모두 원 밖에 있으면 +0
 * 한 점이 원 안에 있으면 +1
 * 점 내부인지 확인 : 원 중심점과의 거리 r이하이면 내부
 */

import java.util.*;
import java.io.*;

public class Main {
    
    static int T;
    static int x1, y1, x2, y2;
    static int N; // 행성 개수


    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        T = Integer.parseInt(br.readLine());
        while(T-- > 0) {
            st = new StringTokenizer(br.readLine());
            x1 = Integer.parseInt(st.nextToken());
            y1 = Integer.parseInt(st.nextToken());
            x2 = Integer.parseInt(st.nextToken());
            y2 = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(br.readLine());

            int cnt = 0;

            for(int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                int cx = Integer.parseInt(st.nextToken());
                int cy = Integer.parseInt(st.nextToken());
                int r = Integer.parseInt(st.nextToken());

                boolean s = check(x1, y1, cx, cy, r);
                boolean e = check(x2, y2, cx, cy ,r);

                if (s != e) cnt++;
            }

            System.out.println(cnt);
        }

    }

    public static boolean check(int x, int y, int cx, int cy, int r) {
        int dx = cx - x;
        int dy = cy - y;

        return dx * dx + dy * dy < r * r;
    }
}

