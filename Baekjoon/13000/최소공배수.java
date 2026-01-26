/**
 * 최소공배수.java 13241
 * gcd로 최대공약 수 구하고, lcm 구할 수 있도록 구성
 */

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        long n, m;
        st = new StringTokenizer(br.readLine());
        n = Long.parseLong(st.nextToken());
        m = Long.parseLong(st.nextToken());

        long res = func(n, m);
        System.out.println(res);

    }

    public static long func(long a, long b) {
        return Math.abs(a * (b / gcd(a, b)));
    }

    public static long gcd(long a, long b) {

        while (b != 0) {
            long temp = a % b;
            a = b;
            b = temp;
        }

        return a;
    }

}