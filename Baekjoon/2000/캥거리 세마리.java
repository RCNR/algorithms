/**
 * 캥거루 세마리.java 2965
 * a, b, c는 크기 순으로 주어지니, b를 기준으로 a와 c의 거리를 구해주고, 
 * 그 중에서 가장 큰 값을 출력하면 된다.
 */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

      System.out.println(Math.max(c-b-1, Math.abs(a-b)-1));
    }
}