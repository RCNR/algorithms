// 트로피 진열.java 1668
// 왼쪽, 오른쪽 각 트로피가 보이는 개수 구하기
// 왼쪽에서부터 가장 큰 트로피보다 큰 트로피가 나올 때마다 개수 증가
// 오른쪽도 동일함

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] board = new int[n+3];

        for(int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            board[i] = num;
        }

        int st = board[0];
        int left = 1;
        for(int i = 1; i < n; i++) {
            if(st < board[i]) {
                st = board[i];
                left += 1;
            }
        }

        int en = board[n-1];
        int right = 1;
        for(int i = n-2; i >= 0; i--) {
            if(en < board[i]) {
                en = board[i];
                right += 1;
            }
        }
        System.out.println(left);
        System.out.println(right);

    }
}