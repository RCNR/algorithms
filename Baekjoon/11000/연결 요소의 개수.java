// 연결 요소의 개수 11724
// for문을 사용해 1~N까지 노드를 탐색한다. 이때 dfs 사용하여 지나간 경로는 visit 체크를 해주고 아직 방문하지 않았다는 것은 연결 요소의 시작이기에 +1을 해준다.

import java.io.*;
import java.util.*;

public class Main{

    public static ArrayList<Integer>[] adj;
    public static boolean is_visited[];
    
    public static void main(String[] args) {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        adj = new ArrayList[n+3];
        is_visited = new boolean[n+3];

        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            adj[u].add(v);
            adj[v].add(u);
        }

        int cnt = 0;

        for(int i = 1; i <= n; i++) {
            if (!is_visited[i]) {
                cnt++;
                dfs(i);
            }
        }
        System.out.println(cnt);
    }

    private static void dfs(int v) {
        
        if(is_visited[v]) return;

        is_visited[v] = true;

        for(int next : adj[v]) {
            if(!is_visited[next]) dfs(next);
        }
    }
}