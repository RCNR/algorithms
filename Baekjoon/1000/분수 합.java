/**
 * 분수 합.java 1735
 * 두 분수의 합을 기약분수로 나타내기
 * 분수의 합을 구한다음에 최대공약수로 나누기
 * 최대공약수는 유클리드 호제법을 재귀로 구현
 */

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;


        st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        int mol = a * d + c * b;
        int den = b * d;

        int res = gcd(mol, den);

        System.out.println(mol / res  + " " + den / res);




    }

    private static int gcd(int mol, int den) {

        if(den == 0) return mol;

        return gcd(den, mol % den);

    }

}

