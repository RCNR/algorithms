/**
 * 진법 변환 2, 11005
 * 10진수를 어떤 x진법으로 바꾸는 방법만 알면 쉽게 풀 수 있다.
 * 이는 몫과 나머지를 이용하면 되고 Map을 이용해 0 ~ 35까지 할당된 값(0 ~ Z)을 넣어준다.
 */
import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ArrayList<String> list = new ArrayList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Map<Integer, String> m = new HashMap<>();

        for (int i = 0; i <= 35; i++) {
            if (i < 10) {
                m.put(i, String.valueOf(i));
            } else {
                m.put(i, String.valueOf((char) (i - 10 + 'A')));
            }
        }

       /* for (Integer i : m.keySet()) {
            System.out.println(i + " : " + m.get(i));
        }*/

        while (n > 0) {
            int res = n % k;
            list.add(m.get(res));
            n /= k;
        }

        for (int i = list.size() - 1; i >= 0; i--) {
            System.out.print(list.get(i));
        }
    }

}
