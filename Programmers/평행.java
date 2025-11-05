import java.util.*;

class Pair<A, B> {
    A x;
    B y;

    Pair(A x, B y) {
        this.x = x;
        this.y = y;
    }
}

class Solution {
    public int solution(int[][] dots) {
        
        for(int i = 1; i < 4; i++) {
            int res = func(dots, 0, i);
            if(res == 1) return 1;
        }
        return 0;
       
    }
    
    public int func(int[][] board, int first, int second) {
        
        boolean[] is_visited = new boolean[4];
        List<Pair<Integer, Integer>> a = new ArrayList<>();
        List<Pair<Integer, Integer>> b = new ArrayList<>();
        
        a.add(new Pair<>(board[first][0], board[first][1]));
        a.add(new Pair<>(board[second][0], board[second][1]));
        
        is_visited[first] = true;
        is_visited[second] = true;
        
        for(int i = 0; i < 4; i++) {
            if (!is_visited[i]) {
                b.add(new Pair<>(board[i][0], board[i][1]));
            }
        }
        
        if (
            ((a.get(0).x - a.get(1).x) * (b.get(0).y - b.get(1).y)) ==
           ((a.get(0).y - a.get(1).y ) * (b.get(0).x - b.get(1).x))
        ) {
            System.out.println(a.get(0).x + " " + a.get(0).y + " " + a.get(1).x + " " + a.get(1).y );
            System.out.println(b.get(0).x + " " + b.get(0).y + " " + b.get(1).x + " " + b.get(1).y );
            return 1;
        }
        else return 0;
    }
}