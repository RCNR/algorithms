import java.util.*;
import java.io.*;

/**
 * a^(p-1) => 1 (mod p)
 * a^(p-2) => a^(-1)  (mod p)
 * 
 * N^(MOD-2) mod MOD
 * 분할 정복 이용한 거듭제곱 -> 페르마의 소정리 활용
 * 3^(-1) ≡ 4 (mod 11)
 * 
 */

public class Main {

    static long MOD = 1000000007;
    static long res = 0;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int S = Integer.parseInt(st.nextToken());

            long nInverse = powerFunc(N, MOD - 2); // N^(MOD - 2)

            long expect = (S * nInverse) % MOD;

            res = (res + expect) % MOD;

        }

        System.out.println(res);

    }

    private static long powerFunc(int num, long exp) {

        if (exp == 0) return 1;

        long half = powerFunc(num, exp / 2);

        long result = (half * half) % MOD;

        if (exp % 2 == 1) {
            return (result * num) % MOD;
        }
        else {
            return result;
        }

    }

}