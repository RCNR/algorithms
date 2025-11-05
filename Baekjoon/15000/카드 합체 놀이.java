// 카드 합체 놀이.java 15903
// 우선순위 큐를 활용한 그리디 풀이

import java.io.*;
import java.util.*;

public class Main{

    static int n, m;
    static int[] board;
    static PriorityQueue<Long> PQ = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine())
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            long num = Integer.parseInt(st.nextToken());
            PQ.offer(num);
        }

        while (m--) {
            long cur_1 = PQ.poll();
            long cur_2 = PQ.poll();
            long sum = cur_1 + cur_2;

            PQ.offer(sum);
            PQ.offer(sum);
        }


        long sum = 0;
        for (long val : PQ) {
            sum += val;
        }

        System.out.println(sum);
    }
}