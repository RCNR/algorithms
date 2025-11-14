/**
 * 물건 팔기.java 1487
 * 물건을 살 수 있을 때 가장 이익이 많이 남는 가격을 구하는 문제
 * 물건을 살 때 사람마다 배송비가 든다.
 * 그런데 특정 가격에 사람마다 동일한 배송비가 지불되는 줄 알았다.
 * 같은 비용이어도 사람마다 배송비가 다르다
 */

import java.util.*;
import java.io.*;

public class Main {

    static class Pair {
        int x;
        int y;
        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int n;
    static List<Pair> board = new ArrayList<>();

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        int t = n;
        while(t-- > 0) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            board.add(new Pair(x, y));
        }

        board.sort((a, b) -> {
            if (a.x == b.x) return a.y - b.y;
            return a.x - b.x;
        });

        int profit = 0;
        int best = 0;

        for (int i = 0; i < n; i++) {
            int price = board.get(i).x;
            int cur_profit = 0;

            for (int j = 0; j < n; j++) {
                if (board.get(j).x >= price) {

                    if (price - board.get(j).y > 0) cur_profit += price - board.get(j).y;
                }
            }

            if (cur_profit > profit) {
                profit = cur_profit;
                best = price;
            }
        }

        System.out.println(best);
    }
}

