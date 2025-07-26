// 버블 소트 1377 
// swap이 얼마나 발생했는지 알아야 한다. 문제 코드는 가장 큰 숫자부터 정렬한다.
// 기존 배열에서 오른쪽에 있던 수들이 몇 번만에 왼쪽으로 왔는지 알아야 한다.

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class Pair {
    int value, idx;

    public Pair(int value, int idx) {
        this.value = value;
        this.idx = idx;
    }
}

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;
        ArrayList<Pair> board = new ArrayList<>();

        int n = Integer.parseInt(br.readLine());
        for(int i = 1; i <= n; i++) {
            int num = Integer.parseInt(br.readLine());
            board.add(new Pair(num, i));
        }

        board.sort(Comparator.comparingInt(o -> o.value));
        int maxNum = 0;

        for(int i = 1; i <= n; i++) {
            int prev_idx = board.get(i-1).idx;
            maxNum = Math.max(prev_idx - i, maxNum); // 정렬 전 idx - 정렬 후 idx
        }

        bw.write(String.valueOf(maxNum + 1));
        bw.flush();

    }
}
