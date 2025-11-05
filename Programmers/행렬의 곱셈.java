// 프로그래머스 행렬의 곱셈

import java.util.*;

class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int row = arr1.length;
        int col = arr2[0].length;
        
        int[][] board = new int[row][col];
        // System.out.println(Arrays.toString(board[0]));
        
        for (int i = 0; i < row; i++) {
            for(int j = 0; j < col; j++) {
                for(int k = 0; k < arr2.length; k++) {
                    board[i][j] += arr1[i][k] * arr2[k][j];
                }
            }
        }
        return board;
    }
}