// K번째 수 1300

import java.io.*;
import java.util.*;

public class Main{

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        /**
         * 2차원 배열의 k번째 수는 k를 넘길 수 없다
         * 2차원 배열에서 어떤 중간값(mid) 보다 작거나 같은 값이 몇 개가 있는지 확인하려면
         * mid / (1~N) 까지 해서 더 해준다. 더 하면 총 값은 mid보다 작거나 같은 개수다 -> cnt라고 하겠다
         * mid의 cnt보다 k가 작다면 st = mid + 1
         * mid의 cnt보다 k가 크거나 같다면 end = mid - 1
         *
         */

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());

        long low = 1;
        long high = k;

        low--;
        high++;

        while(low + 1 < high) {

            long mid = (low + high) / 2;
            long cnt = 0;
//            System.out.println("mid = " + mid);

            for(int i = 1; i <= n; i++) {
                long num = Math.min(n, mid / i);
//                System.out.println(num);
                cnt += num;
            }

            if (cnt < k) low = mid;
            else high = mid;
        }

        System.out.println(high);


    }
}