// 무한 수열.java 1351
// 부분 구간을 구해 답을 찾을 수 있다. 바텀없 방식으로 하면 모든 부분은 다 채워야하니
// 탑다운 방식 사용

import java.io.*;
import java.util.*;

public class Main{

    static long n, p, q;
    static Map<Long, Long> m = new HashMap<>();
//    static long[] is_visited;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Long.parseLong(st.nextToken());
        p = Long.parseLong(st.nextToken());
        q = Long.parseLong(st.nextToken());

        func(n);

        /*for(Map.Entry<Long, Long> entry : m.entrySet()) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }*/

        System.out.println(m.get(n));


    }

    public static long func(long num) {

        if(m.containsKey(num)) {
            return m.get(num);
        }

        if(num == 0) {
            m.put(num, 1L);
            return 1;
        }

        long first = num / p;
        long second = num / q;
        long res = func(first) + func(second);

        m.put(num, func(first) + func(second));

        return res;
    }


}