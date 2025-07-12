// 1005 팔
// 그리디
// 자릿 수가 다른 경우, 자릿 수가 같고 각 idx 수가 짬뽕된 경우, 자릿 수가 같고 각 idx 둘 다 8로 된 경우를 구분하여 처리

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        String n = st.nextToken();
        String m = st.nextToken();

        int cnt = 0;

        if (n.length() != m.length()) {
            cnt = 0;
        } else if (n.equals(m) && n.chars().allMatch(c -> c == '8')) { // 자릿 수가 같고 각 idx 둘 다 8로 된 경우
            cnt = n.length();
        }
        else {
            for (int i = 0; i < n.length(); i++) { // 자릿 수가 같고 각 idx 수가 짬뽕된 경우
                if (n.charAt(i) != m.charAt(i)) {
                    break;
                }
                if (n.charAt(i) == '8' && n.charAt(i) == m.charAt(i)) {
                    cnt++;
                }
            }
        }
        System.out.println(cnt);
    }

}
