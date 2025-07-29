// 2023 신기한 소수
// 한자리인 경우 (시작 지점)를 2,3,5,7로 고정하고 여기서부터 뒤에 붙일 수 있는(홀수)수들을 돌면서 붙인다.
// 붙이는 와중 소수인지 판별한다.

import java.io.*;
import java.util.*;

public class Main{

    public static ArrayList<Integer>[] adj;
    public static int[] basic = {2, 3, 5, 7};
    public static int[] checkNum = {1, 3, 5, 7, 9};
    public static int n;

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        func(2, 1);
        func(3, 1);
        func(5, 1);
        func(7, 1);



    }

    private static void func(int num, int idx) {

        if (idx == n) {
            if (isPrime(num)) {
                System.out.println(num);
            }
            return;
        }

        for (int i = 0; i < checkNum.length; i++) {
            boolean res = isPrime(num * 10 + checkNum[i]);
            if(res) {
                func(num * 10 + checkNum[i], idx + 1);
            }
            else continue;
        }
    }

    private static boolean isPrime(int number) {
        for(int i = 2; i <= (number / 2); i++) {
            if(number % i == 0) return false;
        }
        return true;
    }


}