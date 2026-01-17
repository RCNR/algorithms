/**
 * 선분 교차 2.java 17387
 * ccw 알고리즘을 이용해 선분 교차 판정
 * 1. x자 교차하여 겹치는 경우
 * 2. 일직선 상에 있는 경우
 * 2-1. 겹치는 경우 (한 점이라도)
 * 2-2. 겹치지 않는 경우
 * 3. 이외의 겹치지 않는 경우
 * 
 * 한 선분을 이루는 두 점과 다른 선분을 이루는 두 점을 각각 ccw 판정
 * 
 */

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;


        st = new StringTokenizer(br.readLine());
        long x1 = Long.parseLong(st.nextToken());
        long y1 = Long.parseLong(st.nextToken());
        long x2 = Long.parseLong(st.nextToken());
        long y2 = Long.parseLong(st.nextToken());

        st = new StringTokenizer(br.readLine());
        long x3 = Long.parseLong(st.nextToken());
        long y3 = Long.parseLong(st.nextToken());
        long x4 = Long.parseLong(st.nextToken());
        long y4 = Long.parseLong(st.nextToken());

        Point p1 = new Point(x1, y1);
        Point p2 = new Point(x2, y2);
        Point p3 = new Point(x3, y3);
        Point p4 = new Point(x4, y4);

        int res = func(p1, p2, p3, p4);
        System.out.println(res);
    }

    static int func(Point a, Point b, Point c, Point d) {

        int res123 = ccw(a, b, c);
        int res124 = ccw(a, b, d);
        int res341 = ccw(c, d, a);
        int res342 = ccw(c, d, b);

        if (res123 * res124 <= 0 && res341 * res342 <= 0) {

            if (res123 * res124 == 0 && res341 * res342 == 0) { // 일직선인 경우 체크 필요
                if (Math.max(a.x, b.x) >= Math.min(c.x, d.x) && Math.max(c.x, d.x) >= Math.min(a.x, b.x) && Math.max(a.y, b.y) >= Math.min(c.y, d.y) && Math.max(c.y, d.y) >= Math.min(a.y, b.y)) {
                    return 1;
                }
                else{
                    return 0;
                }
            }
            return 1; // X 자
        }

        return 0;
    }

    static int ccw(Point p1, Point p2, Point p3) {
        long val = (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x);

        if (val > 0) return 1;
        if (val < 0) return -1;
        return 0;
    }

    static class Point {
        long x, y;

        Point(long x, long y) {
            this.x = x;
            this.y = y;
        }
    }



}

