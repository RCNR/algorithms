/**
 * 백준 15591번: MooTube (Silver)
 * 그래프 탐색
 * dfs를 이용해 특정 노드에서 시작하여 간선의 가중치가 k 이상인 노드들을 탐색한다.
 */

import java.util.*;
import java.io.*;

public class Main {

    static class Pair {
        int end;
        int cost;

        public Pair(int end, int cost) {
            this.end = end;
            this.cost = cost;
        }
    }

    static int N, Q;
    static List<Pair>[] adj;
    static boolean[] isVisited;
    static int cnt;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        adj = new ArrayList[N+3];

        for(int i = 1; i <= N; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            adj[u].add(new Pair(v, cost));
            adj[v].add(new Pair(u, cost));
        }

        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            int u = Integer.parseInt(st.nextToken());
            cnt = 0;
            isVisited = new boolean[N+3];

            dfs(u, k);
            sb.append(cnt).append('\n');
        }

        System.out.println(sb);
    }

    private static void dfs(int cur, int k) {

        isVisited[cur] = true;

        for (Pair nxt : adj[cur]) {
            if (!isVisited[nxt.end] && nxt.cost >= k) {
                cnt++;
                dfs(nxt.end, k);
            }
        }
    }
}

