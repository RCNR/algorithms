/**
 * Ten Player Bingo.java 34644
 * 마지막 빙고 -> 마지막 불리는 숫자의 일의 자리 구하기
 */

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        int lastNum = 0;
        for(int i = 0; i < 100; i++) {
            lastNum = Integer.parseInt(st.nextToken());
        }

        int last = lastNum % 10;
        System.out.println(last == 0 ? 10 : last);

    }
}