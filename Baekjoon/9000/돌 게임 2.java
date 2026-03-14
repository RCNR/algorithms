/**
 * 돌 게임 2.java 9656
 * 돌이 N개인 경우 마지막 돌을 가져가는 사람(지는 사람): 
 * 1 -> SK, 2 -> CY, 3 -> SK, 4 -> CY, 5 -> SK, 6 -> CY, 7 -> SK, 8 -> CY, 9 -> SK, 10 -> CY
 * 홀짝 구분하기
 * /

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        if ((n & 1) == 1) {
            System.out.println("CY");
        }
        else {
            System.out.println("SK");
        }
    }


}
