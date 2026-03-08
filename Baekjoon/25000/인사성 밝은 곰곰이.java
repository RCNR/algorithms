/**
 * 인사성 밝은 곰곰이.java 25192
 * ENTER 입력 시, 지금까지 입력된 이모티콘은 모두 사라진다.
 * 입력된 이모티콘이 사라지기 전에 몇 개의 이모티콘이 입력되었는지
 */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        Set<String> emoticon = new HashSet<>();
        int cnt = 0;

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            if (s.equals("ENTER")) {
                emoticon.clear();
            }
            else {
                if (!emoticon.contains(s)) {
                    emoticon.add(s);
                    cnt++;
                }
            }
        }

        System.out.print(cnt);
    }
}