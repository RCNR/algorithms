/**
 * 베르트랑 공주.java 4948
 * 에라토스테네스의 체를 이용해서 2n까지 소수를 먼저 구하고
 * (입력 값, 2n] 범위 내에서 소수 개수 세기
 */

import java.util.*;
import java.io.*;

public class Main {



    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int[] board = new int[250000];
        board[1] = 1;

        for(int i = 2; i <= 123456; i++) {
            if (board[i] == 0) {
                int mul = 2;
                while (mul * i < 250000) {
                    board[mul * i] = 1;
                    mul++;
                }
            }
        }

        while(true) {
            int num = Integer.parseInt(br.readLine());
            if (num == 0) break;

            int cnt = 0;

            for (int i = num + 1; i <= 2 * num; i++) {
                if (board[i] == 0) {
                    cnt += 1;
                }
            }
            System.out.println(cnt);
        }


    }
}

