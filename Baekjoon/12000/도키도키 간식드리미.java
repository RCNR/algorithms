/**
 * 12789번: 도키도키 간식드리미
 * https://www.acmicpc.net/problem/12789
 * 문제 유형: 자료구조, 스택, 덱
 * 풀이 방법:
 * - 덱을 사용하여 입력된 순서대로 사람들을 처리한다.
 * - 현재 순서(order)와 비교하여, 현재 사람이 설 수 있는 공간에 들어갈 수 있는지 확인한다.
 * - 만약 현재 사람이 설 수 있는 공간에 들어갈 수 없다면, 스택에 넣고,
 * - 스택의 맨 위에 있는 사람이 설 수 있는 공간에 들어갈 수 있는지 확인한다.
 * - 모든 사람이 설 수 있는 공간에 들어갈 수 있다면 "Nice"를 출력하고, 그렇지 않다면 "Sad"를 출력한다.
 */
import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        Deque<Integer> dq = new ArrayDeque<>();
        Stack<Integer> s = new Stack<>();
        ArrayList<Integer> result = new ArrayList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            dq.add(num);
        }

        int order = 1;
        while (!dq.isEmpty()) {
            int cur = dq.pollFirst();
            if (cur != order) { // 한 명씩 설 수 있는 공간에서 빼올 수 있다.
                while (!s.isEmpty() && s.peek() == order) {
                    result.add(s.pop());
                    order++;
                }
            }
            if (cur != order) {
                s.push(cur);
                continue;
            }
            result.add(cur);
            order++;
        }

        while (!s.empty()) {
            int cur = s.pop();
            result.add(cur);
        }

        for (int i = 0; i < n; i++) {
            if (result.get(i) != i + 1) {
                bw.write("Sad");
                bw.flush();
                System.exit(0);
            }
        }
        bw.write("Nice");
        bw.flush();

    }
}
