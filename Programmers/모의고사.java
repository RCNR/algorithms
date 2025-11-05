import java.util.*;

// 완전탐색
// 수포자가 찍는 패턴을 배열로 저장하고, 정답과 비교하여 맞춘 개수를 세는 방식
// 가장 많이 맞춘 수포자의 번호를 찾아서 반환

class Solution {
    public int[] solution(int[] answers) {
        
        int[][] board = {
            {1,2,3,4,5},
            {2,1,2,3,2,4,2,5},
            {3,3,1,1,2,2,4,4,5,5}
        };
        
        int[] check = new int[3];
        
        for (int i = 0; i < board.length; i++) {
            int len = board[i].length;
            
            for (int j = 0; j < answers.length; j++) {
                if(answers[j] == board[i][j % len]) check[i] += 1;
            }
        }
        
        int num = Arrays.stream(check).max().getAsInt();
        ArrayList<Integer> res = new ArrayList<>();
        
        for(int i = 0; i < 3; i++) {
            if(check[i] == num) {
                res.add(i+1);
            }
        }
        
        return res.stream().mapToInt(Integer::intValue).toArray();
        
    }
}