import java.util.*;
import java.io.*;

/* 치킨 배달.java 15686
M개의 치킨 집에서 r개를 선택
모든 경우에 따라 치킨 거리의 합을 구하고
그 중 최소값을 출력
*/

public class Main {

    static class Point {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    static int N, M;
    static int[][] board;
    static List<Point> chicken = new ArrayList<>(); // 치킨집 저장
    static List<Point> house = new ArrayList<>(); // 집 저장
    static int res = 0x3fffffff;
    static boolean[] is_visited;
 
    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N+3][N+3];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 1) house.add(new Point(i, j));
                else if (board[i][j] == 2) chicken.add(new Point(i, j));
            }
        }

        is_visited = new boolean[chicken.size() + 3];

        func(0, 0);
        System.out.println(res);

    }

    static void func(int idx, int cnt) { // 치킨집 조합 형성
        
        if (cnt == M) {
            int dist = getDist();
            res = Math.min(res, dist);
            return;
        }

        for(int i = idx; i < chicken.size(); i++) {
            if (!is_visited[i]) {
                is_visited[i] = true;
                func(i + 1, cnt + 1);
                is_visited[i] = false;
            }
        }
    }

    static int getDist() {
        
        int total = 0;

        for(Point p : house) {
            int minsss = 0xfffffff;

            for(int i = 0; i < chicken.size(); i++) {
                if (is_visited[i]) {
                    Point c = chicken.get(i);
                    int dist = Math.abs(p.x - c.x) + Math.abs(p.y - c.y);
                    minsss = Math.min(minsss, dist);
                    }    
            }
            total += minsss;
        }
         return total;
    }
}