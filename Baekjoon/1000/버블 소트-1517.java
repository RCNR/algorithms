// 버블 소트 1517
// 기존 버블 소트 문제와 비슷하지만 시간 복잡도를 O(NlogN)으로 풀어야한다.
// 세그먼트리의 병합 정렬로 분할 되었을 때의 뒷부분 그룹의 숫자가 앞부분으로 넘어올 때 몇개를 거쳐야하는지 카운트 해준다.

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;


public class Main {


    public static int[] board, tmp;
    public static long res;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        board = new int[n+3];
        tmp = new int[n+3];

        st = new StringTokenizer(br.readLine());

        for(int i = 1; i <= n; i++) {
            int num = Integer.parseInt(st.nextToken());
            board[i] = num;
        }

        mergeSort(1, n);

        bw.write(String.valueOf(res));
        bw.flush();
    }

    private static void mergeSort(int start, int end) {

        if(end - start <= 0) return;

        int mid = start + (end - start) / 2;

        mergeSort(start, mid); mergeSort(mid + 1, end);

        for(int i = start; i <= end; i++) tmp[i] = board[i];

        int idx1 = start, idx2 = mid + 1;
        int result_idx = start;

        while(idx1 <= mid && idx2 <= end) {
            if(tmp[idx1] > tmp[idx2]) {
                board[result_idx] = tmp[idx2];
                res += idx2 - result_idx;
                idx2++;
                result_idx++;
            }
            else {
                board[result_idx] = tmp[idx1];
                idx1++;
                result_idx++;
            }
        }

        while(idx1 <= mid) {
            board[result_idx] = tmp[idx1];
            idx1 ++; result_idx++;
        }

        while(idx2 <= end) {
            board[result_idx] = tmp[idx2];
            idx2++; result_idx++;
        }
    }

}
