/**
 * 경매.java 2238
 * 값을 부른 가장 작은 인원을 갖고 있는 가격 및 빨리 부른 인원 구하기
 * (가격, list(인원))
 */

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        List<String>[] priceList = new ArrayList[10003];

        for (int i = 1; i <= 10000; i++) {
            priceList[i] = new ArrayList<>();
        }

        st = new StringTokenizer(br.readLine());
        int u = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int price = Integer.parseInt(st.nextToken());
            priceList[price].add(name);
        }

        int minSize = Integer.MAX_VALUE;
        for (int i = 1; i <= 10000; i++) {
            if (priceList[i].size() > 0) {
                minSize = Math.min(minSize, priceList[i].size());
            }
        }

        for(int i = 1; i <= 10000; i++) {
            if (priceList[i].size() == minSize) {
                System.out.println(priceList[i].get(0) + " " + i);
                break;
            }
        }


    }

}

