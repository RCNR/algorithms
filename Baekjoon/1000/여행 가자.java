import java.util.*;
import java.io.*;

/*
여행 가자.java 1976
여행 계획에 속한 도시들이 모두 연결되어 있는지 확인하는 문제
union-find 알고리즘을 사용
입력이 인접 행렬이 되어있다.
행렬로 입력받아 루프를 돌면서 그 value가 1이면 i와 j를 union한다
*/

public class Main {

    static int[][] board;
    static int n;
    static int m;
    static int[] route;
    static int ret;
    static int[] parent;

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        board = new int[n+3][n+3];
        parent = new int[n+3];

        for(int i = 1; i <= n; i++) parent[i] = i;

        for(int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 1; j <= n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        route = new int[m+3];
        st = new StringTokenizer(br.readLine());
        for(int i = 1; i <= m; i++) {
            route[i] = Integer.parseInt(st.nextToken());
        }

        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= n; j++) {
                if(board[i][j] == 1) {
                    defUnion(i, j);
                }
            }
        }


        ret = find(route[1]);

        for(int i = 2; i <= m; i++) {
            if(ret != find(route[i])) {
                System.out.println("NO");
                System.exit(0);
            }
        }

        System.out.println("YES");


    }

    public static void defUnion(int u, int v) {

        u = find(u);
        v = find(v);
        if (u != v) parent[v] = u;
    }

    public static int find(int u) {

        if (u == parent[u]) return u;
        return parent[u] = find(parent[u]);
    }
}