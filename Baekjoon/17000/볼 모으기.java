/**
 * 볼 모으기.java 17615
 * 단순하게 빨간공을 오른쪽에 몰아버리는 경우를 생각한다
 * 이때 오른쪽 빨간공은 옮길 필요 없이 파란공을 지나 나오는 빨간공의 개수만 카운트하게 된다
 * 빨간공을 오른쪽으로 모두 몰아 넣었다면 자연스럽게 파란공도 몰아넣어지게 된다.
 * 복잡하게 생각하기 보단 단순하게 생각해야했다.
 * 
 * 왼쪽, 오른쪽 각각 모두 모으는 경우를 빨, 파 모두 각각 구해준 후 최솟값을 구한다. 
 */

import java.io.*;
import java.util.*;

public class Main{

    static int n, red_sum, blue_sum;
    static char[] board;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        n = Integer.parseInt(br.readLine());
        String s = br.readLine();

        for(int i = 0; i < n; i++) {
            if (s.charAt(i) == 'R') red_sum ++;
            else blue_sum++;
        }

        int leftRed = front(s, 'R');
        int rightRed = back(s, 'R');

        int leftBlue = front(s, 'B');
        int rightBlue = back(s, 'B');

        int redMin = Math.min(red_sum - leftRed, red_sum - rightRed);
        int blueMin = Math.min(blue_sum - leftBlue, blue_sum - rightBlue);

        System.out.println(Math.min(redMin, blueMin));
    }

    private static int front(String s, char isRedOrBlue) {

        int cnt = 0;

        for(int i = 0; i < s.length() && s.charAt(i) == isRedOrBlue; i++) {
            cnt++;
        }

        return cnt;
    }

    private static int back(String s, char isRedOrBlue) {
        int cnt = 0;

        for(int i = s.length() - 1; i >= 0 && s.charAt(i) == isRedOrBlue; i--) {
            cnt ++;
        }

        return cnt;
    }

}