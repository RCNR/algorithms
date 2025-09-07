// 1672.java DNA 해독
// 염기서열에 따른 조건문 잘 세우기

import java.io.*;
import java.util.*;

public class Main{

    static int n;
    static String s;
    static int[][] board;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        s = new StringTokenizer(br.readLine());

        board = {
            {'A', 'C', 'A', 'G'},
            {'C', 'G', 'T', 'A'},
            {'A', 'T', 'C', 'G'},
            {'G', 'A', 'G', 'T'}
        }

        int len = s.length()
        back = func(s[len-1]);
        

        for(int i = len-2; i >= 0; i--) {
            int front = func(i);
            new_back = board[front][back];
            back = res;
        }

        System.out.println(back);
    }

    public static int func(char spell) {
        if spell == 'A' return 0;
        else if spell == 'G' return 1;
        else if spell == 'C' return 2;
        else if spell == 'T' return 3;
    }

}