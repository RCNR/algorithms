import java.util.*;
import java.io.*;
import java.util.stream.IntStream;

/**
 * 17835 면접보는 승법이네
 * 
 * 각 지역에서 면접장까지 가는 최단거리로 계산하면 수가 너무 커서 시간복잡도에 못 미치게 될 것 - 모든 지역을 다 봐야함
 * -> 면접장에서 각 지역까지 가는 최단거리로 -> 면접장 기준으로
 */

public class Main {

    static final long INF = Long.MAX_VALUE;
    static int n, m, k; // 도시 개수, 도로 개수, 면접장 개수
    static List<List<Node>> adj = new ArrayList<>();
    static long[] dist;
    static PriorityQueue<Node> pq = new PriorityQueue<>();

    static class Node implements Comparable<Node> {

        long cost;
        int vertex;

        Node(long cost, int vertex) {
            this.cost = cost;
            this.vertex = vertex;
        }

        @Override
        public int compareTo(Node o) {
            return Long.compare(this.cost, o.cost);
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        dist = new long[n + 1];
        Arrays.fill(dist, INF);

        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            long c = Integer.parseInt(st.nextToken());
            adj.get(v).add(new Node(c, u)); // 기존 u -> v를 v -> u 로 변경
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) {
            int num = Integer.parseInt(st.nextToken());
            dist[num] = 0;
            pq.offer(new Node(0, num));
        }

        func();

        int maxIndex = IntStream.range(1, dist.length)
                .reduce((i, j) -> dist[i] >= dist[j] ? i : j)
                .orElse(0);
        System.out.println(maxIndex);
        System.out.println(dist[maxIndex]);


        bw.close();
        br.close();
    }

    static void func() {
        while (!pq.isEmpty()) {
            Node cur = pq.poll();

            if (dist[cur.vertex] != cur.cost) continue;

            for (Node nxt : adj.get(cur.vertex)) {
                if (dist[nxt.vertex] <= dist[cur.vertex] + nxt.cost) continue;

                dist[nxt.vertex] = dist[cur.vertex] + nxt.cost;
                pq.offer(new Node(dist[nxt.vertex], nxt.vertex));
            }
        }
    }


}
